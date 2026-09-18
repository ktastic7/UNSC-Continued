# Release Process

This document describes the current release workflow for **United Nations Space Command - Continued**.

## 1. Authority During the GitHub Transition

For now:

- Google Drive is the authoritative release/provenance archive.
- GitHub is the public source/development repository and release mirror.
- GitHub Releases should mirror the exact already-validated release bytes.
- A GitHub tag/release does not replace the Drive promotion/validation record until the project explicitly changes its authority model.

## 2. Branch Roles

### `main`

Represents the latest validated public release.

### `development`

Contains work intended for the next release.

### feature/fix branches

Optional branches for isolated work, merged back into `development` after review.

## 3. Choose the Release Scope

Before building:

1. decide the version number;
2. list exactly what is included;
3. list important exclusions;
4. identify whether save compatibility, IDs, world generation, optional dependencies, or binary assets are affected.

Do not silently bundle unrelated cleanup.

## 4. Prepare Release Metadata on `development`

Update applicable files for the candidate:

- `mod_info.json`
- `UNSCColonyNamer.PROFILE_MOD_VERSION`
- `unsc_continued.version`
- release-specific README/changelog source material
- public `CHANGELOG.md` where appropriate

Keep:

- loader ID `UNSC`
- faction ID `unsc`
- canonical `unsc_*` content IDs

unchanged unless the release explicitly includes a migration.

The colony-namer architecture version should change only when the naming architecture itself changes.

## 5. Build From a Known Commit

Before compiling:

1. commit the intended source/data state on `development`;
2. note the commit SHA;
3. make sure the working tree is clean or that any uncommitted change is understood;
4. compile from that known state.

This makes it possible to answer:

> "Exactly which source state produced this candidate?"

## 6. Compile Against Real References

Production compilation must use the exact real target environment required by the changed code.

Current target/reference family:

- Starsector 0.98a-RC8 API/runtime libraries
- LazyLib
- Nexerelin
- Industrial Evolution

Never use guessed production stubs as a substitute for unavailable real references.

If required production references are missing or ambiguous, stop the build instead of guessing.

## 7. Run Static / Preflight Validation

Run the checks applicable to the release.

Typical checks:

- Java compile success;
- class-file/JAR compatibility;
- JAR entry comparison against prior validated release;
- authored-market validator under `src/tools/`;
- JSON/CSV syntax;
- content-ID checks;
- runtime-source reflection scan;
- runtime-source direct-filesystem/path scan;
- optional-dependency isolation;
- archive integrity;
- bounded diff review.

Unexpected changes should be explained before proceeding.

## 8. Assemble the Clean Candidate

Package the playable mod with its final candidate identity.

Do not include development-only material that is not part of the runtime distribution.

The full Git repository may contain source/tools/docs that are intentionally absent from the playable ZIP.

Calculate and record SHA-256 for at least:

- runtime ZIP;
- Development Source ZIP;
- `jars/UNSC.jar`.

The runtime candidate must be the exact artifact used for the final in-game seal.

## 9. Store the Candidate in Google Drive Working

While Drive remains authoritative:

- store the candidate runtime/source in the project `Working/` area;
- record exact filenames and SHA-256 values;
- preserve the prior authoritative release unchanged.

A candidate is not yet the authoritative release.

## 10. Perform Exact-Artifact In-Game Validation

Test the exact packaged candidate without editing or repacking it afterward.

Minimum validation depends on scope, but normally includes:

- launcher/mod identity;
- main menu/startup;
- representative save or fresh campaign;
- Epsilon Eridani generation when relevant;
- optional integrations when relevant;
- profiler version identity;
- full log review.

For a final release seal, preserve the resulting log or other required evidence.

If the candidate bytes change after the test, repeat the applicable final-artifact validation.

## 11. Promote the Exact Bytes in Google Drive

After the final seal passes:

1. copy the exact tested runtime/source bytes into the immutable release archive;
2. rename only through a copy operation that preserves the bytes;
3. read back the stored files;
4. verify SHA-256 equality with the tested candidates;
5. update authoritative project/release documentation.

At this point the release becomes authoritative under the current Drive-first model.

## 12. Merge the Validated Source Into `main`

After Drive promotion:

1. make sure `development` contains the source/assets corresponding to the promoted release;
2. open a pull request:
   - base: `main`
   - compare: `development`
3. review the complete diff;
4. merge the pull request;
5. pull/fetch the updated `main` locally.

Normal future development resumes on `development`, not directly on `main`.

For the one-time 1.03 repository bootstrap, the validated 1.03 source/assets were already present directly on `main` before `development` existed. That bootstrap is accepted as the initial stable baseline rather than being rewritten solely to simulate a historical pull request.

## 13. Create the Git Tag and GitHub Release

Create a tag using the `v` prefix.

Example:

```text
v1.03
```

Release title:

```text
United Nations Space Command - Continued (1.03)
```

The tag should target the `main` commit representing that release.

Create the GitHub Release and attach the exact authoritative files from Drive.

Typical assets:

```text
United Nations Space Command - Continued (VERSION).zip
United Nations Space Command - Continued (VERSION) - Development Source.zip
```

A validation summary may also be attached when useful.

Do **not** commit these release ZIPs into normal Git history.

## 14. Verify Release Assets

After upload:

1. confirm the filenames/assets are correct;
2. download or otherwise verify the uploaded assets;
3. compare SHA-256 against the authoritative Drive records;
4. do not replace an asset with rebuilt/repacked bytes while keeping the same release identity.

GitHub automatically provides "Source code (zip)" and "Source code (tar.gz)" links for the tagged repository tree.

Those automatically generated archives are **not** the playable Starsector release package.

Make this distinction clear in release notes.

## 15. Version Checker After Publication

Current Version Checker master declaration:

```text
https://raw.githubusercontent.com/ktastic7/UNSC-Continued/HEAD/unsc_continued.version
```

Because `HEAD` resolves through the repository default branch, the public master file should match the current public release.

Keep `main` as the repository default branch while this URL is used. Work-in-progress version declarations should remain on `development` until release promotion.

For 1.03, `directDownloadURL` and `changelogURL` are intentionally deferred.

Do not add those fields casually after release if doing so would blur the distinction between:

- the exact runtime file that was validated;
- the repository copy; and
- a remote-only master declaration.

Design and document that separation first if automatic-download URLs are added later.

## 16. Public Release Notes Template

Use a concise structure:

```text
# United Nations Space Command - Continued VERSION

## Highlights
- ...

## Requirements
- Starsector ...
- LazyLib ...

## Compatibility
- Nexerelin ...
- Industrial Evolution ...

## Installation
1. ...
2. ...

## Downloads
Use the attached runtime ZIP for normal installation.
GitHub's automatic "Source code" archives are not the playable mod package.

## SHA-256
Runtime:
...

Development Source:
...

## Credits
Original by AppleMarineXX
Continued by Kemptastic
```

## 17. After Release

After the GitHub release is verified:

1. return to `development`;
2. make sure it contains the new `main` state;
3. begin the next work only after the next scope is selected;
4. do not preemptively advertise the next final version from `main`.

## 18. 1.03 Bootstrap — Completed Drive Promotion

The repository was bootstrapped before the branch workflow was established, so the exact 1.03 source/assets were placed directly on `main`.

The final 1.03 artifact passed its exact-artifact in-game seal and was promoted unchanged in the authoritative Google Drive release archive.

Authoritative 1.03 identity:

- runtime:
  `United Nations Space Command - Continued (1.03).zip`
- runtime Drive ID:
  `1lromk6OmHUfu6_8CuHS2dHcy3QA9SYnY`
- runtime SHA-256:
  `a32990a1d735b5831d125c467a3366866b14865e7d15d74d73f656b5b9799f67`
- Development Source:
  `United Nations Space Command - Continued (1.03) - Development Source.zip`
- Development Source Drive ID:
  `1rTZkZh-7vnrfd8qJXbH0JfYUcWOkHsDl`
- Development Source SHA-256:
  `41d664a2719f79d8832f2054b62592d6edd29719be6bfaa193b6a3ae74bc1629`
- `UNSC.jar` SHA-256:
  `f1d68c9309534137ff8206229a9e2e2dc41a35ee12ca3cbf9c8de45cdafdb6bb`

The exact tested runtime/source candidate bytes were copied into the immutable Drive release archive without rebuilding, editing, or repacking, and raw Drive read-back hashes matched the sealed candidate hashes.

The current GitHub `main` tree contains the corresponding 1.03 mod metadata, Version Checker declaration/registration, runtime JAR, Java source, and assets.

**1.03 status: IN-GAME VALIDATED / AUTHORITATIVE.**

The remaining GitHub bootstrap sequence is:

1. commit the final 1.03 repository-status documentation to `main`;
2. create `development` from that clean 1.03 `main` baseline;
3. keep `main` as the default branch;
4. tag the final `main` commit as `v1.03`;
5. create the GitHub Release using the exact authoritative Drive runtime and Development Source ZIPs;
6. verify the uploaded release assets against the authoritative SHA-256 values;
7. return normal ongoing work to `development`.
