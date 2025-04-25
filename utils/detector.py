from parser.deities_parser import DeitiesParser
from parser.feats_parser import FeatsParser
from parser.spells_parser import SpellsParser
from parser.items_parser import ItemsParser
from parser.races_parser import RacesParser
# Later: import classes_parser, monsters_parser, templates_parser

class EntityTypeDetector:
    def detect_parser(self, file_path):
        """
        Analyze the file content to guess what parser should be used.
        Returns a parser class, or None if unknown.
        """
        try:
            from docx import Document
            document = Document(file_path)
            first_page_text = "\n".join([p.text for p in document.paragraphs[:10]]).lower()

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
            # Placeholders for heavy hitters
            # elif "hit die" in first_page_text or "special attacks" in first_page_text:
            #     return MonstersParser
            # elif "base attack bonus" in first_page_text and "save" in first_page_text:
            #     return ClassesParser
            # elif "template" in first_page_text and "adjustment" in first_page_text:
            #     return TemplatesParser

        except Exception as e:
            print(f"[!] Failed to detect entity type for {file_path}: {e}")
            return None

        return None
