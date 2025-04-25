from parser.deities_parser import DeitiesParser
# Future imports: feats_parser, spells_parser, items_parser, races_parser, etc.

class EntityTypeDetector:
    def detect_parser(self, file_path):
        """
        Analyze the file content to guess what parser should be used.
        Returns a parser class, or None if unknown.
        """
        try:
            from docx import Document
            document = Document(file_path)
            first_page_text = "\n".join([p.text for p in document.paragraphs[:10]]).lower()

            if "domains" in first_page_text or "deity" in first_page_text:
                return DeitiesParser

            # Future extension: add more detectors here
            # elif "feat" in first_page_text:
            #     return FeatsParser
            # elif "spell resistance" in first_page_text:
            #     return SpellsParser
            # etc...

        except Exception as e:
            print(f"[!] Failed to detect entity type for {file_path}: {e}")
            return None

        return None
