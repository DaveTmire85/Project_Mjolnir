from utils.text_cleaner import clean_text
from db.db_manager import insert_entry

class FeatsParser:
    def parse(self, file_path):
        from docx import Document
        
        doc = Document(file_path)
        raw_lines = [p.text for p in doc.paragraphs]
        lines = clean_text(raw_lines)
        
        feats = []
        current_feat = {}
        
        for line in lines:
            if line.startswith("[") and "]" in line:
                if current_feat:
                    feats.append(current_feat)
                    current_feat = {}
                parts = line.split("]")
                current_feat['type'] = parts[0][1:].strip()
                current_feat['name'] = parts[1].strip()
            elif "Prerequisite" in line:
                current_feat['prerequisite'] = line.split(":")[1].strip()
            elif "Benefit" in line:
                current_feat['benefit'] = line.split(":")[1].strip()
            elif "Source" in line:
                current_feat['source'] = line.split(":")[1].strip()
        
        if current_feat:
            feats.append(current_feat)
        
        for entry in feats:
            insert_entry('feats', entry)
