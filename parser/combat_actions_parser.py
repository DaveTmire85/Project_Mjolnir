from utils.text_cleaner import clean_text
from db.db_manager import insert_entry
from docx import Document

class CombatActionsParser:
    def parse(self, file_path):
        from docx import Document

        doc = Document(file_path)
        raw_lines = [p.text for p in doc.paragraphs]
        lines = clean_text(raw_lines)

        actions = []
        current_action = {}

        for line in lines:
            if line.startswith("Action:"):
                if current_action:
                    actions.append(current_action)
                    current_action = {}
                current_action['name'] = line.replace("Action:", "").strip()
            elif "Attack Roll" in line:
                current_action['attack_roll'] = line.split(":")[1].strip()
            elif "Steps" in line:
                current_action['steps'] = line.split(":")[1].strip()
            elif "Feats Affecting" in line:
                current_action['feats_affecting'] = line.split(":")[1].strip()
            elif "Special Modifiers" in line:
                current_action['special_modifiers'] = line.split(":")[1].strip()

        if current_action:
            actions.append(current_action)

        for entry in actions:
            insert_entry('combat_actions', entry)
