import sys
import os
from db.db_manager import DBManager
from utils.text_cleaner import TextCleaner
from utils.detector import detect_entity
from parser.deities_parser import DeitiesParser
from parser.feats_parser import FeatsParser
from parser.spells_parser import SpellsParser
from parser.items_parser import ItemsParser
from parser.races_parser import RacesParser
from parser.classes_parser import ClassesParser
from parser.monsters_parser import MonstersParser
from parser.templates_parser import TemplatesParser

class Mjolnir:

    def __init__(self):
        self.db = DBManager()

    def run(self, input_path):
        files = self.collect_files(input_path)
        for file in files:
            if not file.endswith(".docx"):
                continue

            print(f"[+] Parsing {file}")
            parser = self.select_parser(file)
            if not parser:
                print(f"[!] No suitable parser for {file}")
                continue

            parsed_data = parser.parse()
            if parsed_data['records']:
                self.db.insert(parsed_data['table'], parsed_data['records'])
            else:
                print(f"[!] No records parsed from {file}")

    def collect_files(self, path):
        collected = []
        if os.path.isfile(path):
            collected.append(path)
        else:
            for root, dirs, files in os.walk(path):
                for file in files:
                    collected.append(os.path.join(root, file))
        return collected

    def select_parser(self, file_path):
        text_list = TextCleaner.load_text(file_path)
        entity = detect_entity(text_list)

        if entity == "deities":
            return DeitiesParser(file_path)
        elif entity == "feats":
            return FeatsParser(file_path)
        elif entity == "spells":
            return SpellsParser(file_path)
        elif entity == "equipment" or entity == "magic_items":
            return ItemsParser(file_path)
        elif entity == "races":
            return RacesParser(file_path)
        elif entity == "classes":
            return ClassesParser(file_path)
        elif entity == "monsters":
            return MonstersParser(file_path)
        elif entity == "templates":
            return TemplatesParser(file_path)
        else:
            return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mjolnir.py path_to_docx_or_directory")
        sys.exit(1)

    mjolnir = Mjolnir()
    mjolnir.run(sys.argv[1])
