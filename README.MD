# Project Mjölnir: D&D 3.5e Data Parser and Database Builder

**Purpose:**  
Forge a fully relational, modular database from D&D 3.5e index `.docx` files, preparing for future VTT integration.

---

## Features

- Converts `.doc` → `.docx` automatically using LibreOffice.
- Modular parser system (deities, feats, spells, monsters, classes, races, templates).
- Inserts parsed data into a normalized SQLite database.
- Structured logs and error handling.
- Designed for full cross-platform compatibility (Windows, MacOS, Linux).
- Future extension hooks (data validation, rule automation, JSON export).

---

## Core Directory Structure

| Folder | Purpose |
|:---|:---|
| `/converter/` | Document format conversions (.doc → .docx) |
| `/parser/` | Modular parsers for each data type |
| `/db/` | Database schema and interaction modules |
| `/utils/` | Detection, cleaning, helper scripts |
| `/logs/` | Output logs and error reports |
| `/converted/` | Converted `.docx` outputs |
| `/parsed_output/` | Optional JSON exports for sanity checking |

---

## Quick Start

1. Install the requirements (see [INSTALL.md](INSTALL.md)).
2. Prepare a folder with `.doc` or `.docx` index files.
3. Run Mjölnir:

```bash
python mjolnir.py path/to/your/docx/files/
```

Check `/db/mjolnir.db` for parsed content.

## Data Source Philosophy

Project Mjölnir is specifically designed to process structured `.docx` index files derived from D&D 3.5e source material.

- **Why .docx?**
  - Parsing directly from official PDFs is notoriously unreliable due to inconsistent layouts, broken tables, and OCR artifacts.
  - `.docx` indexes provide a plaintext-like structure that allows for accurate, scalable data extraction.
  - This choice ensures the database remains clean, normalized, and relational — without needing fragile, error-prone parsing hacks.

- **Origin of Indexes:**
  - The `.docx` indexes were originally collected from community archives no longer reliably available.
  - These documents are tailored and semi-structured — meaning Mjölnir's parsers are optimized specifically for this format.
  
- **Sustainability:**
  - Future versions of Mjölnir will remain tuned to ingest properly formatted `.docx` files.
  - Community tools may later be developed to convert other materials into compatible `.docx` format if needed.
  
- **Transparency:**
  - Mjölnir is not designed to parse full proprietary PDFs or infringe copyright; it operates only on derived index materials.

---

## Requirements

- Python 3.8+
- LibreOffice (with soffice command available)
- Python libraries:
  - python-docx

(Optional: Install SQLiteBrowser if you want a GUI to inspect the database.)

## Author

- Name: David Tofflemire
- GitHub: DaveTmire85
- Email: davetmire85@gmail.com

Forged in the fires of determination. 🔨

## License

This project is licensed under the MIT License.