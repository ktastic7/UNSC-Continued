# Development and Contribution Notes

This document is for people who want to inspect the source, experiment locally, or contribute changes to **United Nations Space Command - Continued**.

It intentionally covers only public source/contributor information. Internal project-management, validation, and release-governance documentation is maintained separately by the project.

## Repository Layout

The repository contains the full playable mod together with its Java source and development utilities.

```text
data/                   Runtime data/config/content
graphics/               Runtime graphics
sounds/                 Runtime music/sound
jars/UNSC.jar           Compiled runtime JAR
mod_info.json           Starsector mod metadata
unsc_continued.version  Version Checker declaration

src/
  data/                 Java source
  tools/                Development utilities
  version-checker/      Version Checker reference/source files
```

## Target Environment

Current target:

- Starsector `0.98a-RC8`

Current source/build dependencies include:

- Starsector API/runtime libraries
- LazyLib
- Nexerelin
- Industrial Evolution

LazyLib is currently a declared required dependency.

Nexerelin and Industrial Evolution are optional at runtime, but the source contains integration code for them. Anyone rebuilding the Java source should use the matching real APIs/dependencies rather than guessed replacement stubs.

## Runtime Identity

Unless a future release explicitly changes them:

- loader mod ID: `UNSC`
- faction ID: `unsc`
- UNSC-owned subordinate content IDs use the lowercase `unsc_*` namespace

These IDs may affect compatibility and should not be renamed casually.

## Java Source

The public Java source is stored under:

```text
src/data/
```

The playable mod loads:

```text
jars/UNSC.jar
```

The repository currently includes the compiled runtime JAR so the checked-out release tree remains close to the playable mod.

A fully automated public build script is not yet provided. If you modify Java source, rebuild `UNSC.jar` against the appropriate Starsector and dependency libraries before testing the change in game.

## Development Utilities

Development-only utilities are stored under:

```text
src/tools/
```

These tools are intended to help inspect or validate project data and are not required for normal gameplay.

## Version Checker Files

Version Checker-compatible metadata is stored at:

```text
unsc_continued.version
data/config/version/version_files.csv
```

Development reference copies may also be present under:

```text
src/version-checker/
```

When changing version metadata, keep the shipped registration and declaration consistent.

## Asset Changes

Graphics and audio are tracked directly in Git.

When changing an asset:

- preserve the expected file format;
- preserve dimensions/centering where the game depends on them;
- avoid unnecessary recompression or format conversion;
- verify visual/audio changes in game.

The file:

```text
data/weapons/unsc_harpoon_cell.wpn~
```

is intentionally retained as a dormant asset. Do not remove it merely because its filename ends in `~`.

## Coding and Compatibility Notes

When contributing code:

- use the actual Starsector and partner-mod APIs used by the project;
- avoid guessing API constants, method signatures, or registry IDs;
- avoid adding runtime reflection or direct filesystem access unless there is a clear, reviewed need;
- keep optional-mod integrations isolated so the base mod remains loadable when those optional mods are absent;
- avoid unrelated cleanup in the same change when possible;
- preserve compatibility-sensitive IDs unless a deliberate migration is part of the change.

## Testing Contributions

At minimum, test the part of the mod you changed.

Depending on the change, useful checks may include:

- game startup;
- new campaign creation;
- Epsilon Eridani generation;
- relevant markets or industries;
- combat/refit behavior;
- optional integration enabled/disabled behavior;
- `starsector.log` review for new errors.

A successful compile alone does not guarantee correct in-game behavior.

## Submitting Changes

When proposing a contribution:

- explain what the change does and why;
- keep the scope focused;
- mention any save-compatibility implications;
- mention which optional mods are affected;
- include screenshots for visual changes when useful;
- include relevant log excerpts or reproduction steps for bug fixes.

Only submit code, art, audio, or other material that you have the right to contribute.

See [../PERMISSIONS.md](../PERMISSIONS.md) and [../CREDITS.md](../CREDITS.md) before submitting third-party material.
