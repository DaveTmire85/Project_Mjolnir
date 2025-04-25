from parser.base_parser import BaseParser

class DeitiesParser(BaseParser):
    def parse(self):
        text_list = self.load_text()
        blocks = self.split_blocks(text_list)

        for block in blocks:
            deity = self.extract_deity(block)
            if deity:
                self.data.append(deity)

        return {'table': 'deities', 'records': self.data}

    def extract_deity(self, block_text):
        lines = block_text.split("\n")
        if len(lines) < 3:
            return None  # Too little information

        deity = {
            'name': lines[0].strip(),
            'source': lines[1].strip() if len(lines) > 1 else None,
            'pantheon': None,
            'alignment': None,
            'domains': None,
            'favored_weapon': None,
            'symbol': None
        }

        for line in lines[2:]:
            if "Pantheon" in line:
                deity['pantheon'] = line.split(":", 1)[-1].strip()
            elif "Alignment" in line:
                deity['alignment'] = line.split(":", 1)[-1].strip()
            elif "Domains" in line:
                deity['domains'] = line.split(":", 1)[-1].strip()
            elif "Weapon" in line:
                deity['favored_weapon'] = line.split(":", 1)[-1].strip()
            elif "Symbol" in line:
                deity['symbol'] = line.split(":", 1)[-1].strip()

        return deity
