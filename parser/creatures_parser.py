from utils.text_cleaner import clean_text
from db.db_manager import insert_entry
from docx import Document

class CreaturesParser:
    def parse(self, file_path):
        from docx import Document

        doc = Document(file_path)
        raw_lines = [p.text for p in doc.paragraphs]
        lines = clean_text(raw_lines)

        creatures = []
        current_creature = {}

        for line in lines:
            if line.startswith("Creature:"):
                if current_creature:
                    creatures.append(current_creature)
                    current_creature = {}
                current_creature['name'] = line.replace("Creature:", "").strip()
            elif "Type" in line:
                current_creature['type'] = line.split(":")[1].strip()
            elif "Size" in line:
                current_creature['size'] = line.split(":")[1].strip()
            elif "HD" in line:
                current_creature['hit_dice'] = line.split(":")[1].strip()
            elif "Alignment" in line:
                current_creature['alignment'] = line.split(":")[1].strip()
            elif "Special Traits" in line:
                current_creature['special_traits'] = []
            elif current_creature.get('special_traits') is not None:
                current_creature['special_traits'].append(line.strip())

        if current_creature:
            creatures.append(current_creature)

        for entry in creatures:
            insert_entry('creatures', entry)
