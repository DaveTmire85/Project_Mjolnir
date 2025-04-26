# Changelog
All notable changes to this project will be documented here.

The format is based on [Semantic Versioning](https://semver.org/).

---

## [0.1.0] — 2025-04-25

### Added
- Project Mjölnir foundation created: a modular D&D 3.5e parser and database builder.
- Full root directory structure:
  - `/converter/` — document format conversions (.doc → .docx)
  - `/parser/` — modular parsers for entity types
  - `/db/` — database schema and manager
  - `/utils/` — detectors and cleaners
  - `/logs/`, `/converted/`, `/parsed_output/`, `/ingest/`
- Created initial launcher: `mjolnir.py`
- Created document converter: `doc_converter.py`
- Designed SQLite database schema (`schema.sql`) covering:
  - Deities, Feats, Spells, Items, Races, Classes, Monsters, Templates
- Created database manager: `db_manager.py`
- Built utils:
  - `detector.py` — parser router
  - `text_cleaner.py` — OCR artifact fixer

---

## [0.2.0] — 2025-04-25

### Added
- `parser/deities_parser.py` — full deity block parsing.
- `parser/feats_parser.py` — feat name, type, prereqs, benefits, normal, special, source.
- `parser/spells_parser.py` — spell school, subschool, level by class, components, save, SR, and more.
- `parser/items_parser.py` — type, subtype, cost, weight, effect, properties.
- `parser/races_parser.py` — type, size, speed, ability mods, traits, languages.

### Improved
- Upgraded `detector.py` to auto-route documents to the correct parser (Deities, Feats, Spells, Items, Races).
- Modular parser system standardized using `BaseParser`.

---

## [0.2.1] — 2025-04-25

### Added
- `/ingest/` directory populated with real D&D 3.5e index `.docx` files.
- `README.md` completed and updated with full project details and author information:
  - Name: David Tofflemire
  - GitHub: DaveTmire85
  - Email: davetmire85@gmail.com
- `INSTALL.md` — clear installation and setup instructions.
- `RUN_FIRST.md` — first-run sanity test instructions.

---

## [Next Planned Release] — 0.3.0

### Will Add
- `parser/classes_parser.py` — parser for base and prestige classes (handling level tables and features).
- `parser/monsters_parser.py` — parser for monster statblocks (HD, CR, abilities, attacks).
- `parser/templates_parser.py` — parser for templates adjusting base creatures (LA/CR adjustments).
- Expansion of `detector.py` to recognize classes, monsters, and templates.
- Enhancements to multi-line and nested block parsing (for complex stat entries).

---

# Versions Summary

| Version | Date | Highlights |
|:---|:---|:---|
| 0.1.0 | 2025-04-25 | Core project architecture and launcher created |
| 0.2.0 | 2025-04-25 | Deities, Feats, Spells, Items, Races parsers completed |
| 0.2.1 | 2025-04-25 | Ingest populated, documentation finalized |
| 0.3.0 | Planned | Heavy-duty class, monster, and template parsers |

---
