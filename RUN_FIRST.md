# RUN FIRST: Testing Mjölnir Setup

## Quick Test Guide

1. Create a dummy `.docx` file inside a folder (example: `test_files/`) with the following simple content:

```
Thor
Player's Handbook
Pantheon: Norse
Alignment: Lawful Good
Domains: Strength, Storm
Weapon: Warhammer
Symbol: Hammer of Thunderbolts
```

2. Run Mjölnir on this test folder:

```bash
python mjolnir.py test_files/
```

3. Check the logs (logs/mjolnir.log) for parsing info.

4. Inspect the database:

```bash
sqlite3 db/mjolnir.db
```

5. Inside SQLite shell, check:

```sql
SELECT * FROM deities;
```

You should see your dummy entry for Thor.

## Troubleshooting
If no entry is found, check:
- LibreOffice installed and callable
- python-docx installed
- Correct directory paths
- No typo in dummy .docx

## You're ready!
If Thor shows up in the DB — Mjölnir is fully operational!