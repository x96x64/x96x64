# hello

[![LinkedIn](https://img.shields.io/badge/LinkedIn-x96x64-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/x96x64)
[![Swift](https://img.shields.io/badge/Swift-6-F05138?logo=swift&logoColor=white)](https://www.swift.org)
[![macOS](https://img.shields.io/badge/macOS-14%2B-000000?logo=apple&logoColor=white)](https://www.apple.com/macos/)
[![Core ML](https://img.shields.io/badge/Core%20ML-on--device-34C759?logo=apple&logoColor=white)](https://developer.apple.com/documentation/coreml)
[![Open source](https://img.shields.io/badge/open%20source-Apache--2.0-blue)](https://github.com/x96x64/ilyrics/blob/main/LICENSE)

I am a student and independent developer in Japan. I build quiet tools: software that improves your work without asking for your attention. Most of what I make lives on the command line or runs entirely on the device in front of you, and most of it is free and open-source software that anyone can read, run, and improve.

## What I Believe

Technology should be a means to a better experience, not a feature to be noticed. I am inspired by Apple's approach to Apple Intelligence and Siri, where intelligence quietly improves what you are already doing instead of asking you to change how you work. The best tools are the ones you hardly notice using, until you realize that your work has quietly become better.

In practice, this means that I care about the moments around the main task as much as the task itself. A command should check its inputs before it spends minutes on them, explain a problem in plain language when something goes wrong, leave nothing half-finished behind when it is interrupted, and produce the same result every time it is given the same input. None of these details is visible when everything works, and that is the point.

## What I Am Building

[![iLyrics](social-preview.png)](https://github.com/x96x64/ilyrics)

[iLyrics](https://github.com/x96x64/ilyrics) is a macOS command that renders lyrics videos reproducing the Lyrics screen of the Music app on iPhone, and synchronizes plain English lyrics to a recording entirely on your Mac. You give it a song and its lyrics; it separates the vocals, finds where every word is sung, and renders a 1080 × 1920 video at 60 frames per second, ready for phones and social platforms. Recordings, lyrics, and videos never leave your computer.

Under the hood, HTDemucs separates the vocals and wav2vec 2.0 recognizes them through Core ML, and a CTC forced alignment places every character of the lyrics. Every frame is a pure function of its timestamp, drawn with Core Text and Core Graphics, so a video can be rendered in parallel and reproduced exactly. On 80 unseen recordings with manual word timing, 95.9% of lines were placed correctly. The screen itself was measured against screen recordings of the Music app on iOS 27, and the known differences are documented rather than hidden.

[![Homebrew](https://img.shields.io/badge/Homebrew-x96x64%2Ftap-FBB040?logo=homebrew&logoColor=white)](https://github.com/x96x64/homebrew-tap)
[![npm](https://img.shields.io/npm/v/ilyrics?logo=npm&color=CB3837)](https://www.npmjs.com/package/ilyrics)
[![PyPI](https://img.shields.io/pypi/v/ilyrics?logo=pypi&logoColor=white&color=3775A9)](https://pypi.org/project/ilyrics/)

iLyrics is written in Swift and distributed through Homebrew, npm, and PyPI.

#### Homebrew

```bash
brew install x96x64/tap/ilyrics
```

#### npm

```bash
npm install -g ilyrics
```

#### pip

```bash
pipx install ilyrics
```

Without pipx, `pip install ilyrics` installs it as well.

## How I Work

I develop together with AI coding agents. Codex and Claude take part in planning, implementation, review, and documentation, and their contributions are credited in the commit history. I decide what to build, set the constraints, and review every change before it ships; the agents make it possible for one person to keep the standards of a team, from atomic commits and continuous integration to written reports that record every measurement and every decision.

## Interests

My interests are AI agents and bots, command-line tools, free and open-source software, and audio and music files. Away from the keyboard, I listen to a lot of music from the 1960s through the 1990s, above all Michael Jackson and The Beatles. My favorite Michael Jackson album is *HIStory: Past, Present and Future, Book I*, and my favorite of his songs is its title track, "HIStory." My favorite Beatles album is *The Beatles*, better known as the White Album, and my favorite of their songs is "Yellow Submarine," from *Yellow Submarine*.

## GitHub Stats

These cards are generated from my public GitHub activity and update on their own.

[![Re:COO's GitHub stats](https://github-readme-stats.vercel.app/api?username=x96x64&show_icons=true&hide_border=true&include_all_commits=true)](https://github.com/x96x64)
[![Top languages](https://github-readme-stats.vercel.app/api/top-langs/?username=x96x64&layout=compact&hide_border=true)](https://github.com/x96x64)

[![GitHub streak](https://streak-stats.demolab.com?user=x96x64&hide_border=true)](https://github.com/x96x64)

[![Trophies](https://github-trophies.vercel.app/?username=x96x64&theme=flat&no-frame=true&no-bg=true&margin-w=8&column=-1)](https://github.com/x96x64)

[![iLyrics repository card](https://github-readme-stats.vercel.app/api/pin/?username=x96x64&repo=ilyrics&show_owner=true&hide_border=true)](https://github.com/x96x64/ilyrics)

## Contributions

Every day, a snake makes its way through my contribution graph and eats the squares in the order they were earned.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/x96x64/x96x64/output/github-snake-dark.svg">
  <img alt="A snake eating the squares of Re:COO's contribution graph" src="https://raw.githubusercontent.com/x96x64/x96x64/output/github-snake.svg">
</picture>

## Recent Activity

My latest public activity on GitHub, updated automatically every six hours:

<!--START_SECTION:activity-->
1. 🚀 Published release [iLyrics: v1.2.0, Lyrics Videos of the iPhone Music Lyrics Screen for macOS](https://github.com/x96x64/ilyrics/releases/tag/v1.2.0) in [x96x64/ilyrics](https://github.com/x96x64/ilyrics)
2. 🚀 Published release [iLyrics: v1.1.0, Lyrics Videos of the iPhone Music Lyrics Screen for macOS](https://github.com/x96x64/ilyrics/releases/tag/v1.1.0) in [x96x64/ilyrics](https://github.com/x96x64/ilyrics)
3. 🚀 Published release [iLyrics: v1.0.1, Lyrics Videos of the iPhone Music Lyrics Screen for macOS](https://github.com/x96x64/ilyrics/releases/tag/v1.0.1) in [x96x64/ilyrics](https://github.com/x96x64/ilyrics)
4. 🚀 Published release [iLyrics: v1.0.0, Lyrics Videos of the iPhone Music Lyrics Screen for macOS](https://github.com/x96x64/ilyrics/releases/tag/v1.0.0) in [x96x64/ilyrics](https://github.com/x96x64/ilyrics)
5. 🚀 Published release [iLyrics: v0.2.0, Lyrics Videos of the iPhone Music Lyrics Screen for macOS](https://github.com/x96x64/ilyrics/releases/tag/v0.2.0) in [x96x64/ilyrics](https://github.com/x96x64/ilyrics)
<!--END_SECTION:activity-->

## Get in Touch

You can find my work here on GitHub and my background on [LinkedIn](https://www.linkedin.com/in/x96x64). For questions or problems with iLyrics, please open an issue in the [iLyrics repository](https://github.com/x96x64/ilyrics/issues), where everyone can benefit from the answer.
