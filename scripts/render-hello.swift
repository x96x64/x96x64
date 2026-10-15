// Render the approved lowercase greeting without embedding or redistributing a font.
// Usage (macOS): swift scripts/render-hello.swift /path/to/MacintoshSkeletalFilled.otf assets/hello
// Source and usage conditions are recorded in assets/hello/NOTICE.txt.
import Foundation
import CoreGraphics
import CoreText

guard CommandLine.arguments.count == 3 else {
    fatalError("Usage: render-hello.swift FONT_PATH OUTPUT_DIRECTORY")
}
let fontURL = URL(fileURLWithPath: CommandLine.arguments[1])
let outputURL = URL(fileURLWithPath: CommandLine.arguments[2], isDirectory: true)
guard let provider = CGDataProvider(url: fontURL as CFURL),
      let graphicsFont = CGFont(provider) else {
    fatalError("Unable to read the supplied font")
}
let font = CTFontCreateWithGraphicsFont(graphicsFont, 96, nil, nil)
guard CTFontCopyFamilyName(font) as String == "Macintosh Skeletal Filled" else {
    fatalError("Expected Macintosh Skeletal Filled")
}
let text = NSAttributedString(string: "hello", attributes: [
    NSAttributedString.Key(kCTFontAttributeName as String): font
])
// Core Text applies contextual alternates and includes the connecting glyphs.
let line = CTLineCreateWithAttributedString(text)
let outline = CGMutablePath()
var glyphCount = 0
for run in CTLineGetGlyphRuns(line) as! [CTRun] {
    let count = CTRunGetGlyphCount(run)
    let attributes = CTRunGetAttributes(run) as NSDictionary
    let runFont = attributes[kCTFontAttributeName] as! CTFont
    var glyphs = [CGGlyph](repeating: 0, count: count)
    var positions = [CGPoint](repeating: .zero, count: count)
    CTRunGetGlyphs(run, CFRange(location: 0, length: 0), &glyphs)
    CTRunGetPositions(run, CFRange(location: 0, length: 0), &positions)
    for index in 0..<count {
        guard glyphs[index] != 0 else { fatalError("Missing glyph") }
        if let path = CTFontCreatePathForGlyph(runFont, glyphs[index], nil) {
            outline.addPath(path, transform: CGAffineTransform(
                translationX: positions[index].x, y: positions[index].y))
        }
    }
    glyphCount += count
}
let bounds = outline.boundingBoxOfPath
let padding: CGFloat = 4
var transform = CGAffineTransform(a: 1, b: 0, c: 0, d: -1,
    tx: padding - bounds.minX, ty: bounds.maxY + padding)
guard let normalized = outline.copy(using: &transform) else { fatalError("Empty outline") }
func number(_ value: CGFloat) -> String {
    String(format: "%.3f", locale: Locale(identifier: "en_US_POSIX"), Double(value))
}
func point(_ point: CGPoint) -> String { "\(number(point.x)) \(number(point.y))" }
var commands = [String]()
normalized.applyWithBlock { pointer in
    let element = pointer.pointee
    switch element.type {
    case .moveToPoint: commands.append("M\(point(element.points[0]))")
    case .addLineToPoint: commands.append("L\(point(element.points[0]))")
    case .addQuadCurveToPoint:
        commands.append("Q\(point(element.points[0])) \(point(element.points[1]))")
    case .addCurveToPoint:
        commands.append("C\(point(element.points[0])) \(point(element.points[1])) \(point(element.points[2]))")
    case .closeSubpath: commands.append("Z")
    @unknown default: fatalError("Unknown path element")
    }
}
try FileManager.default.createDirectory(at: outputURL, withIntermediateDirectories: true)
let width = number(bounds.width + padding * 2)
let height = number(bounds.height + padding * 2)
for (theme, color) in [("light", "#1f2328"), ("dark", "#f0f6fc")] {
    let svg = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 \(width) \(height)" width="96" role="img" aria-labelledby="hello-title">
      <title id="hello-title">hello</title>
      <!-- Outlined Macintosh Skeletal Filled; see NOTICE.txt for source and conditions. -->
      <path fill="\(color)" d="\(commands.joined(separator: " "))"/>
    </svg>

    """
    try svg.write(to: outputURL.appendingPathComponent("hello-\(theme).svg"), atomically: true, encoding: .utf8)
}
print("Rendered hello with \(glyphCount) shaped glyphs; viewBox 0 0 \(width) \(height)")
