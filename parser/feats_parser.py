from parser.base_parser import BaseParser

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
            return None

        feat = {
            'name': lines[0].strip(),
            'type': None,
            'prerequisites': None,
            'benefit': None,
            'normal': None,
            'special': None,
            'source': None
        }

        for line in lines[1:]:
            if "Type" in line:
                feat['type'] = line.split(":", 1)[-1].strip()
            elif "Prerequisite" in line:
                feat['prerequisites'] = line.split(":", 1)[-1].strip()
            elif "Benefit" in line:
                feat['benefit'] = line.split(":", 1)[-1].strip()
            elif "Normal" in line:
                feat['normal'] = line.split(":", 1)[-1].strip()
            elif "Special" in line:
                feat['special'] = line.split(":", 1)[-1].strip()
            elif "Source" in line:
                feat['source'] = line.split(":", 1)[-1].strip()

        return feat
