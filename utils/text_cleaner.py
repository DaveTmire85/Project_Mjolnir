import re

def clean_text(lines):
    """
    Cleans text lines by:
    - Stripping blank lines
    - Removing CrystalKeep headers/footers
    - Removing page numbers
    - Removing date stamps
    - Removing known URLs
    """
    cleaned_lines = []

    for line in lines:
        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        lower_line = line.lower()

        # Known CrystalKeep garbage
        if any(keyword in lower_line for keyword in [
            "dungeons & dragons 3.5 edition index",
            "collected by chet erez",
            "report suggestions or errors",
            "http://www.crystalkeep.com",
            "microsoft word",
        ]):
            continue

        # Skip page numbers
        if re.match(r'^page\s+\d+', lower_line):
            continue

        # Skip dates like "September 4, 2007"
        if re.match(r'^[a-z]+\s+\d{1,2},\s+\d{4}', lower_line):
            continue

        cleaned_lines.append(line)

    return cleaned_lines
