# Project Mjölnir: D&D 3.5e Data Parser and Database Builder

**Purpose:**  
Forge a fully relational, modular database from D&D 3.5 index `.docx` files, in preparation for future VTT integration.

---

## Features

- Converts `.doc` → `.docx` automatically using LibreOffice
- Modular parser system (deities, feats, spells, monsters, classes, races)
- Inserts parsed data into a normalized SQLite database
- Logging of errors and parsing issues
- Future extension hooks (text cleaning, data validation)

---

## Core Directories

- `/converter/` — handles document format conversions
- `/parser/` — modular parsers for different entity types
- `/db/` — database schema and interaction scripts
- `/utils/` — detection, cleaning, helper scripts
- `/logs/` — log output
- `/converted/` — converted `.docx` outputs
- `/parsed_output/` — optional JSON output dumps

---

## Running

```bash
python mjolnir.py <path_to_input_directory>
