# United Nations Space Command - Continued

A continued version of AppleMarineXX's **United Nations Space Command** faction mod for [Starsector](https://fractalsoftworks.com/), based on the UNSC from the Halo universe.

**Original mod:** AppleMarineXX  
**Continued and maintained by:** Kemptastic  
**Current release:** 1.03  
**Starsector target:** 0.98a-RC8  
**Loader mod ID:** `UNSC`  
**Faction ID:** `unsc`

> For normal installation, download the packaged runtime ZIP from the **GitHub Releases** page.  
> GitHub's automatically generated "Source code" archives are not the playable mod package.

## Overview

UNSC Continued maintains and modernizes the original Halo-themed UNSC faction mod while preserving its established gameplay identity.

The project includes:

- UNSC ships, fighters, weapons, hullmods, faction data, doctrine, variants, graphics, music, and sound assets.
- A hand-authored Epsilon Eridani system featuring Reach, Tribute, Circumstance, Beta Gabriel, Site 17, exploration content, derelicts, and other UNSC locations.
- Nexerelin integration, including UNSC colony-expedition naming support.
- Optional Industrial Evolution integration.
- Compatibility data for supported third-party mods where applicable.
- Version Checker-compatible update metadata beginning with 1.03.
- Public Java source and development utilities under `src/`.

## Requirements

### Required

- **Starsector 0.98a-RC8**
- **LazyLib**

### Optional integrations

Supported integration paths include:

- **Nexerelin**
- **Industrial Evolution**
- **Commissioned Crews**
- **Starpocalypse**

Optional integrations are intended to remain inactive when their corresponding mod is absent unless otherwise documented.

Version Checker-compatible metadata is included beginning with 1.03 and does **not** add a new hard runtime dependency.

## Installation

1. Open the repository's **Releases** page.
2. Download the attached runtime ZIP named like:
   `United Nations Space Command - Continued (VERSION).zip`
3. Extract the contained mod folder into your Starsector `mods` directory.
4. Make sure only one copy of UNSC / UNSC Continued is enabled at a time.
5. Enable **LazyLib** and any optional supported mods you use.
6. Enable **United Nations Space Command - Continued** in the Starsector launcher.

The technical loader ID remains `UNSC` for compatibility.

## Save Compatibility

The project completed a major identifier namespace migration in the 1.02m line.

- Releases using the modern namespace use canonical `unsc_*` content IDs.
- Very old saves from before that migration may contain obsolete serialized IDs and may not load correctly with current releases.
- The mod does not ship a broad automatic migration layer for those older saves.

Back up important saves before upgrading across major historical changes and review the release notes for the version you are installing.

## Repository Contents

This repository contains the full mod together with its public source.

```text
UNSC-Continued/
├── data/                  Runtime data/config/content
├── graphics/              Runtime graphics
├── sounds/                Runtime sound/music
├── jars/UNSC.jar          Compiled runtime JAR
├── mod_info.json          Starsector mod metadata
├── unsc_continued.version Version Checker declaration
├── src/                   Java source and development utilities
└── docs/                  Public contributor/download documentation
```

For source-oriented information, see [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md).

For release/download information, see [docs/RELEASE_PROCESS.md](docs/RELEASE_PROCESS.md).

## Version Checker

Beginning with 1.03, the repository includes:

```text
unsc_continued.version
```

and the shipped registration file:

```text
data/config/version/version_files.csv
```

These files allow compatible Version Checker implementations to identify the current public release.

## Reporting Bugs

When reporting a reproducible problem, please include as much of the following as practical:

- UNSC Continued version.
- Starsector version.
- Whether Nexerelin and/or Industrial Evolution are enabled.
- A short description of what you were doing when the problem appeared.
- `starsector.log` when the issue may involve loading, scripts, world generation, markets, or integrations.
- A screenshot when the issue is primarily visual.

GitHub Issues are the preferred public place for reproducible bug reports when issue tracking is enabled for the project.

## Contributing

Contributions are welcome when they fit the project's scope and permissions.

Before submitting code or assets, please read:

- [CREDITS.md](CREDITS.md)
- [PERMISSIONS.md](PERMISSIONS.md)
- [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md)

## Credits and Permissions

The original mod was created by **AppleMarineXX** and is continued by **Kemptastic** with the original author's permission.

See [CREDITS.md](CREDITS.md) and [PERMISSIONS.md](PERMISSIONS.md) for additional information.

This is a fan-made Starsector mod. Starsector, Halo, and related names, trademarks, artwork, audio, and other intellectual property remain the property of their respective rights holders. This project is not affiliated with or endorsed by Fractal Softworks, Microsoft, or the relevant Halo rights holders.
