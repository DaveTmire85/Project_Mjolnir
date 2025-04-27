from utils.text_cleaner import clean_text
from db.db_manager import insert_entry
from docx import Document

class DeitiesParser:
    def parse(self, file_path):
        doc = Document(file_path)
        raw_lines = [p.text for p in doc.paragraphs]
        lines = clean_text(raw_lines)

        deities = []
        for line in lines:
            if line.strip() and "(" in line and ")" in line:
                parts = line.split()
                name = parts[0]
                reference = parts[1].strip("()")
                pantheon = parts[2]
                alignment = parts[3]
                rank = parts[4]
                nickname_portfolio = " ".join(parts[5:])

                deity = {
                    'name': name,
                    'reference': reference,
                    'pantheon': pantheon,
                    'alignment': alignment,
                    'rank': rank,
                    'nickname_portfolio': nickname_portfolio,
                    'domains': '',
                    'favored_weapon': '',
                    'symbol': ''
                }

                deities.append(deity)

        # Now second pass to fill domains, weapon, symbol
        # (Assuming the fields follow right after the basic entry in cleaned lines)

        for i, deity in enumerate(deities):
            j = i * 3 + 1  # assuming rough line offsets
            if j < len(lines):
                domains_line = lines[j]
                weapon_symbol_line = lines[j+1] if (j+1) < len(lines) else ""

                if domains_line:
                    deity['domains'] = domains_line.replace(",", ", ").strip()

                if weapon_symbol_line:
                    split = weapon_symbol_line.split()
                    deity['favored_weapon'] = split[0] if split else ''
                    deity['symbol'] = " ".join(split[1:]) if len(split) > 1 else ''

        for entry in deities:
            insert_entry('deities', entry)
