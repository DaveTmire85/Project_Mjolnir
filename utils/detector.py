from parser.deities_parser import DeitiesParser
from parser.feats_parser import FeatsParser
from parser.spells_parser import SpellsParser
from parser.items_parser import ItemsParser
from parser.races_parser import RacesParser
from parser.classes_parser import ClassesParser
# from parser.monsters_parser import MonstersParser  # Uncomment if you have the MonstersParser implemented
# from parser.templates_parser import TemplatesParser  # Uncomment if you have the TemplatesParser implemented

class EntityTypeDetector:
    def detect_parser(self, file_path):
        try:
            from docx import Document
            document = Document(file_path)
            first_page_text = "\n".join([p.text for p in document.paragraphs[:20]]).lower()

            if "domains" in first_page_text or "deity" in first_page_text:
                return DeitiesParser
            elif "prerequisite" in first_page_text and "benefit" in first_page_text:
                return FeatsParser
            elif "casting time" in first_page_text and "school" in first_page_text:
                return SpellsParser
            elif "cost" in first_page_text and "weight" in first_page_text:
                return ItemsParser
            elif "racial traits" in first_page_text or "size" in first_page_text:
                return RacesParser
            elif "hit die" in first_page_text or "base attack bonus" in first_page_text:
                return ClassesParser
#           elif "challenge rating" in first_page_text or "special attacks" in first_page_text:  # Uncomment if you have the MonstersParser implemented
#               return MonstersParser
#           elif "template" in first_page_text or "level adjustment" in first_page_text:  # Uncomment if you have the TemplatesParser implemented
#               return TemplatesParser

        except Exception as e:
            print(f"[!] Failed to detect entity type for {file_path}: {e}")
            return None

        return None
