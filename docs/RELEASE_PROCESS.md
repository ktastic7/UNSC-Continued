# Releases and Downloads

This page explains the public release files for **United Nations Space Command - Continued**.

It does not describe the project's internal development, validation, or release-management process.

## Where to Download

Use the repository's **GitHub Releases** page for normal downloads.

A release normally provides an attached runtime package named like:

```text
United Nations Space Command - Continued (VERSION).zip
```

This is the package intended for normal Starsector installation.

A release may also provide:

```text
United Nations Space Command - Continued (VERSION) - Development Source.zip
```

for people who want the corresponding Java source/development snapshot.

## GitHub "Source code" Archives

GitHub automatically adds:

```text
Source code (zip)
Source code (tar.gz)
```

to tagged releases.

These are automatic snapshots of the Git repository. They are **not** the normal playable Starsector package.

For gameplay, use the attached runtime ZIP whose filename begins:

```text
United Nations Space Command - Continued
```

## Installation

1. Download the attached runtime ZIP from the desired release.
2. Extract its contained mod folder into the Starsector `mods` directory.
3. Make sure only one copy of UNSC / UNSC Continued is enabled.
4. Enable LazyLib and any optional supported integrations you use.
5. Enable **United Nations Space Command - Continued** in the Starsector launcher.

## Release Versions

Git tags use a `v` prefix, for example:

```text
v1.03
```

The in-game mod version omits that prefix:

```text
1.03
```

Test or pre-release builds, when publicly distributed, may use an additional suffix and may be marked as a GitHub pre-release.

## Checksums

Release notes may include SHA-256 checksums for downloadable artifacts.

A checksum can be used to confirm that a downloaded file matches the published release file.

For Windows PowerShell, one way to calculate a SHA-256 hash is:

```powershell
Get-FileHash "path\to\file.zip" -Algorithm SHA256
```

Compare the resulting hash with the value shown in the release notes.

## Version Checker

Beginning with 1.03, the mod includes Version Checker-compatible metadata.

The public declaration is:

```text
unsc_continued.version
```

and is registered through:

```text
data/config/version/version_files.csv
```

This allows compatible Version Checker implementations to identify the current public release.

## Historical Releases

Older release packages may reflect earlier compatibility assumptions or known issues.

Where the changelog marks a version as **Known Broken**, do not use that version as a stable gameplay release.

See [../CHANGELOG.md](../CHANGELOG.md) for the public release history.
