from utils.text_cleaner import clean_text
from db.db_manager import insert_entry
from docx import Document

class ClassesParser:
    def parse(self, file_path):
        from docx import Document
        
        doc = Document(file_path)
        raw_lines = [p.text for p in doc.paragraphs]
        lines = clean_text(raw_lines)
        
        classes = []
        current_class = {}
        
        for line in lines:
            if line.startswith("Class:"):
                if current_class:
                    classes.append(current_class)
                    current_class = {}
                current_class['name'] = line.replace("Class:", "").strip()
            elif "Hit Die" in line:
                current_class['hit_die'] = line.split(":")[1].strip()
            elif "Alignment" in line:
                current_class['alignment'] = line.split(":")[1].strip()
            elif "Skill Points" in line:
                current_class['skill_points'] = line.split(":")[1].strip()
            elif "Class Skills" in line:
                current_class['class_skills'] = line.split(":")[1].strip()
            elif "Weapon/Armor Proficiencies" in line:
                current_class['weapon_armor_proficiencies'] = line.split(":")[1].strip()
            elif "Class Features" in line:
                current_class['class_features'] = []
            elif current_class.get('class_features') is not None:
                current_class['class_features'].append(line.strip())
        
        if current_class:
            classes.append(current_class)
        
        for entry in classes:
            insert_entry('classes', entry)
