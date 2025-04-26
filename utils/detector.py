from utils.detector_helper import load_text_for_detection

def detect_entity(text_list):
    # Scan the first 200 lines (paragraphs + table cells)
    scan_text = "\n".join(text_list[:200]).lower()

    if "pantheon:" in scan_text and "domains:" in scan_text:
        return "deities"
    elif "prerequisite:" in scan_text and "benefit:" in scan_text:
        return "feats"
    elif "school:" in scan_text and "casting time:" in scan_text:
        return "spells"
    elif "damage:" in scan_text and ("armor bonus:" in scan_text or "critical:" in scan_text):
        return "equipment"
    elif "aura:" in scan_text and "caster level:" in scan_text and "slot:" in scan_text:
        return "magic_items"
    elif "type:" in scan_text and "size:" in scan_text and "abilities:" in scan_text:
        return "races"
    elif "hit die:" in scan_text and "class skills" in scan_text:
        return "classes"
    elif "hit dice:" in scan_text and "initiative:" in scan_text and "armor class:" in scan_text:
        return "monsters"
    elif "level adjustment:" in scan_text and "challenge rating:" in scan_text:
        return "templates"
    else:
        return "unknown"
