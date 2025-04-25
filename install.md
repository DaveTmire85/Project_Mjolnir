# INSTALLATION GUIDE: Project Mjölnir

---

## 1. Clone or Copy the Repository

If cloning via Git:

```bash
git clone https://github.com/DaveTmire85/Project_Mjolnir.git
```

If manually copying:
- Ensure full directory structure is preserved.

## 2. Install Python Requirements

Use pip to install the necessary Python library:

```bash
pip install python-docx
```

## 3. Install LibreOffice

LibreOffice is needed for .doc to .docx conversion.

Download here: [LibreOffice Download](https://www.libreoffice.org/download/download/)

Ensure soffice is available in your system PATH.

Test installation:

```bash
soffice --version
```

If you see a version number, you're good to go.

## 4. (Optional) Install a SQLite GUI Browser

For inspecting and verifying your database:

[DB Browser for SQLite](https://sqlitebrowser.org/)

Example (on Linux):

```bash
sudo apt install sqlitebrowser
```

## 5. Initialize the Database

Nothing manual required!

On first run, Mjölnir automatically:
- Creates `/db/mjolnir.db`
- Initializes the database using `/db/schema.sql`

## 6. First Run

Prepare a test folder with .doc or .docx files.

Run Mjölnir:

```bash
python mjolnir.py path/to/your/docx/files/
```

Check:
- `/db/mjolnir.db` for inserted data
- `/logs/mjolnir.log` for parsing details

