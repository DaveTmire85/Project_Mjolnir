from utils.text_cleaner import clean_text
from db.db_manager import insert_entry

class SkillsParser:
    def parse(self, file_path):
        from docx import Document

        doc = Document(file_path)
        raw_lines = [p.text for p in doc.paragraphs]
        lines = clean_text(raw_lines)

        skills = []
        current_skill = {}

        for line in lines:
            if line.startswith("Skill:"):
                if current_skill:
                    skills.append(current_skill)
                    current_skill = {}
                current_skill['name'] = line.replace("Skill:", "").strip()
            elif "Ability" in line:
                current_skill['ability'] = line.split(":")[1].strip()
            elif "Trained Only" in line:
                current_skill['trained_only'] = line.split(":")[1].strip()
            elif "Armor Check" in line:
                current_skill['armor_check_penalty'] = line.split(":")[1].strip()
            elif "Synergy" in line:
                current_skill['synergy'] = line.split(":")[1].strip()
            elif "Special" in line:
                current_skill['special'] = line.split(":")[1].strip()

        if current_skill:
            skills.append(current_skill)

        for entry in skills:
            insert_entry('skills', entry)
