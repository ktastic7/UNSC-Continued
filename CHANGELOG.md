# Changelog

This is the public-facing changelog for **United Nations Space Command - Continued**.

Internal build audits, validation records, migration records, and repository-governance documents are maintained separately from this public summary.

## 1.03 — In-Game Validated Release

### Version Checker support

- Added passive Version Checker-compatible metadata.
- Added root `unsc_continued.version`.
- Added `data/config/version/version_files.csv` registration.
- Master declaration points to the public GitHub repository.
- Final 1.03 declaration uses:
  - major `1`
  - minor `3`
  - patch `0`
- Version Checker support remains data-only/passive and does not add a new hard Java/runtime dependency.
- `directDownloadURL` and `changelogURL` remain intentionally deferred until public-release links are deliberately configured.

### Runtime behavior

- No gameplay or content changes from 1.02p.
- Loader ID remains `UNSC`.
- Faction ID remains `unsc`.
- Canonical `unsc_*` content IDs remain unchanged.
- World generation, markets, ships, weapons, combat behavior, integrations, and save-migration policy remain unchanged.

### Validation and promotion

- The exact final 1.03 promotion candidate passed the in-game release check.
- The exact tested runtime and Development Source bytes were promoted unchanged into the authoritative Google Drive release archive.
- Drive read-back SHA-256 values matched the sealed candidate hashes.
- Runtime SHA-256: `a32990a1d735b5831d125c467a3366866b14865e7d15d74d73f656b5b9799f67`
- Development Source SHA-256: `41d664a2719f79d8832f2054b62592d6edd29719be6bfaa193b6a3ae74bc1629`
- `UNSC.jar` SHA-256: `f1d68c9309534137ff8206229a9e2e2dc41a35ee12ca3cbf9c8de45cdafdb6bb`

**Status:** in-game validated / current authoritative release.

---

## 1.02p — First "Continued" Public Identity

- Renamed the public project to **United Nations Space Command - Continued**.
- Updated the mod-folder/display identity to the Continued naming format.
- Updated author metadata to:
  - `Original by AppleMarineXX, Continued by Kemptastic`
- Updated the public description to identify the project as a continuation of AppleMarineXX's original mod.
- Preserved technical compatibility identity:
  - loader ID `UNSC`
  - faction ID `unsc`
  - canonical `unsc_*` content namespace
- No gameplay/content changes from 1.02o.

**Status:** in-game validated / superseded by 1.03.

---

## 1.02o

- Released the previously validated ST-16 Epsilon Eridani hyperspace-clearing improvement.
- Released the previously validated ST-12 `UNSC_AddMarketplace` hardening.
- Replaced boxed helper booleans with primitive booleans while preserving explicit market routing.
- Added development-only exact-registry validation for authored market IDs.
- Preserved the validated Epsilon Eridani system layout, market layout, wreck design, integrations, and content IDs.

**Status:** in-game validated / superseded by 1.02p.

---

## 1.02n

### Core-world protection and defenses

- Added Vanilla story-critical protection to Reach, Tribute, and Circumstance using reason `unsc_core_world`.
- Preserved Nexerelin's normal story-critical invasion behavior rather than applying a hard uninvadable flag.

### Reach

- Patrol HQ upgraded to Military Base.
- Alpha Cores applied to intended military defenses.
- Orbital Works and Corrupted Nanoforge retained.
- Starting Refining removed.

### Tribute

- High Command retained.
- Orbital Works added.
- Light Industry removed.
- Midline Star Fortress and intended Alpha Core defenses retained.

### Circumstance

- Patrol HQ upgraded to High Command.
- Ground Defenses upgraded to Heavy Batteries.
- Midline Star Fortress added.
- Refining added.
- Intended military Alpha Cores added.

These starting-market changes apply to fresh authored world generation rather than retrofitting existing serialized markets.

---

## 1.02m

### Identifier namespace standardization

- Standardized 82 approved UNSC-owned IDs to the canonical lowercase `unsc_*` namespace.
- Preserved loader mod ID `UNSC` and faction ID `unsc`.
- Renamed the custom Goalkeeper projectile to `unsc_pd_ballistic_shot`.
- Made six authored UNSC market IDs explicit.
- Updated Commissioned Crews integration to the canonical UNSC hullmod ID.
- Removed copied ScalarTech special-forces-name data and stale ScalarTech hooks.
- Preserved the authored 20-wreck design:
  - 6 normal/free recoverables
  - 14 Story Point recovery candidates
- No runtime alias/automatic old-save migration layer was added.

---

## 1.02l

- Added Industrial Evolution embassy whitelist support.
- Added all eight principal UNSC hulls to Industrial Evolution reverse-engineering and Derelict Industries printing whitelists.
- Rebuilt the production JAR against real target/dependency references.
- Finalized dormant Harpoon Battery handling.
- Removed stale Nex data.
- Removed dead loose duplicate Vanilla hullmod source copies.
- Cleaned the runtime distribution and retained current player-facing material.

---

## 1.02k

- Corrected the fresh-world-generation crash inherited from 1.02i/1.02j.
- Restored the proven `UNSCStar` runtime path.
- Corrected the latent decivilization-memory-key issue.
- Retained safe maintenance improvements from the earlier attempts.

---

## 1.02j — Known Broken

- Attempted a narrow wreck-generation hotfix.
- Did not fix the actual world-generation crash because the unsafe production-stub issue remained.

Do not use as a stable release.

---

## 1.02i — Known Broken

- Contained several maintenance/robustness changes.
- Production compilation used unsafe guessed Starsector stubs.
- Incorrect `static final` values were inlined into runtime bytecode and broke fresh world generation.

Do not use as a stable release.

---

## 1.02h

- Corrected a debris-field world-generation failure involving `baseSalvageXP`.
- Returned to the running game's default salvage-XP behavior.
- Established a known-good historical baseline.

---

## 1.02g

- Expanded Epsilon Eridani exploration content.
- Added five persistent battle-debris fields.
- Added weapons/equipment caches.
- Added abandoned exploration locations.
- Added exactly 20 authored UNSC wrecks.
- Expanded optional Industrial Evolution content.

---

## 1.02f

- Increased Epsilon Eridani spacing.
- Refined moon sizes, conditions, and orbits.
- Added fixed phase relationships for selected authored bodies to improve system-map readability.

---

## 1.02d

- Applied Vanilla-pattern world-generation corrections.
- Improved condition-market initialization for uncolonized bodies.
- Adjusted belt/ring behavior.

---

## 1.02c

- Major Epsilon Eridani reconstruction.
- Added/reworked Epsilon Eridani I, Reach, Tribute, Circumstance, Beta Gabriel, Tantalus, Site 17, belts, and related content.

---

## 1.02b

- Added the Industrial Evolution optional-dependency gate around Reach Railgun Artillery.
- Preserved operation when Industrial Evolution is absent.

---

## Earlier Releases

Earlier modernization work included hull-ID cleanup, UTF-8/spelling fixes, Nex colony-name support, Epsilon Eridani development, optional integration work, profiling, and save-compatibility maintenance.

For exact historical behavior, consult the preserved release artifacts rather than assuming every intermediate version is suitable for current use.
