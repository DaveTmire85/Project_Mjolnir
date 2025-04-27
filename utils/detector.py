from utils.detector_helper import contains_keywords

def detect_parser(text_lines):
    """
    Given a list of text lines, returns the parser type as a string.
    """

    joined_text = " ".join(text_lines).lower()

    detection_map = {
        'classes': ['hit die', 'class features', 'alignment'],
        'feats': ['prerequisite', 'benefit', 'feat type'],
        'races': ['ability modifiers', 'favored class', 'movement'],
        'creatures': ['mounts', 'companions', 'trainable creatures'],
        'equipment': ['armor bonus', 'armor check penalty', 'arcane spell failure'],
        'magic_items': ['aura', 'caster level', 'requirements', 'gp cost'],
        'skills': ['trained only', 'armor check penalty', 'synergy'],
        'combat_actions': ['opposed rolls', 'special modifiers'],
        'templates': ['template', 'level adjustment', 'challenge rating'],
        'deities': ['pantheon', 'domains', 'favored weapon'],
        'spells': ['spell descriptions', 'casting time', 'saving throw']
    }

    for parser_type, keywords in detection_map.items():
        if contains_keywords(joined_text, keywords):
            return parser_type

    return None
