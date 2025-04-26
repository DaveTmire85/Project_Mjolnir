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
- `parser/items_parser.py` — item type, subtype, cost, weight, properties, effects.
- `parser/races_parser.py` — type, size, speed, ability mods, traits, languages.

### Improved
- Upgraded `detector.py` to auto-route `.docx` documents to the correct parser (Deities, Feats, Spells, Items, Races).
- Modular parser system standardized using `BaseParser`.

---

## [0.2.1] — 2025-04-25

### Changed
- **Removed** document conversion dependency:
  - Deleted `/converter/`
  - Stripped LibreOffice (soffice) dependency.
  - Mjölnir now **only processes `.docx` files** directly.
- Simplified `mjolnir.py`:
  - Skips non-`.docx` files automatically.
  - Faster parsing, fewer dependencies.
  
### Added
- `/ingest/` directory populated with real D&D 3.5e index `.docx` files.
- `README.md` completed and updated:
  - Now specifies `.docx`-only ingestion.
  - Author Info:
    - Name: David Tofflemire
    - GitHub: DaveTmire85
    - Email: davetmire85@gmail.com
- `INSTALL.md` updated to match `.docx`-only ingestion.
- `RUN_FIRST.md` created to guide first launch and validation.

---

## [Next Planned Release] — 0.3.0

### Will Add
- `parser/classes_parser.py` — parser for base and prestige classes (handling level tables, features, prerequisites).
- `parser/monsters_parser.py` — parser for full D&D statblocks (HD, CR, AC, attacks, special abilities).
- `parser/templates_parser.py` — parser for templates modifying base creatures (type changes, CR/LA adjustments).
- Expansion of `detector.py` to recognize Classes, Monsters, and Templates.
- Enhancements to multi-line and nested block parsing (handling class tables, monster routines, etc.).

---

# Versions Summary

| Version | Date | Highlights |
|:---|:---|:---|
| 0.1.0 | 2025-04-25 | Core project architecture and launcher created |
| 0.2.0 | 2025-04-25 | Deities, Feats, Spells, Items, Races parsers completed |
| 0.2.1 | 2025-04-25 | Conversion code removed, `.docx`-only system finalized, ingest populated |
| 0.3.0 | Planned | Heavy-duty Class, Monster, and Template parsers |

---
