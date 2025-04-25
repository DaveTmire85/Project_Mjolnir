from parser.base_parser import BaseParser
from utils.text_cleaner import TextCleaner

class SpellsParser(BaseParser):
    def parse(self):
        text_list = self.load_text()
        blocks = self.split_blocks(text_list)

        for block in blocks:
            spell = self.extract_spell(block)
            if spell:
                self.data.append(spell)

        return {'table': 'spells', 'records': self.data}

    def extract_spell(self, block_text):
        lines = block_text.split("\n")
        if len(lines) < 2:
            return None

        spell = {
            'name': None,
            'school': None,
            'subschool': None,
            'descriptors': None,
            'level_by_class': None,
            'components': None,
            'casting_time': None,
            'range': None,
            'effect': None,
            'duration': None,
            'saving_throw': None,
            'spell_resistance': None,
            'source': None
        }

        spell['name'] = lines[0].strip()

        for line in lines[1:]:
            clean_line = TextCleaner.clean_text(line)
            if "School:" in clean_line:
                school_parts = clean_line.split(":")[1].strip().split(";")
                spell['school'] = school_parts[0].strip()
                if len(school_parts) > 1:
                    spell['subschool'] = school_parts[1].strip()
            elif "Descriptors:" in clean_line:
                spell['descriptors'] = clean_line.split(":", 1)[-1].strip()
            elif "Level:" in clean_line:
                spell['level_by_class'] = clean_line.split(":", 1)[-1].strip()
            elif "Components:" in clean_line:
                spell['components'] = clean_line.split(":", 1)[-1].strip()
            elif "Casting Time:" in clean_line:
                spell['casting_time'] = clean_line.split(":", 1)[-1].strip()
            elif "Range:" in clean_line:
                spell['range'] = clean_line.split(":", 1)[-1].strip()
            elif "Effect:" in clean_line:
                spell['effect'] = clean_line.split(":", 1)[-1].strip()
            elif "Duration:" in clean_line:
                spell['duration'] = clean_line.split(":", 1)[-1].strip()
            elif "Saving Throw:" in clean_line:
                spell['saving_throw'] = clean_line.split(":", 1)[-1].strip()
            elif "Spell Resistance:" in clean_line:
                spell['spell_resistance'] = clean_line.split(":", 1)[-1].strip()
            elif "Source:" in clean_line:
                spell['source'] = clean_line.split(":", 1)[-1].strip()

        return spell
