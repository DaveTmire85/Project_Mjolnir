from utils.text_cleaner import clean_text
from db.db_manager import insert_entry

class TemplatesParser:
    def parse(self, file_path):
        from docx import Document

        doc = Document(file_path)
        raw_lines = [p.text for p in doc.paragraphs]
        lines = clean_text(raw_lines)

        templates = []
        current_template = {}

        for line in lines:
            if line.startswith("Template:"):
                if current_template:
                    templates.append(current_template)
                    current_template = {}
                current_template['name'] = line.replace("Template:", "").strip()
            elif "Source" in line:
                current_template['source'] = line.split(":")[1].strip()
            elif "Type Change" in line:
                current_template['creature_type_change'] = line.split(":")[1].strip()
            elif "Ability Changes" in line:
                current_template['ability_changes'] = line.split(":")[1].strip()
            elif "Natural Armor" in line:
                current_template['natural_armor_bonus'] = line.split(":")[1].strip()
            elif "Level Adjustment" in line:
                current_template['level_adjustment'] = line.split(":")[1].strip()
            elif "Challenge Rating" in line:
                current_template['challenge_rating_change'] = line.split(":")[1].strip()
            elif "Immunities" in line:
                current_template['immunities'] = line.split(":")[1].strip()

        if current_template:
            templates.append(current_template)

        for entry in templates:
            insert_entry('templates', entry)
