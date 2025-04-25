import os
import sys
import logging
from converter.doc_converter import DocConverter
from utils.detector import EntityTypeDetector
from db.db_manager import DBManager
from config.settings import Config

# Setup logging
logging.basicConfig(filename='logs/mjolnir.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Mjolnir:
    def __init__(self, input_dir):
        self.input_dir = input_dir
        self.db = DBManager()
        self.converter = DocConverter()
        self.detector = EntityTypeDetector()

    def run(self):
        files = os.listdir(self.input_dir)
        for file in files:
            file_path = os.path.join(self.input_dir, file)

            if file.endswith('.doc'):
                self.converter.convert(file_path)
                continue

            if file.endswith('.docx'):
                parser_class = self.detector.detect_parser(file_path)
                if parser_class:
                    parser = parser_class(file_path)
                    parsed_data = parser.parse()
                    self.db.insert(parsed_data)
                else:
                    logging.warning(f"Unsupported or undetected file: {file_path}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python mjolnir.py <directory_path>")
        sys.exit(1)

    input_folder = sys.argv[1]
    os.makedirs('logs', exist_ok=True)
    os.makedirs('converted', exist_ok=True)
    os.makedirs('parsed_output', exist_ok=True)

    mjolnir = Mjolnir(input_folder)
    mjolnir.run()
