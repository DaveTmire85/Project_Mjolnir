from utils.text_cleaner import clean_text
from db.db_manager import insert_entry

class MagicItemsParser:
    def parse(self, file_path):
        from docx import Document

        doc = Document(file_path)
        raw_lines = [p.text for p in doc.paragraphs]
        lines = clean_text(raw_lines)

        magic_items = []
        current_item = {}

        for line in lines:
            if "Aura" in line:
                current_item['aura'] = line.split(":")[1].strip()
            elif "Caster Level" in line:
                current_item['caster_level'] = line.split(":")[1].strip()
            elif "Requirements" in line:
                current_item['requirements'] = line.split(":")[1].strip()
            elif "Cost" in line:
                current_item['cost'] = line.split(":")[1].strip()
            elif "Weight" in line:
                current_item['weight'] = line.split(":")[1].strip()
            elif line.strip():
                current_item['name'] = line.strip()
                magic_items.append(current_item)
                current_item = {}

        for entry in magic_items:
            insert_entry('magic_items', entry)
