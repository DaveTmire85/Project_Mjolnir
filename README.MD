Project Mjölnir
A modular, cross-platform D&D 3.5e parser and database builder, designed to forge structured game data from sourcebook indexes into a fully relational SQLite backend for future VTT integration.

Features
Accepts .docx files directly (no .doc conversion required)

Modular parser system:

Deities

Feats

Spells

Items

Races

Classes (Base, Prestige, Variants)

Normalizes data into a structured SQLite database (mjolnir.db)

Organized output directories:

/logs/ — logging parsing operations and errors

/parsed_output/ — optional JSON dumps

/ingest/ — source .docx files to be parsed

Lightweight dependency stack (Python + python-docx only)

Cross-platform compatibility (Windows, MacOS, Linux)

Future-proof architecture for VTT engine integration

Designed for stability, modularity, and raw parsing speed

Directory Layout
pgsql
Copy
Edit
Mjolnir/
├── config/
│   └── settings.py
├── db/
│   ├── db_manager.py
│   └── schema.sql
├── parser/
│   ├── base_parser.py
│   ├── deities_parser.py
│   ├── feats_parser.py
│   ├── spells_parser.py
│   ├── items_parser.py
│   ├── races_parser.py
│   └── classes_parser.py
├── utils/
│   ├── detector.py
│   └── text_cleaner.py
├── ingest/
│   └── (your sourcebook .docx files)
├── logs/
├── parsed_output/
├── mjolnir.py
├── README.md
├── INSTALL.md
├── RUN_FIRST.md
└── LICENSE
Requirements
Python 3.8 or newer

Python libraries:

python-docx

Installation
bash
Copy
Edit
pip install python-docx
Running Mjölnir
Place your .docx source indexes into the /ingest/ folder.

Run Mjölnir with:

bash
Copy
Edit
python mjolnir.py ingest/
Parsed data will be inserted into the database at /db/mjolnir.db.

Logs will appear in /logs/mjolnir.log.

You can inspect the database easily using tools like DB Browser for SQLite.

Supported Data Types

Entity Type	Status
Deities	✅ Done
Feats	✅ Done
Spells	✅ Done
Items	✅ Done
Races	✅ Done
Classes (Base/Prestige/Variants)	✅ Done
Monsters (NPCs/Creatures)	🔨 In Progress
Templates	🔨 In Progress
Current Development Roadmap
Add monsters_parser.py to handle monster statblocks.

Add templates_parser.py to handle creature templates and adjustments.

Expand detector.py to support new parser types.

Enhance multi-line and nested field parsing (especially for monster attacks and templates).

Normalize advanced magic systems (vestiges, soulmelds, maneuvers, psionics) in class features.

Author
Name: David Tofflemire

GitHub: DaveTmire85

Email: davetmire85@gmail.com

Forged in the fires of necessity. 🔨

License
This project is licensed under the MIT License.

