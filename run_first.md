```markdown
# First Run Instructions

1. Prepare your sourcebooks or indexes.
   - Supported formats: `.docx`
2. Place your files in a directory or subdirectory.
3. Run:

```bash
python mjolnir.py path_to_your_directory
```
Watch the console for details.

Parsed database will be updated at /db/mjolnir.db.

Notes:

Files are auto-detected and routed to the correct parser.

Any invalid or unknown files are skipped with warnings.