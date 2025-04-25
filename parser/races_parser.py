from parser.base_parser import BaseParser
from utils.text_cleaner import TextCleaner

class RacesParser(BaseParser):
    def parse(self):
        text_list = self.load_text()
        blocks = self.split_blocks(text_list)

        for block in blocks:
            race = self.extract_race(block)
            if race:
                self.data.append(race)

        return {'table': 'races', 'records': self.data}

    def extract_race(self, block_text):
        lines = block_text.split("\n")
        if len(lines) < 2:
            return None

        race = {
            'name': None,
            'type': None,
            'subtype': None,
            'size': None,
            'speed': None,
            'ability_mods': None,
            'traits': None,
            'languages': None,
            'source': None
        }

        race['name'] = lines[0].strip()

        for line in lines[1:]:
            clean_line = TextCleaner.clean_text(line)
            if "Type:" in clean_line:
                type_parts = clean_line.split(":", 1)[-1].strip().split(";")
                race['type'] = type_parts[0].strip()
                if len(type_parts) > 1:
                    race['subtype'] = type_parts[1].strip()
            elif "Size:" in clean_line:
                race['size'] = clean_line.split(":", 1)[-1].strip()
            elif "Speed:" in clean_line:
                race['speed'] = clean_line.split(":", 1)[-1].strip()
            elif "Ability Modifiers:" in clean_line or "Ability Mods:" in clean_line:
                race['ability_mods'] = clean_line.split(":", 1)[-1].strip()
            elif "Traits:" in clean_line:
                race['traits'] = clean_line.split(":", 1)[-1].strip()
            elif "Languages:" in clean_line:
                race['languages'] = clean_line.split(":", 1)[-1].strip()
            elif "Source:" in clean_line:
                race['source'] = clean_line.split(":", 1)[-1].strip()

        return race
