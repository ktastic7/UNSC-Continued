# Changelog

Public release history for **United Nations Space Command - Continued**.

## 1.03

### Version Checker support

- Added passive Version Checker-compatible metadata.
- Added root `unsc_continued.version`.
- Added `data/config/version/version_files.csv` registration.
- Public version metadata is hosted through this GitHub repository.
- Version Checker support remains optional and does not add a new hard runtime dependency.

### Runtime behavior

1.03 contains no gameplay or content changes from 1.02p.

The following remain unchanged:

- loader ID `UNSC`;
- faction ID `unsc`;
- canonical `unsc_*` content IDs;
- world generation;
- markets and industries;
- ships, fighters, and weapons;
- combat behavior;
- supported integrations;
- save-migration policy.

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

---

## 1.02o

- Added the validated two-stage Epsilon Eridani hyperspace-clearing improvement.
- Hardened `UNSC_AddMarketplace` boolean handling while preserving explicit market routing.
- Added development-time validation for authored market IDs.
- Preserved the existing Epsilon Eridani layout, market layout, wreck design, integrations, and content IDs.

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

- Standardized 82 UNSC-owned IDs to the canonical lowercase `unsc_*` namespace.
- Preserved loader mod ID `UNSC` and faction ID `unsc`.
- Renamed the custom Goalkeeper projectile to `unsc_pd_ballistic_shot`.
- Made six authored UNSC market IDs explicit.
- Updated Commissioned Crews integration to the canonical UNSC hullmod ID.
- Removed copied ScalarTech special-forces-name data and stale ScalarTech hooks.
- Preserved the authored 20-wreck design:
  - 6 normal/free recoverables
  - 14 Story Point recovery candidates
- No broad automatic old-save migration layer was added.

---

## 1.02l

- Added Industrial Evolution embassy whitelist support.
- Added all eight principal UNSC hulls to Industrial Evolution reverse-engineering and Derelict Industries printing whitelists.
- Rebuilt the production JAR against the intended game/mod dependencies.
- Finalized dormant Harpoon Battery handling.
- Removed stale Nex data.
- Removed dead loose duplicate Vanilla hullmod source copies.
- Cleaned the runtime distribution.

---

## 1.02k

- Corrected the fresh-world-generation crash inherited from 1.02i/1.02j.
- Restored the proven `UNSCStar` runtime path.
- Corrected the latent decivilization-memory-key issue.
- Retained safe maintenance improvements from the earlier attempts.

---

## 1.02j — Known Broken

- Attempted a narrow wreck-generation hotfix.
- Did not fix the inherited world-generation crash.

Do not use as a stable release.

---

## 1.02i — Known Broken

- Included maintenance/robustness changes.
- A build-reference error caused invalid compiled runtime constants and broke fresh world generation.

Do not use as a stable release.

---

## 1.02h

- Corrected a debris-field world-generation failure involving `baseSalvageXP`.
- Returned to the game's default salvage-XP behavior.

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

For exact historical behavior, consult the preserved release packages rather than assuming every intermediate build is suitable for current use.
