# INSTALLATION GUIDE: Project Mjölnir

## Step 1: Install Python 3.8 or newer

Download and install Python if not already installed:  
https://www.python.org/downloads/

---

## Step 2: Install Python Libraries

Install python-docx:

```bash
pip install python-docx
```

## Step 3: Prepare Your Documents

Place all your .docx sourcebooks into the /ingest/ directory. Mine are included by default to help you build test data. To be honest, it should work just with that alone.

Ensure the files are readable and properly structured.

## Step 4: Running Mjölnir

Launch the parser:

```bash
python mjolnir.py ingest/
```

Parsed data will be inserted into /db/mjolnir.db.

Logs will appear in /logs/mjolnir.log.


