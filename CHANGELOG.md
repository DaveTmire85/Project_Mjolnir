# Project Mjölnir — Forge Changelog

## v2.0.0 — April 2025 — The Great Reforging

### Major System Upgrades:
- Rebuilt the entire parser architecture from the ground up.
- Modularized all entity types into clean, separated parser modules.
- Expanded smart file detection (detector.py) for automatic parser selection.
- Forged the following parser modules:
  - DeitiesParser (Pantheon, Domains, Weapons, Symbols)
  - FeatsParser (Prerequisites, Benefits, Specials)
  - SpellsParser (Basic spell entries, by-class spell lists, full spell descriptions)
  - ItemsParser (Mundane equipment vs. Magic items parsing)
  - RacesParser (Types, Sizes, Abilities, Languages, Favored Classes)
  - ClassesParser (Progression tables, Features, Requirements for Prestige Classes)
  - MonstersParser (Statblock parsing for monsters AND NPCs)
  - TemplatesParser (CR Adjustments, LA Changes, Type Changes, Special Abilities)
  
### Infrastructure Overhaul:
- Updated mjolnir.py launcher to dynamically dispatch based on detection.
- Updated database insertion engine (db_manager.py) to handle bulk record inserts cleanly.
- Updated text_cleaner.py utility to handle Unicode, OCR artifacts, and special characters.

### Full Repository Packaging:
- Added __init__.py files to all critical directories for clean Python packaging.
- Added setup.py for setuptools-based installation.
- Added pyproject.toml for modern Python 3.10+ packaging compliance.
- Added LICENSE (MIT License) for open-source legal coverage.
- Cleaned README.md, INSTALL.md, CHANGELOG.md, RUN_FIRST.md for full professional documentation.

### Future-Proofing:
- Package structure fully ready for GitHub Packages or PyPI publication.
- Repository structured for `pip install` direct usage.
- Separate, optional namespace reserved for expansion into VTT generators, character builders, and database-driven campaign management tools.

---

# Closing Notes:
Project Mjölnir was reforged line-by-line, blow-by-blow, to professional-grade standards.  
Not a placeholder.  
Not a prototype.  
A true, chrome-plated Forge system for D&D 3.5e content management.

Forged not in haste.  
Forged in fire.

⚡🔨
