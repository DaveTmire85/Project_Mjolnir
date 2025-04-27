# Project Mjölnir - First Run Instructions

Welcome to Project Mjölnir.

Follow these steps to get Project Mjölnir operational:

---

## 1. Install Dependencies

```bash
pip install project-mjolnir
```

Or clone and install locally:

```bash
git clone https://github.com/DaveTmire85/Project_Mjolnir.git
cd Project_Mjolnir
pip install .
```

## 2. Run the Ingestion Pipeline

```bash
python mjolnir.py ingest
```

Mjölnir will:

- Auto-detect document types
- Parse static data fields
- Insert all entities into an SQLite database
- Skip bad or unknown files gracefully

## 3. Inspect Your Database

The resulting `mjolnir.db` SQLite database will be created at project root.

You can use tools like:

- DB Browser for SQLite
- sqlite3 command-line tool
- Or integrate it directly into your VTT project later.

## Optional: Manual Database Initialization

Normally, Project Mjölnir will automatically create the database on first run.

However, if you want to manually initialize it beforehand:

```bash
python db/init_db.py

⚡ Welcome to Awesomeness.