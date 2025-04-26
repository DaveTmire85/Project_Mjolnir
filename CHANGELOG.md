# Changelog
All notable changes to this project will be documented here.

The format is based on [Semantic Versioning](https://semver.org/).

---

## [0.1.0] — 2025-04-25

### Added
- Project Mjölnir foundation created: a modular D&D 3.5e parser and database builder.
- Full root directory structure, including ingest, parsed output, logs, and modules.

---

## [0.2.0] — 2025-04-25

### Added
- Parsers for:
  - Deities
  - Feats
  - Spells
  - Items
  - Races
- Upgraded detector.py for correct parser routing.

---

## [0.2.1] — 2025-04-25

### Changed
- Removed `.doc` to `.docx` conversion.
- Fully committed to `.docx` ingestion only.
- Updated README.md, INSTALL.md, and RUN_FIRST.md accordingly.

---

## [0.3.0] — 2025-04-25

### Added
- `parser/classes_parser.py` created:
  - Parses base classes, prestige classes, and class variants.
  - Extracts hit die, skill points, proficiencies, class features, spellcasting, and level progression.
  - Flexible feature tagging system for future expansions (vestiges, soulmelds, maneuvers, psionics, etc.).
- Updated `detector.py` to recognize Class documents.

---

## [Next Planned Release] — 0.4.0

### Will Add
- `parser/monsters_parser.py` — full D&D statblock parser.
- `parser/templates_parser.py` — template adjustments (CR, LA, abilities).
- Further flexible expansion of detector and database schema.

---

# Versions Summary

| Version | Date | Highlights |
|:---|:---|:---|
| 0.1.0 | 2025-04-25 | Project foundation established |
| 0.2.0 | 2025-04-25 | Deities, Feats, Spells, Items, Races parsers completed |
| 0.2.1 | 2025-04-25 | LibreOffice removed, .docx-only system finalized |
| 0.3.0 | 2025-04-25 | ClassesParser built, detector upgraded |
| 0.4.0 | Planned | Monsters, Templates parsing expansion |
