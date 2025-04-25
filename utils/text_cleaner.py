import re

class TextCleaner:
    @staticmethod
    def clean_text(text):
        """
        Clean weird OCR artifacts, multiple spaces, strange characters.
        """
        text = text.replace('\u2013', '-')  # Fix en-dashes
        text = text.replace('\u2014', '-')  # Fix em-dashes
        text = text.replace('\u2019', "'")  # Fix right single quotes
        text = text.replace('\u2018', "'")  # Fix left single quotes
        text = text.replace('\u201c', '"').replace('\u201d', '"')  # Fix quotes
        text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with one
        text = text.strip()
        return text
