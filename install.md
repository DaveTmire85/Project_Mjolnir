# INSTALLATION GUIDE: Project Mjölnir

## Step 1: Clone or Copy the Repository

If cloning via Git:

```bash
git clone https://github.com/DaveTmire85/Project_Mjolnir.git
```

If manually copying:
- Ensure full directory structure is preserved.

## Step 2: Install Python Dependencies
Install required Python library:

```bash
pip install python-docx
```

That's it!

## Step 3: Prepare Your Source Files
- Mjölnir only accepts .docx files.
- Place your .docx indexes inside the `/ingest/` directory.
- Ensure your files are properly formatted and readable.

## Step 4: Initialize the Database
No action needed! On first run, Mjölnir will automatically create mjolnir.db and load the schema from `/db/schema.sql`.

## Ready to Run!
Run Mjölnir like this:

```bash
python mjolnir.py ingest/
```

Parsed data will be inserted into the database at `/db/mjolnir.db`.

Logs will be written to `/logs/mjolnir.log`.

## Troubleshooting

If you get a "No module named docx" error:
- Run `pip install python-docx`

If parsing fails:
- Check `/logs/mjolnir.log` for error details.
- Verify your .docx file structure.

✅ Nothing else needed.

