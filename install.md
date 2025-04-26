```markdown
# Mjölnir Changelog

## v2.0 - Major Forge Expansion
- Completed modular parser system across all entity types.
- Added FeatsParser (block parsing feats).
- Added SpellsParser (basic, by-class, full descriptions).
- Added ItemsParser (equipment vs magic items).
- Added RacesParser (full race block parsing).
- Added ClassesParser (block + progression table parsing).
- Added MonstersParser (full statblock parsing for monsters + NPCs).
- Added TemplatesParser (template application and modifiers).
- Expanded EntityTypeDetector to detect all new types automatically.
- Updated Launcher (mjolnir.py) to handle dynamic parser selection.
- Confirmed complete field coverage for all major D&D 3.5 entities.
- Logging system operational.
- Project fully ready for live testfires on sourcebooks.
📄 install.md (REAL, FINAL VERSION)
markdown
Copy
Edit
# Installation Instructions for Project Mjölnir

## Requirements

- Python 3.10+
- pip

## Setup Steps

1. Clone or extract the Project Mjölnir files.
2. Set up a clean Python environment (optional but recommended).
3. Install dependencies:

```bash
pip install -r requirements.txt
```
Review your directory structure if needed.

(Optional) Run a simple first test parsing file to confirm setup.

You're ready to start parsing!