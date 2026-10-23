<h1>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/hello/hello-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/hello/hello-light.svg">
    <img src="assets/hello/hello-light.svg" alt="Hello" width="96">
  </picture>
</h1>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-x96x64-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/x96x64)
[![Swift](https://img.shields.io/badge/Swift-6-F05138?logo=swift&logoColor=white)](https://www.swift.org)
[![macOS](https://img.shields.io/badge/macOS-14%2B-000000?logo=apple&logoColor=white)](https://www.apple.com/macos/)
[![Codex: Agent](https://img.shields.io/badge/Codex-Agent-374151)](#how-i-work)
[![Claude: Agent](https://img.shields.io/badge/Claude-Agent-D97757)](#how-i-work)
[![CLI: Tools](https://img.shields.io/badge/CLI-Tools-334155)](#what-i-believe)
[![iLyrics Release](https://img.shields.io/github/v/release/x96x64/ilyrics?label=iLyrics)](https://github.com/x96x64/ilyrics/releases/latest)
[![iLibrary Release](https://img.shields.io/github/v/release/x96x64/ilibrary?label=iLibrary)](https://github.com/x96x64/ilibrary/releases/latest)

I am a student and independent developer in Japan. I build quiet tools: software that improves your work without asking for your attention. Most of what I make lives on the command line or runs entirely on the device in front of you, and most of it is free and open-source software that anyone can read, run, and improve.

## What I Believe

Technology should be a means to a better experience, not a feature to be noticed. I am inspired by Apple's approach to Apple Intelligence and Siri AI, where intelligence quietly improves what you are already doing instead of asking you to change how you work. The best tools are the ones you hardly notice using, until you realize that your work has quietly become better.

In practice, this means that I care about the moments around the main task as much as the task itself. A command should check its inputs before it spends minutes on them, explain a problem in plain language when something goes wrong, leave nothing half-finished behind when it is interrupted, and produce the same result every time it is given the same input. None of these details is visible when everything works, and that is the point.

## How I Work

I develop together with AI coding agents. Codex and Claude take part in planning, implementation, review, and documentation, and their contributions are credited in the commit log. I decide what to build, set the constraints, and review every change before it ships.

The agents make it possible for one person to keep the standards of a team: small commits that follow Conventional Commits, continuous integration on every pull request, a regression test with every safety fix, and documentation that is corrected whenever the behavior it describes changes. Both projects state their engineering constraints in the repository, so that a human contributor and an agent are held to the same rules.

## What I Am Building

I am currently building two command-line tools for macOS, iLyrics and iLibrary. Both are written in Swift and published as free and open-source software under the Apache License, Version 2.0. Both run on the Mac without any network service, apart from the one-time download of the alignment models that iLyrics needs, and both are designed to state what they will do before they do it. The two projects share conventions: commands with verbs as subcommands, a `doctor` command that gives a recovery step for each problem it finds, and honest statements of what has and has not been measured.

### iLyrics

[iLyrics](https://github.com/x96x64/ilyrics) is a macOS command-line tool that creates synchronized lyrics videos reproducing the Lyrics screen of the Music app on iPhone. You give it a song and its plain English lyrics; it separates the vocals, estimates where the words are sung, and renders a 1080 × 1920 video at 60 frames per second, ready for phones and social platforms. Recordings, lyrics, and videos never leave your computer.

Under the hood, HTDemucs separates the vocals and wav2vec 2.0 produces character probabilities through Core ML, which CTC forced alignment uses to estimate the timing of the supplied lyrics. Every frame is a pure function of its timestamp, drawn with Core Text and Core Graphics, so frames can be evaluated independently and rendered in parallel; this reproducibility concerns frame generation under fixed rendering conditions. The alignment models are installed once, on first use, from their publishers' weights, which are verified against pinned digests and rebuilt as Core ML models on your Mac.

In the [historical evaluation](https://github.com/x96x64/ilyrics/blob/main/docs/reports/third-preview-qualification-results.md) of commit `e0ab92a` on 80 unseen recordings with manual word timing, 95.9% of 3,005 scored lines had an accepted interval overlapping the reference interval, but three recordings fell below the per-recording placement threshold of 80%. This measures line placement rather than word-timing accuracy, and the complete locked qualification criteria were not met. The screen itself was measured against screen recordings of the Music app on iOS 27, and the known differences are documented rather than hidden. Automatic synchronization supports English and may require manual correction; Japanese synchronization is experimental.

#### Installing iLyrics

iLyrics requires macOS 14 or later on Apple silicon. It is distributed through Homebrew, npm, and PyPI; install it through one channel only, so that updating that channel updates the `ilyrics` you run. The first alignment of plain English lyrics downloads about 460 MB of model weights from their publishers, which iLyrics rebuilds as Core ML models on your Mac. You can install them in advance with `ilyrics models install`, and `ilyrics doctor` shows the installed version and the command that updates it.

```bash
brew install x96x64/tap/ilyrics
npm install -g ilyrics
pipx install ilyrics    # or: pip install ilyrics
```

### iLibrary

[iLibrary](https://github.com/x96x64/ilibrary) is a macOS command-line tool that prepares downloaded and purchased music for a local Apple Music library and adds it in a controlled order. On import, it converts FLAC, WAV, and AIFF downloads to Apple Lossless and verifies each result by comparing the decoded audio with the source, and it copies iTunes Store purchases without re-encoding while removing the purchaser's account, name, purchase date, and store identifiers. Every command that changes files or the library offers a dry run, states what it will change before changing it, and verifies its result afterwards.

The work is organized around a catalog: a JSON document that describes albums, tracks, release dates, and title rules. A catalog is drafted from the tags of existing files, completed by hand or with an AI agent, validated against the files, and applied. Applying it writes the metadata without re-encoding the audio, can remove qualifiers such as "(2012 Remaster)" and apply MLA, APA, or start-case capitalization to titles, names files and folders as the Music app does, and sets file dates to release dates. The [catalog documentation](https://github.com/x96x64/ilibrary/blob/main/docs/catalogs.md) describes the format and the matching rules.

Albums are then added to Music one at a time, in one of four orders: by release date, by artist, by artist in descending order, or by artist and then release date. iLibrary waits until the clock has passed the addition second of the previous album, so that the Recently Added view shows the albums in the intended order. Two diagnostic commands support the workflow: `check` reports missing tags, duplicate tracks, and incorrect dates, and compares the files with the library's records, while `doctor` reports problems with the environment and the steps to recover from them. An existing library can also be rebuilt in stages. The rebuild begins with a backup on separate storage that iLibrary verifies and test-restores. It then moves the files out of the media folder, removes exactly the registrations it recorded, writes the catalog to the files, and adds the albums again. Each stage records its progress and refuses to run out of order. The [library operations guide](https://github.com/x96x64/ilibrary/blob/main/docs/library-operations.md#rebuilding-a-library) describes the procedure.

The Swift package separates portable processing from macOS integration. `MP4Core` parses and rewrites MP4 boxes and relocates chunk offsets, `FLACCore` reads FLAC metadata without decoding audio, `CatalogCore` implements the catalog format, and `RebuildCore` holds the backup verification, recovery record, and progress journal. These four targets depend only on Foundation and are built and tested on Linux. `ConversionMac` and `LibraryMac` are the macOS integrations, which handle conversion through AudioToolbox, file dates, and Music automation. The command logic reaches Music only through a protocol, so it is tested with substitute libraries, and no external tool is required at run time.

The limits are stated plainly in the project. File processing is verified with synthetic inputs, and Music operations are tested with a substitute library. The forms of the requests that iLibrary sends to Music were measured on macOS 27.0.1 with Music 1.7, but the rebuilding stages have not been run against the Music application, and behavior on other versions is unknown. iLibrary removes store identifiers and reports the cloud statuses that Music exposes, but it does not prevent Apple Music cloud matching. Protected audio is out of scope, and iLibrary does not download audio. It moves and rewrites music files and changes a Music library, so begin with copies, keep independent backups of your library, and review every dry run. The [README](https://github.com/x96x64/ilibrary#limitations) lists the remaining limitations.

#### Installing iLibrary

iLibrary requires macOS 14 or later on Apple silicon. It is distributed through Homebrew, npm, and PyPI; install it through one channel only. The npm and PyPI names include my identifier because the plain name `ilibrary` belongs to other projects on those registries. After installation, `ilibrary --version` confirms the executable, and `ilibrary doctor` checks the environment and the Automation permission that Music commands need.

```bash
brew install x96x64/tap/ilibrary
npm install -g @x96_64/ilibrary
pipx install x96_64-ilibrary    # or: pip install x96_64-ilibrary
```

## Interests

My interests are AI agents and bots, command-line tools, free and open-source software, and audio and music files. They meet in the tools I build, since both iLyrics and iLibrary work with audio files and music libraries from the command line.

Away from the keyboard, I listen to a great deal of music, particularly recordings from the 1960s through the 1990s. One live recording in particular still lands like a powerful shock, however many times I have heard it before.

## Get in Touch

You can find my work here on GitHub and my background on [LinkedIn](https://www.linkedin.com/in/x96x64). For questions or problems with a project, please open an issue in the matching repository, where everyone can benefit from the answer: the [iLyrics issue tracker](https://github.com/x96x64/ilyrics/issues) for iLyrics, and the [iLibrary issue tracker](https://github.com/x96x64/ilibrary/issues) for iLibrary. A useful report names the version, the macOS version, and the exact command, and for iLibrary describes a synthetic reproduction rather than private files, as the [contribution guide](https://github.com/x96x64/ilibrary/blob/main/CONTRIBUTING.md) explains. Security problems with iLibrary are reported privately as its [security policy](https://github.com/x96x64/ilibrary/blob/main/SECURITY.md) describes.

## GitHub Activity

The activity list, the statistics cards, and the contribution snake below are generated from my public GitHub data by two scheduled workflows in this repository. One rewrites the activity list and refreshes the cards every six hours; the other redraws the snake every day and after each push to the main branch, and publishes it to a separate branch. These three parts are never edited by hand, so they show the public record as of their last successful refresh.

### Recent Activity

The list below shows my latest public activity on GitHub. A scheduled workflow rewrites it automatically every six hours, so it reflects my recent public events, most recent first, and it may lag behind what GitHub itself shows:

<!--START_SECTION:activity-->
1. 💪 Opened PR [#2](https://github.com/x96x64/x96x64/pull/2) in [x96x64/x96x64](https://github.com/x96x64/x96x64)
2. 💪 Opened PR [#12](https://github.com/x96x64/homebrew-tap/pull/12) in [x96x64/homebrew-tap](https://github.com/x96x64/homebrew-tap)
3. 🗣 Commented on [#49](https://github.com/x96x64/ilibrary/pull/49#issuecomment-6362008087) in [x96x64/ilibrary](https://github.com/x96x64/ilibrary)
4. 💪 Opened PR [#49](https://github.com/x96x64/ilibrary/pull/49) in [x96x64/ilibrary](https://github.com/x96x64/ilibrary)
5. 💪 Opened PR [#11](https://github.com/x96x64/homebrew-tap/pull/11) in [x96x64/homebrew-tap](https://github.com/x96x64/homebrew-tap)
<!--END_SECTION:activity-->

### GitHub Stats

These cards are generated from my public GitHub activity and refreshed automatically every six hours. The displayed figures may lag behind recent activity because the source services cache their results; if a refresh fails, the last successful cards remain available. The four cards show statistics, the languages most used in my public repositories, contribution streaks, and achievement trophies; each links to my profile.

<a href="https://github.com/x96x64">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/github/stats-dark.svg">
    <img alt="GitHub statistics card for x96x64: commits, pull requests, issues, and stars" src="assets/github/stats-light.svg">
  </picture>
</a>
<a href="https://github.com/x96x64">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/github/languages-dark.svg">
    <img alt="Card of the languages most used in the public repositories of x96x64" src="assets/github/languages-light.svg">
  </picture>
</a>

<a href="https://github.com/x96x64">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/github/streak-dark.svg">
    <img alt="Card of the current and longest GitHub contribution streaks of x96x64" src="assets/github/streak-light.svg">
  </picture>
</a>

<a href="https://github.com/x96x64">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/github/trophies-dark.svg">
    <img alt="Card of GitHub achievement trophies earned by x96x64" src="assets/github/trophies-light.svg">
  </picture>
</a>

### Contributions

Every day, a snake makes its way through my contribution graph and eats the squares in the order they were earned. The animation is generated from the public contribution calendar by a scheduled workflow and published to a separate branch. It is decorative; the graph on my GitHub profile page is the authoritative record of contributions.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/x96x64/x96x64/output/github-snake-dark.svg">
  <img alt="An animated snake eating the squares of the GitHub contribution graph of x96x64 in the order they were earned" src="https://raw.githubusercontent.com/x96x64/x96x64/output/github-snake.svg">
</picture>
