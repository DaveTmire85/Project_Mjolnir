# Project Mjölnir

A modular, cross-platform D&D 3.5e parser and database builder.

Project Mjölnir ingests static CrystalKeep-style `.docx` indexes and builds a complete, structured SQLite database of gameplay entities.  
Designed for stability, speed, and future Virtual Tabletop (VTT) integration.

---

## Features

- **Static Document Ingestion**  
  Parses known `.docx` indexes quickly and reliably.  
  Fully offline, no live content crawling or guessing.

- **Multi-Entity Support**  
  Mjölnir parses and stores:
  - Deities
  - Feats
  - Base Classes
  - Prestige Classes
  - Races
  - Creatures
  - Equipment
  - Magic Items
  - Skills
  - Combat Actions
  - Templates
  - Spells (via combined triple-source parsing)

- **Cleaner System**  
  Automatically strips CrystalKeep headers, footers, metadata junk, page numbers, and noise.

- **SQLite Database Output**  
  All parsed entities are normalized into an easy-to-query SQLite backend.

- **Direct Parser Dispatching**  
  Lightweight ingestion pipeline — no parser factories, no overhead.

- **Multi-File Support**  
  Spell ingestion requires three specific sources: List, Sorted, and Descriptions.  
  Mjölnir handles multi-file ingestion cleanly and automatically.

- **Cross-Platform**  
  Runs on Windows, Mac, and Linux with Python 3.10+.

- **Built for Future Expansion**  
  Database ready for optional homebrew support, editing interfaces, or VTT linkage.

---

## Installation

Install from PyPI:

```bash
pip install project-mjolnir
```

Or install locally from source:

```bash
git clone https://github.com/DaveTmire85/Project_Mjolnir.git
cd Project_Mjolnir
pip install .
```

## Usage

Run the ingestion pipeline:

```bash
python mjolnir.py ingest
```

Inspect your resulting mjolnir.db SQLite database.

You can query the database directly or integrate it into your VTT project.

## Database Tables

| Table | Description |
|-------|-------------|
| deities | Gods, pantheons, domains, symbols |
| feats | All feats and mechanics |
| classes | Base and prestige classes |
| races | Playable race templates |
| creatures | Mounts, companions, familiars |
| equipment | Armor and shields |
| magic_items | Magic personal gear |
| skills | Core skill entries |
| combat_actions | Combat maneuver rules |
| templates | Monster and undead templates |
| spells | Full spell catalog |

## Requirements

- Python 3.10+
- python-docx

## Project Status

Version: 2.1.0  
Phase: Full Ingestion Complete (Forge Live)

Project Mjölnir is stable and ready for full database builds.

## License

MIT License

## Links

### PyPI Package
https://pypi.org/project/project-mjolnir/

### Source Code
https://github.com/DaveTmire85/Project_Mjolnir

### Issue Tracker
https://github.com/DaveTmire85/Project_Mjolnir/issues
