from utils.text_cleaner import clean_text
from db.db_manager import insert_entry

class EquipmentParser:
    def parse(self, file_path):
        from docx import Document

        doc = Document(file_path)
        raw_lines = [p.text for p in doc.paragraphs]
        lines = clean_text(raw_lines)

        equipment = []
        current_item = {}

        for line in lines:
            if "Armor Bonus" in line:
                current_item['armor_bonus'] = line.split(":")[1].strip()
            elif "Max Dex" in line:
                current_item['max_dex_bonus'] = line.split(":")[1].strip()
            elif "Armor Check Penalty" in line:
                current_item['armor_check_penalty'] = line.split(":")[1].strip()
            elif "Arcane Spell Failure" in line:
                current_item['arcane_spell_failure'] = line.split(":")[1].strip()
            elif "Cost" in line:
                current_item['cost'] = line.split(":")[1].strip()
            elif "Weight" in line:
                current_item['weight'] = line.split(":")[1].strip()
            elif line.strip():
                current_item['name'] = line.strip()
                equipment.append(current_item)
                current_item = {}

        for entry in equipment:
            insert_entry('equipment', entry)
