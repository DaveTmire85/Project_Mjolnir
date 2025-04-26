# deities_parser.py - Version 2.1: Adjusted for no-arg parse()

from parser.base_parser import BaseParser
from docx import Document
import re
import os

class DeitiesParser(BaseParser):

    def parse(self):
        file_path = self.file_path  # Expect file_path to be set on the object
        if not file_path or not os.path.exists(file_path):
            print(f"[!] Invalid file path: {file_path}")
            return {'table': 'deities', 'records': []}

        document = Document(file_path)
        paragraphs = [p.text.strip() for p in document.paragraphs if p.text.strip()]

        # Clean leading junk (skip ToC, headers, etc.)
        start_idx = 0
        for idx, para in enumerate(paragraphs):
            if para.lower().startswith('aegir'):
                start_idx = idx
                break

        cleaned_paragraphs = paragraphs[start_idx:]

        deities = []
        block = []

        for line in cleaned_paragraphs:
            if not line.startswith('(') and not line.startswith('[') and block:
                if len(block) >= 9:
                    deities.append(self.parse_deity_block(block))
                block = []
            block.append(line)

        if block and len(block) >= 9:
            deities.append(self.parse_deity_block(block))

        return {
            'table': 'deities',
            'records': deities
        }

    def parse_deity_block(self, block):
        try:
            name = block[0]
            source = self.extract_source(block[1])
            pantheon = block[2]
            alignment = block[3]
            rank = block[4]
            portfolio = block[5]
            domains = block[6]
            favored_weapon = block[7]
            symbol = block[8] if len(block) > 8 else ''

            return {
                'name': name,
                'source': source,
                'pantheon': pantheon,
                'alignment': alignment,
                'rank': rank,
                'portfolio': portfolio,
                'domains': domains,
                'favored_weapon': favored_weapon,
                'symbol': symbol
            }
        except Exception as e:
            print(f"[!] Failed to parse deity block: {block} -- {e}")
            return {}

    def extract_source(self, line):
        match = re.search(r'\((.*?)\)', line)
        if match:
            return match.group(1)
        return ''
