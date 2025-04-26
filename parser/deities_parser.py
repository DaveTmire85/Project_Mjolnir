from parser.base_parser import BaseParser
from utils.text_cleaner import TextCleaner
import docx

class DeitiesParser(BaseParser):

    def parse(self):
        records = []
        doc = docx.Document(self.file_path)

        for table in doc.tables:
            for row in table.rows:
                cells = [TextCleaner.clean_text(cell.text) for cell in row.cells]
                
                # Safety: Skip header rows (look for keyword "Pantheon" or "Align" or similar)
                if len(cells) >= 9 and cells[2].lower() != "pantheon" and cells[3].lower() != "align":
                    deity = self.extract_deity_from_cells(cells)
                    if deity:
                        records.append(deity)

        return {'table': 'deities', 'records': records}

    def extract_deity_from_cells(self, cells):
        try:
            deity = {
                'name': cells[0],
                'source': cells[1],
                'pantheon': cells[2],
                'alignment': cells[3],
                'rank': cells[4],
                'portfolio': cells[5],
                'domains': cells[6],
                'favored_weapon': cells[7],
                'symbol': cells[8]
            }
            return deity
        except IndexError:
            return None
