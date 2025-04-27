from utils.text_cleaner import clean_text
from db.db_manager import insert_entry

class RacesParser:
    def parse(self, file_path):
        from docx import Document
        
        doc = Document(file_path)
        raw_lines = [p.text for p in doc.paragraphs]
        lines = clean_text(raw_lines)

        races = []
        current_race = {}

        for line in lines:
            if line.startswith("Race:"):
                if current_race:
                    races.append(current_race)
                    current_race = {}
                current_race['name'] = line.replace("Race:", "").strip()
            elif "Ability Modifiers" in line:
                current_race['ability_modifiers'] = line.split(":")[1].strip()
            elif "Favored Class" in line:
                current_race['favored_class'] = line.split(":")[1].strip()
            elif "Size" in line:
                current_race['size'] = line.split(":")[1].strip()
            elif "Movement" in line:
                current_race['movement'] = line.split(":")[1].strip()
            elif "Vision" in line:
                current_race['vision'] = line.split(":")[1].strip()
            elif "Level Adjustment" in line:
                current_race['level_adjustment'] = line.split(":")[1].strip()
            elif "Features" in line:
                current_race['features'] = []
            elif current_race.get('features') is not None:
                current_race['features'].append(line.strip())

        if current_race:
            races.append(current_race)

        for entry in races:
            insert_entry('races', entry)
