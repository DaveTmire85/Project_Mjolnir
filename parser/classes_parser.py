from parser.base_parser import BaseParser
from utils.text_cleaner import TextCleaner
import re

class ClassesParser(BaseParser):
    def parse(self):
        text_list = self.load_text()
        blocks = self.split_blocks(text_list)

        for block in blocks:
            cls = self.extract_class(block)
            if cls:
                self.data.append(cls)

        return {'table': 'classes', 'records': self.data}

    def extract_class(self, block_text):
        lines = block_text.split("\n")
        if len(lines) < 5:
            return None  # Too little information

        cls = {
            'name': None,
            'type': 'Base',  # Default, can flip to Prestige
            'hit_die': None,
            'skill_points': None,
            'class_skills': None,
            'armor_proficiencies': None,
            'weapon_proficiencies': None,
            'prerequisites': None,
            'spellcasting': False,
            'features': [],
            'level_progression': [],
            'source': None
        }

        cls['name'] = lines[0].strip()

        # Detect if Prestige Class or Variant
        full_block = "\n".join(lines).lower()
        if "prerequisites" in full_block:
            cls['type'] = "Prestige"
        if "variant" in full_block or "class feature variants" in full_block:
            cls['type'] = "Variant"

        for i, line in enumerate(lines):
            clean_line = TextCleaner.clean_text(line)

            if "Hit Die:" in clean_line:
                cls['hit_die'] = clean_line.split(":", 1)[-1].strip()

            elif "Skill Points at" in clean_line:
                cls['skill_points'] = clean_line.split(":", 1)[-1].strip()

            elif "Class Skills:" in clean_line:
                cls['class_skills'] = clean_line.split(":", 1)[-1].strip()

            elif "Armor Proficiencies:" in clean_line or "Armor/Shield Proficiencies:" in clean_line:
                cls['armor_proficiencies'] = clean_line.split(":", 1)[-1].strip()

            elif "Weapon Proficiencies:" in clean_line:
                cls['weapon_proficiencies'] = clean_line.split(":", 1)[-1].strip()

            elif "Prerequisites:" in clean_line and cls['type'] == "Prestige":
                prereq_lines = [clean_line]
                # Read multiline prerequisites
                for j in range(i + 1, len(lines)):
                    next_line = TextCleaner.clean_text(lines[j])
                    if next_line and not next_line.endswith(":"):
                        prereq_lines.append(next_line)
                    else:
                        break
                cls['prerequisites'] = " ".join(prereq_lines).split(":", 1)[-1].strip()

        # Extract Features and Table separately
        cls['features'] = self.extract_features(full_block)
        cls['level_progression'] = self.extract_level_table(full_block)

        # Spellcasting detection
        if "spells per day" in full_block or "spells known" in full_block:
            cls['spellcasting'] = True

        return cls

    def extract_features(self, full_block):
        features = []
        feature_sections = re.split(r"\b(Class Features|Features|Abilities)\b", full_block, flags=re.IGNORECASE)
        if len(feature_sections) > 2:
            features_block = feature_sections[2]

            feature_list = re.split(r"(?=\n[A-Z][a-z]+\s[A-Z][a-z]+|\n[A-Z]{2,})", features_block)
            for feature in feature_list:
                feature = feature.strip()
                if not feature:
                    continue

                # Detect weird system mentions
                feature_type = "standard"
                lowered = feature.lower()
                if any(keyword in lowered for keyword in ['vestige', 'soulmeld', 'mystery', 'power point', 'maneuver']):
                    feature_type = "special"

                features.append({
                    'name': feature.split("\n")[0],
                    'description': feature,
                    'feature_type': feature_type
                })

        return features

    def extract_level_table(self, full_block):
        # Very basic table grabber for now
        table = []
        lines = full_block.split("\n")
        start = False
        for line in lines:
            clean_line = TextCleaner.clean_text(line)
            if re.search(r"\bLevel\b", clean_line) and re.search(r"\bBAB\b", clean_line):
                start = True
                continue
            if start:
                if clean_line.strip() == "":
                    break
                row = [cell.strip() for cell in clean_line.split("\t") if cell.strip()]
                if len(row) >= 4:
                    table.append(row)

        return table
