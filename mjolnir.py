import os
from utils.text_cleaner import clean_text
from utils.detector import detect_parser
from docx import Document

from parser.classes_parser import ClassesParser
from parser.feats_parser import FeatsParser
from parser.races_parser import RacesParser
from parser.creatures_parser import CreaturesParser
from parser.equipment_parser import EquipmentParser
from parser.magic_items_parser import MagicItemsParser
from parser.skills_parser import SkillsParser
from parser.combat_actions_parser import CombatActionsParser
from parser.templates_parser import TemplatesParser
from parser.deities_parser import DeitiesParser
from parser.spells_parser import SpellsParser

FILE_TO_PARSER = {
    'Classes_Base.docx': 'classes',
    'Classes_Prestige.docx': 'classes',
    'Creatures.docx': 'creatures',
    'Deities.docx': 'deities',
    'Equipment.docx': 'equipment',
    'Feats.docx': 'feats',
    'Magic_Items.docx': 'magic_items',
    'Races.docx': 'races',
    'Skills_Actions.docx': 'skills',  # Note: special case if you later split Skills/Actions
    'Templates.docx': 'templates',
    'Spell_List.docx': 'spells',
    'Spells_Sorted.docx': 'spells',
    'Spell_Descriptions.docx': 'spells'
}

def run_ingestion():
    ingest_folder = 'ingest'
    files = [os.path.join(ingest_folder, f) for f in os.listdir(ingest_folder) if f.endswith('.docx')]

    spell_files = []

    for file_path in files:
        filename = os.path.basename(file_path)

        # First try static mapping
        parser_type = FILE_TO_PARSER.get(filename)

        # If static mapping fails, fallback to detector
        if not parser_type:
            document = Document(file_path)
            raw_lines = [p.text for p in document.paragraphs]
            cleaned_lines = clean_text(raw_lines)
            parser_type = detect_parser(cleaned_lines)

        if not parser_type:
            print(f"[-] Could not detect parser type for {filename}")
            continue

        if parser_type == 'spells':
            spell_files.append(file_path)
            continue

        # Direct hardwired parser dispatch
        if parser_type == 'classes':
            parser = ClassesParser()
        elif parser_type == 'feats':
            parser = FeatsParser()
        elif parser_type == 'races':
            parser = RacesParser()
        elif parser_type == 'creatures':
            parser = CreaturesParser()
        elif parser_type == 'equipment':
            parser = EquipmentParser()
        elif parser_type == 'magic_items':
            parser = MagicItemsParser()
        elif parser_type == 'skills':
            parser = SkillsParser()
        elif parser_type == 'combat_actions':
            parser = CombatActionsParser()
        elif parser_type == 'templates':
            parser = TemplatesParser()
        elif parser_type == 'deities':
            parser = DeitiesParser()
        else:
            print(f"[-] No parser implemented for {parser_type}")
            continue

        print(f"[+] Parsing {parser_type} from {filename}")
        parser.parse(file_path)

    # Special case: Spells require 3 files
    if spell_files:
        if len(spell_files) == 3:
            print(f"[+] Parsing spells from {len(spell_files)} files")
            parser = SpellsParser()
            parser.parse(spell_files)
        else:
            print(f"[!] Found {len(spell_files)} spell-related files but need exactly 3.")

if __name__ == "__main__":
    run_ingestion()
