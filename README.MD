# Project Mjölnir
A modular, cross-platform D&D 3.5e parser and database builder, designed to forge structured game data from sourcebook indexes into a fully relational SQLite backend for future VTT integration.

---

## Features

- Accepts `.docx` files directly (no `.doc` conversion required)
- Modular parser system:
  - Deities
  - Feats
  - Spells
  - Items
  - Races
- Normalizes data into a structured SQLite database (`mjolnir.db`)
- Organized output directories:
  - `/logs/` — logging parsing operations and errors
  - `/converted/` — (legacy, currently unused)
  - `/parsed_output/` — optional JSON dumps
- Lightweight dependency stack (Python + python-docx only)
- Cross-platform compatibility (Windows, MacOS, Linux)
- Future-proof architecture for VTT engine integration
- Designed for stability, modularity, and raw speed

---

## Directory Layout

```
Mjolnir/
├── config/
│   └── settings.py
├── converter/
│   └── (currently unused)
├── db/
│   ├── db_manager.py
│   └── schema.sql
├── parser/
│   ├── base_parser.py
│   ├── deities_parser.py
│   ├── feats_parser.py
│   ├── spells_parser.py
│   ├── items_parser.py
│   └── races_parser.py
├── utils/
│   ├── detector.py
│   └── text_cleaner.py
├── ingest/
│   └── (your sourcebook .docx files go here)
├── logs/
├── converted/
├── parsed_output/
├── mjolnir.py
├── README.md
├── INSTALL.md
├── RUN_FIRST.md
└── LICENSE
```

---

## Requirements

- Python 3.8 or newer
- Python libraries:
  - `python-docx`

---

## Installation

```bash
pip install python-docx
```

## Running Mjölnir

Place your .docx source indexes into the /ingest/ folder.

Run Mjölnir with:

```bash
python mjolnir.py ingest/
```

Check /logs/mjolnir.log for parsing results and any issues.

Inspect your database at /db/mjolnir.db (SQLite format).

You can view the database easily using tools like DB Browser for SQLite.

## Supported Data Types

| Entity Type | Status |
|:---|:---|
| Deities | ✅ Done |
| Feats | ✅ Done |
| Spells | ✅ Done |
| Items | ✅ Done |
| Races | ✅ Done |
| Classes (Base/Prestige/Variants) | ✅ Done |
| Monsters (NPCs/Creatures) | 🔨 In Progress |
| Templates | 🔨 In Progress |

## Current Development Roadmap

- Add classes_parser.py to handle class tables and spellcasting levels.
- Add monsters_parser.py to handle full creature statblocks.
- Add templates_parser.py to handle LA/CR adjustments and overlays.
- Improve field parsing for complex nested fields (e.g., spell-like abilities, monster special attacks).
- Expand relational database cross-linking (classes → spells, races → abilities).

## Author

Name: David Tofflemire

GitHub: DaveTmire85

Email: davetmire85@gmail.com

Forged in the fires of determination. 🔨

## License

This project is licensed under the MIT License.