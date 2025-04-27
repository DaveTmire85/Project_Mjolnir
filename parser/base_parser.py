from abc import ABC, abstractmethod
from docx import Document
from utils.text_cleaner import clean_text

class BaseParser(ABC):
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    @abstractmethod
    def parse(self):
        """
        Must be implemented by all child parsers.
        Handles parsing and preparing data for database insertion.
        """
        pass

    def load_text(self):
        """
        Loads and cleans text from a .docx file.
        Removes header/footer junk, normalizes lines.
        """
        document = Document(self.file_path)
        raw_lines = [p.text for p in document.paragraphs]
        return clean_text(raw_lines)

    def split_blocks(self, text_list):
        """
        Default block splitter based on empty lines between entries.
        Can be overridden by child parsers if needed.
        """
        blocks = []
        current_block = []

        for line in text_list:
            if line.strip() == "":
                if current_block:
                    blocks.append("\n".join(current_block))
                    current_block = []
            else:
                current_block.append(line)

        if current_block:
            blocks.append("\n".join(current_block))

        return blocks
