from parser.base_parser import BaseParser
from utils.text_cleaner import TextCleaner

class ItemsParser(BaseParser):
    def parse(self):
        text_list = self.load_text()
        blocks = self.split_blocks(text_list)

        for block in blocks:
            item = self.extract_item(block)
            if item:
                self.data.append(item)

        return {'table': 'items', 'records': self.data}

    def extract_item(self, block_text):
        lines = block_text.split("\n")
        if len(lines) < 2:
            return None

        item = {
            'name': None,
            'type': None,
            'subtype': None,
            'cost': None,
            'weight': None,
            'properties': None,
            'effect': None,
            'source': None
        }

        item['name'] = lines[0].strip()

        for line in lines[1:]:
            clean_line = TextCleaner.clean_text(line)
            if "Type:" in clean_line:
                type_parts = clean_line.split(":", 1)[-1].strip().split(";")
                item['type'] = type_parts[0].strip()
                if len(type_parts) > 1:
                    item['subtype'] = type_parts[1].strip()
            elif "Cost:" in clean_line:
                item['cost'] = clean_line.split(":", 1)[-1].strip()
            elif "Weight:" in clean_line:
                item['weight'] = clean_line.split(":", 1)[-1].strip()
            elif "Properties:" in clean_line:
                item['properties'] = clean_line.split(":", 1)[-1].strip()
            elif "Effect:" in clean_line:
                item['effect'] = clean_line.split(":", 1)[-1].strip()
            elif "Source:" in clean_line:
                item['source'] = clean_line.split(":", 1)[-1].strip()

        return item
