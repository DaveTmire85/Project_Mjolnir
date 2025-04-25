from parser.base_parser import BaseParser
from utils.text_cleaner import TextCleaner

class FeatsParser(BaseParser):
    def parse(self):
        text_list = self.load_text()
        blocks = self.split_blocks(text_list)

        for block in blocks:
            feat = self.extract_feat(block)
            if feat:
                self.data.append(feat)

        return {'table': 'feats', 'records': self.data}

    def extract_feat(self, block_text):
        lines = block_text.split("\n")
        if len(lines) < 2:
            return None  # Too little information

        # Initialize empty feat
        feat = {
            'name': None,
            'type': None,
            'prerequisites': None,
            'benefit': None,
            'normal': None,
            'special': None,
            'source': None  # Optional field
        }

        feat['name'] = lines[0].strip()

        for line in lines[1:]:
            clean_line = TextCleaner.clean_text(line)
            if "Type:" in clean_line:
                feat['type'] = clean_line.split(":", 1)[-1].strip()
            elif "Prerequisite" in clean_line:
                feat['prerequisites'] = clean_line.split(":", 1)[-1].strip()
            elif "Benefit" in clean_line:
                feat['benefit'] = clean_line.split(":", 1)[-1].strip()
            elif "Normal" in clean_line:
                feat['normal'] = clean_line.split(":", 1)[-1].strip()
            elif "Special" in clean_line:
                feat['special'] = clean_line.split(":", 1)[-1].strip()
            elif "Source" in clean_line:
                feat['source'] = clean_line.split(":", 1)[-1].strip()

        return feat
s