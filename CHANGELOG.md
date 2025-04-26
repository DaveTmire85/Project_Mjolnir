# Changelog
All notable changes to this project will be documented here.

The format is based on [Semantic Versioning](https://semver.org/).

---

## [0.1.0] — 2025-04-25

### Added
- Project Mjölnir foundation created: a modular D&D 3.5e parser and database builder.
- Full root directory structure:
  - `/parser/` — modular parsers for entity types
  - `/db/` — database schema and manager
  - `/utils/` — detectors and cleaners
  - `/logs/`, `/converted/`, `/parsed_output/`, `/ingest/`
- Created initial launcher: `mjolnir.py`
- Designed SQLite database schema (`schema.sql`) covering:
  - Deities, Feats, Spells, Items, Races, Classes, Monsters, Templates
- Created database manager: `db_manager.py`
- Built utilities:
  - `detector.py` — parser router
  - `text_cleaner.py` — OCR artifact fixer

---

## [0.2.0] — 2025-04-25

### Added
- `parser/deities_parser.py` — full deity block parsing.
- `parser/feats_parser.py` — feat name, type, prerequisites, benefits, normal, special, source.
- `parser/spells_parser.py` — spell school, subschool, level by class, components, effect, range, save, spell resistance.
- `parser/items_parser.py` — item type, subtype, cost, weight, effect, properties.
- `parser/races_parser.py` — race type, subtype, size, speed, ability mods, traits, languages.

### Improved
- Upgraded `detector.py` to auto-route `.docx` documents to the correct parser.
- Standardized modular parser design using `BaseParser`.

---

## [0.2.1] — 2025-04-25

### Changed
- **Removed** document conversion system (no more `.doc` to `.docx` conversions).
- **Deleted** `/converter/` directory and all LibreOffice dependencies.
- **Simplified `mjolnir.py`**: 
  - Direct `.docx` ingestion only.
  - Skips non-`.docx` files automatically.
- **Updated README.md**:
  - Clarified `.docx`-only requirement.
  - Removed all references to LibreOffice or soffice.
- **Updated INSTALL.md**:
  - Clean install guide for pure python-docx installation.
- **Updated RUN_FIRST.md**:
  - Reflects direct `.docx` parsing and first-run verification.

### Added
- `/ingest/` folder populated with real D&D 3.5e source indexes in `.docx` format.
- Full project documentation polished for public GitHub readiness.

---

## [Next Planned Release] — 0.3.0

### Will Add
- `parser/classes_parser.py` — for base and prestige classes (level tables, class features, spellcasting).
- `parser/monsters_parser.py` — for creature statblocks (HD, AC, attacks, abilities).
- `parser/templates_parser.py` — for template application (adjustments to CR, LA, abilities).
- `detector.py` expansion to recognize Classes, Monsters, Templates.
- Advanced multi-line and nested field parsing.

---

# Versions Summary

| Version | Date | Highlights |
|:---|:---|:---|
| 0.1.0 | 2025-04-25 | Core project architecture and launcher created |
| 0.2.0 | 2025-04-25 | Deities, Feats, Spells, Items, Races parsers completed |
| 0.2.1 | 2025-04-25 | Conversion system removed, `.docx`-only setup finalized, documentation rewritten |
| 0.3.0 | Planned | Heavy-duty Class, Monster, Template parsers to be added |

---
