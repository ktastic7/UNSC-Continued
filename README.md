# United Nations Space Command - Continued

A continued version of AppleMarineXX's **United Nations Space Command** faction mod for [Starsector](https://fractalsoftworks.com/), based on the UNSC from the Halo universe.

**Original mod:** AppleMarineXX  
**Continued and maintained by:** Kemptastic  
**Starsector target:** 0.98a-RC8  
**Loader mod ID:** `UNSC`  
**Faction ID:** `unsc`

> **Repository status:** The current repository snapshot contains the **1.03 promotion candidate**.  
> The latest fully promoted, in-game-validated release remains **1.02p** until the exact 1.03 candidate completes its final release seal.
>
> For normal installation, use the packaged files on the **GitHub Releases** page rather than GitHub's automatically generated "Source code" ZIP.

## Overview

UNSC Continued maintains and modernizes the original Halo-themed UNSC faction mod while preserving its established gameplay identity.

The project currently includes:

- UNSC ships, fighters, weapons, hullmods, faction data, doctrine, variants, graphics, music, and sound assets.
- A hand-authored Epsilon Eridani system featuring Reach, Tribute, Circumstance, Beta Gabriel, Site 17, exploration content, derelicts, and other UNSC locations.
- Nexerelin integration, including UNSC colony-expedition naming support.
- Optional Industrial Evolution integration.
- Compatibility data for supported third-party mods where applicable.
- Version Checker-compatible update metadata beginning with the 1.03 line.
- A complete public source tree under `src/`.

## Requirements

### Required

- **Starsector 0.98a-RC8**
- **LazyLib**

### Optional integrations

The mod contains supported integration paths for:

- **Nexerelin**
- **Industrial Evolution**
- **Commissioned Crews**
- **Starpocalypse**

Optional integrations are intended to remain inert when their corresponding mod is absent unless otherwise documented.

Version Checker-compatible metadata is included beginning with 1.03. It does **not** add a new hard runtime dependency.

## Installation

1. Download the current playable runtime ZIP from the repository's **Releases** page.
2. Extract the contained folder into your Starsector `mods` directory.
3. Make sure only one copy of UNSC/UNSC Continued is enabled at a time.
4. Enable **LazyLib** and any optional supported mods you want to use.
5. Launch Starsector and enable:
   - `United Nations Space Command - Continued`

The technical loader ID remains `UNSC` for compatibility.

## Save Compatibility

The project underwent a major identifier namespace migration in the 1.02m line.

- Saves created with the modern `unsc_*` namespace should generally follow the compatibility notes for the specific release.
- Very old saves from before the namespace migration may contain obsolete serialized IDs.
- No broad runtime alias/automatic migration layer is shipped.
- Two private development saves were migrated manually during the namespace project, but that process is not a general-purpose public save converter.

For a major upgrade, keep a backup of your save and review the release notes before replacing an older version.

## Repository Layout

This repository intentionally contains the **full mod**, including runtime assets.

```text
UNSC-Continued/
├── data/                  Playable runtime data
├── graphics/              Runtime graphics
├── sounds/                Runtime sound/music
├── jars/UNSC.jar          Compiled runtime JAR
├── mod_info.json          Starsector mod metadata
├── startup.txt            Development/testing startup commands
├── unsc_continued.version Version Checker master/runtime declaration
├── src/                   Complete development source snapshot
│   ├── data/              Java source
│   ├── tools/             Development-only validation tools
│   └── version-checker/   Version Checker source/reference files
└── docs/                  Development and release workflow documentation
```

See [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) for the development workflow and [docs/RELEASE_PROCESS.md](docs/RELEASE_PROCESS.md) for the release process.

## Development Model

For the current transition period:

- **Google Drive remains the authoritative release/provenance archive.**
- **GitHub is the public source repository, working-development surface, and release mirror.**
- `main` is intended to represent the latest validated public release.
- `development` is intended for normal ongoing work.
- Feature/fix branches may be created from `development` when useful.

The repository was initially bootstrapped directly on `main` with the 1.03 candidate before the branch workflow was established. Future work should use the branch model above.

## Version Checker

Beginning with 1.03, the repository root contains:

```text
unsc_continued.version
```

The shipped registration file is:

```text
data/config/version/version_files.csv
```

The master version declaration currently resolves from the repository's default branch. For this reason, future-version declarations should normally remain on `development` until that version is actually ready to become the public release.

## Reporting Bugs

When reporting a problem, please include as much of the following as practical:

- UNSC Continued version.
- Starsector version.
- Whether Nexerelin and/or Industrial Evolution are enabled.
- A short description of what you were doing when the problem appeared.
- `starsector.log` when the issue may involve loading, scripts, world generation, markets, or integrations.
- A screenshot when the issue is primarily visual.

GitHub Issues are the preferred public place for reproducible bug reports once issue tracking is enabled for the project.

## Contributing

Contributions are welcome when they fit the project's scope and permissions.

Please read:

- [CREDITS.md](CREDITS.md)
- [PERMISSIONS.md](PERMISSIONS.md)
- [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md)

before submitting code or assets.

## Credits and Permissions

The original mod was created by **AppleMarineXX** and is continued by **Kemptastic** with the original author's permission.

See [CREDITS.md](CREDITS.md) and [PERMISSIONS.md](PERMISSIONS.md) for additional information.

This is a fan-made Starsector mod. Starsector, Halo, and related names, trademarks, artwork, audio, and other intellectual property remain the property of their respective rights holders. This project is not affiliated with or endorsed by Fractal Softworks, Microsoft, or the relevant Halo rights holders.
