# INSTALLATION GUIDE: Project Mjölnir

## Step 1: Clone or Copy the Repository

If cloning via Git:
```bash
git clone https://github.com/DaveTmire85/Mjolnir.git
```

If manually copying:
- Ensure full directory structure is preserved.

## Step 2: Install Python Dependencies
Install required Python libraries:

```bash
pip install python-docx
```

## Step 3: Install LibreOffice
LibreOffice is needed to convert .doc files into .docx:

Download: https://www.libreoffice.org/download/download/

Ensure the soffice command is available in your system PATH.

Test by running:

```bash
soffice --version
```

If you get a version number, you're good.

## Step 4: Initialize the Database
No action needed!
On first run, Mjölnir will automatically create mjolnir.db and load the schema from /db/schema.sql.

## Ready to Run!
🔥 You can now start parsing documents with:

```bash
python mjolnir.py <path_to_your_docx_files>
```

## Troubleshooting
If you get a "no module named docx" error:
- Run `pip install python-docx`

If .doc to .docx conversion fails:
- Check LibreOffice installation.