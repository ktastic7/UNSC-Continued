# Development Guide

This document describes the working-development model for **United Nations Space Command - Continued**.

## 1. Current Authority Model

The project is in a transition period.

For now:

- **Google Drive remains the authoritative release and provenance archive.**
- **GitHub is the public source repository, day-to-day development surface, and release mirror.**
- Local development happens from a Git clone on the maintainer's PC.
- A GitHub release is not authoritative merely because it exists; the matching build must first pass the project's validation/promotion process.

This arrangement is intentional while the maintainer gains experience with Git/GitHub and while the build process is made more reproducible.

## 2. Branch Model

### `main`

Target policy:

- Represents the latest validated public release.
- Contains the source/assets corresponding to that release.
- Contains the public Version Checker master declaration.
- Should not be used for normal experimental editing.

Bootstrap note: the repository was initially populated directly on `main` with 1.03 before the branch workflow was established. The exact 1.03 build subsequently passed its final in-game seal and was promoted unchanged in the authoritative Google Drive release archive. `main` therefore serves as the clean validated 1.03 baseline from which the normal branch workflow begins.

After the one-time 1.03 repository-status documentation cleanup is committed, future normal development should not be performed directly on `main`.

### `development`

Use for normal ongoing work toward the next release.

Examples:

- source changes;
- data/config edits;
- documentation work;
- asset changes;
- build-script development;
- pre-release Version Checker changes.

The public Version Checker master URL resolves through the repository default branch, so a future version declaration should normally stay on `development` until that version is actually ready to become public.

### Feature/fix branches

For larger or riskier work, branch from `development`.

Examples:

```text
feature/seeded-worldgen
feature/build-script
fix/colony-naming
fix/market-generation
```

Merge the completed work back into `development` after review/testing.

## 3. Repository Layout

The repository root intentionally contains the full playable mod.

```text
data/                   Runtime data/config/content
graphics/               Runtime graphics
sounds/                 Runtime music/sound
jars/UNSC.jar           Compiled runtime JAR
mod_info.json           Starsector mod metadata
startup.txt             Development/testing startup commands
unsc_continued.version  Runtime + remote Version Checker declaration

src/
  data/                 Complete Java source snapshot
  tools/                Development-only validators
  version-checker/      Version Checker reference/source files
  CHANGELOG 1.xx.txt    Release-source changelog copy
  README 1.xx SOURCE.txt

docs/                   Public development/release process documentation
```

The repository contains binary assets directly. The current project is small enough that Git LFS is not required. Revisit that decision only if large binary history becomes a concrete repository-size problem.

## 4. Runtime Identity Invariants

Unless a separately approved migration changes them:

- loader mod ID: `UNSC`
- faction ID: `unsc`
- UNSC-owned content namespace: lowercase `unsc_*`
- only one enabled UNSC copy should be active at a time

Display names, folder names, and public version labels may change without changing the loader ID.

## 5. Target Environment

Current target:

- Starsector `0.98a-RC8`

Current build/reference dependencies include:

- Starsector API/runtime libraries
- LazyLib
- Nexerelin
- Industrial Evolution

LazyLib is currently a declared hard dependency.

Nexerelin and Industrial Evolution are optional at runtime, but the Java source contains typed integration code and production compilation uses the exact real dependency references required by those classes.

Do not replace production dependencies with guessed stubs.

## 6. Production-Code Safety Rules

Production changes should preserve the established project safety model:

- compile against real target APIs/dependencies;
- do not guess method signatures, constants, IDs, or static-final values;
- do not add Java reflection to runtime code by default;
- do not add direct Java filesystem/path access to runtime code by default;
- prefer Starsector APIs and documented partner-mod APIs;
- isolate optional partner-mod references behind proven gates;
- preserve exact IDs and serialization-sensitive behavior unless a migration is explicitly planned.

Historical releases 1.02i and 1.02j demonstrated why guessed production stubs are unsafe: incorrect static-final values were compiled into runtime bytecode and broke fresh world generation.

## 7. Java / JAR Workflow

The runtime uses:

```text
jars/UNSC.jar
```

The authoritative Java source snapshot lives under:

```text
src/data/
```

Current production builds are expected to:

1. start from the intended Git commit/source state;
2. compile the complete Java source set against the exact real references;
3. verify compiler/class-file compatibility;
4. replace `jars/UNSC.jar` with the newly built JAR;
5. compare JAR entries and changed classes against the prior validated release;
6. run the applicable static/preflight checks;
7. package a clean runtime candidate;
8. test the exact packaged candidate.

Do not treat "it compiled" as equivalent to "it is validated."

## 8. Development-Only Tools

The ST-12 authored-market validator is stored under:

```text
src/tools/
```

It is development-only and should not be copied into the playable runtime ZIP unless a future release process deliberately changes that rule.

Current intended checks include exact authored market condition/submarket/industry validation and helper-call contract checks.

## 9. Version Checker

Runtime registration:

```text
unsc_continued.version
data/config/version/version_files.csv
```

Development reference copies:

```text
src/version-checker/
```

Current master URL:

```text
https://raw.githubusercontent.com/ktastic7/UNSC-Continued/HEAD/unsc_continued.version
```

Important rules:

- keep the local/runtime declaration and repository master declaration consistent for the release being built;
- do not advertise a future final version from `main` before that version is ready to be public;
- keep future declarations on `development` until release promotion;
- Version Checker support must remain passive unless a future scope explicitly changes its dependency/runtime architecture;
- `directDownloadURL` and `changelogURL` should remain deferred until release-link handling is deliberately designed and verified.

The repository default branch should remain `main` while this `HEAD`-based master URL is used, so the public declaration continues to describe the current validated public release rather than an in-progress development version.

## 10. Commit Guidelines

A commit should represent a meaningful checkpoint.

Good examples:

```text
Add 1.03 Version Checker registration
Document repository development workflow
Fix Reach market industry configuration
Update Halberd sprite alignment
Prepare 1.04 promotion candidate
```

Avoid vague messages such as:

```text
stuff
changes
update
fix
```

Before committing:

1. review every changed file in GitHub Desktop;
2. make sure generated/temp files are not included;
3. confirm no local Starsector/dependency binaries were accidentally added;
4. verify the commit contains one understandable unit of work where practical.

## 11. Asset Changes

Graphics and audio are tracked directly in normal Git.

When replacing a binary asset:

- verify the intended file/path;
- preserve dimensions/centering/format where required by Starsector;
- avoid repeated unnecessary binary rewrites;
- inspect the result in game when the change is visual or audio-sensitive.

The intentionally dormant file:

```text
data/weapons/unsc_harpoon_cell.wpn~
```

must remain tracked. Do not add a blanket `*~` ignore rule.

## 12. Local Files That Must Not Be Committed

Do not commit:

- local Starsector installation paths;
- local dependency copies used only for compilation;
- user saves;
- logs/crash dumps;
- generated build directories;
- release ZIPs;
- machine-specific IDE metadata;
- private permission correspondence;
- internal Google Drive doctrine/governance files unless a future public-documentation decision explicitly includes them.

## 13. Validation Expectations

Select validation based on what changed.

Typical layers include:

- JSON/CSV/config syntax;
- exact-reference Java compilation;
- JAR integrity and entry comparison;
- ID/constant/descriptor checks;
- runtime safety scan;
- optional-dependency enabled/absent paths when relevant;
- main-menu/startup smoke test;
- fresh game/Epsilon Eridani generation when worldgen is affected;
- campaign/combat/refit checks when relevant;
- full `starsector.log` review;
- exact final-artifact identity/hash confirmation.

The final release status belongs to the exact artifact that was tested.

## 14. Pull Requests

Once `development` exists, use pull requests to move validated work into `main`.

A pull request is the review point where you can see all changes between the branches before making them part of the stable branch.

For a release merge:

- base: `main`
- compare/head: `development`

Do not merge a release candidate merely because it builds. Merge only after the intended release gate has been satisfied.
