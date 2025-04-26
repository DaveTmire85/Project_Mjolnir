from parser.deities_parser import DeitiesParser
from parser.feats_parser import FeatsParser
from parser.spells_parser import SpellsParser
from parser.items_parser import ItemsParser
from parser.races_parser import RacesParser
from parser.classes_parser import ClassesParser
# Future: import monsters_parser, templates_parser when built

class EntityTypeDetector:
    def detect_parser(self, file_path):
        try:
            from docx import Document
            document = Document(file_path)
            first_page_text = "\n".join([p.text for p in document.paragraphs[:20]]).lower()

            if "pantheon" in first_page_text or "domains" in first_page_text:
                return DeitiesParser
            elif "prerequisite" in first_page_text and "benefit" in first_page_text:
                return FeatsParser
            elif "school" in first_page_text and "spell resistance" in first_page_text:
                return SpellsParser
            elif "cost" in first_page_text and "weight" in first_page_text:
                return ItemsParser
            elif "racial traits" in first_page_text or "favored class" in first_page_text:
                return RacesParser
            elif "class features" in first_page_text or "hit die" in first_page_text:
                return ClassesParser
            # Future: elif "hit dice" in first_page_text: (for monsters_parser)
            # Future: elif "template traits" in first_page_text: (for templates_parser)

        except Exception as e:
            print(f"[!] Failed to detect entity type for {file_path}: {e}")
            return None

        return None
