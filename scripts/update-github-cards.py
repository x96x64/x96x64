#!/usr/bin/env python3
"""Refresh the existing public cards and apply the viewer's system UI font.

Uses the Python standard library. Fetch and validate every card before writing
anything, so a provider failure leaves the last successful set in place.
"""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "github"
FONT_STACK = 'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
FONT_STYLE = f'<style id="profile-system-font">text, tspan {{ font-family: {FONT_STACK} !important; }}</style>'
NS = "{http://www.w3.org/2000/svg}"


def sources():
    for theme in ("light", "dark"):
        stats_theme = "default" if theme == "light" else "github_dark"
        common = {"username": "x96x64", "hide_border": "true", "theme": stats_theme}
        for name, endpoint, options in (
            ("stats", "api", {"show_icons": "true", "include_all_commits": "true"}),
            ("languages", "api/top-langs/", {"layout": "compact"}),
            ("ilyrics", "api/pin/", {"repo": "ilyrics", "show_owner": "true"}),
        ):
            yield f"{name}-{theme}.svg", "https://github-readme-stats.vercel.app/" + endpoint + "?" + urlencode(common | options)
        yield f"streak-{theme}.svg", "https://streak-stats.demolab.com?" + urlencode({
            "user": "x96x64", "hide_border": "true",
            "theme": "default" if theme == "light" else "github-dark-blue",
        })
        yield f"trophies-{theme}.svg", "https://github-trophies.vercel.app/?" + urlencode({
            "username": "x96x64", "theme": "flat" if theme == "light" else "darkhub",
            "no-frame": "true", "no-bg": "true", "margin-w": "8", "column": "6",
        })


def apply_system_font(svg):
    root = ET.fromstring(svg)
    if root.tag != NS + "svg" or next(root.iter(NS + "text"), None) is None:
        raise ValueError("Expected an SVG card containing text")
    if "viewBox" in root.attrib:
        box = [float(value) for value in root.attrib["viewBox"].replace(",", " ").split()]
        if len(box) != 4 or box[2] <= 0 or box[3] <= 0:
            raise ValueError("Invalid card dimensions")
    visible_text = " ".join(" ".join(e.itertext()) for e in root.iter()
                            if e.tag in (NS + "text", NS + "title", NS + "desc"))
    if re.search(r"something went wrong|could not fetch|rate limit|maximum retries|user not found", visible_text, re.I):
        raise ValueError(f"Provider returned an error card: {visible_text[:200]}")
    if any(e.tag in (NS + "script", NS + "foreignObject") for e in root.iter()):
        raise ValueError("Unexpected active content in SVG card")
    if 'id="profile-system-font"' in svg:
        raise ValueError("Card has already been processed")
    # !important also overrides presentation attributes and inline family styles.
    # Keep sizes, weights, labels, metrics, links, and provider artwork unchanged.
    result = re.sub(r"</svg>\s*$", FONT_STYLE + "\n</svg>\n", svg, count=1)
    if result == svg:
        raise ValueError("Missing closing SVG element")
    result = re.sub(r"(?m)^[ \t]+$", "", result)
    ET.fromstring(result)
    return result


def fetch(item):
    name, url = item
    request = Request(url, headers={"User-Agent": "x96x64-profile-cards", "Accept": "image/svg+xml"})
    with urlopen(request, timeout=60) as response:
        svg = response.read(2_000_001)
    if len(svg) > 2_000_000:
        raise ValueError(f"Oversized card: {name}")
    return name, apply_system_font(svg.decode("utf-8"))


def main():
    with ThreadPoolExecutor(max_workers=3) as pool:
        cards = list(pool.map(fetch, sources()))
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for name, svg in cards:
        (OUTPUT / name).write_text(svg, encoding="utf-8")
        print(f"Updated {name}")


if __name__ == "__main__":
    main()
