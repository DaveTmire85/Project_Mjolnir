-- Project Mjölnir: Full Database Schema (v2.1.0)

-- ==========================
-- DEITIES
-- ==========================
CREATE TABLE deities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    reference TEXT,
    pantheon TEXT,
    alignment TEXT,
    rank TEXT,
    nickname_portfolio TEXT,
    domains TEXT,
    favored_weapon TEXT,
    symbol TEXT
);

-- ==========================
-- FEATS
-- ==========================
CREATE TABLE feats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    type TEXT,
    prerequisite TEXT,
    benefit TEXT,
    source TEXT
);

-- ==========================
-- CLASSES (Base and Prestige)
-- ==========================
CREATE TABLE classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    hit_die TEXT,
    alignment TEXT,
    skill_points TEXT,
    class_skills TEXT,
    weapon_armor_proficiencies TEXT,
    class_features TEXT
);

-- ==========================
-- RACES
-- ==========================
CREATE TABLE races (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    ability_modifiers TEXT,
    favored_class TEXT,
    size TEXT,
    movement TEXT,
    vision TEXT,
    level_adjustment TEXT,
    features TEXT
);

-- ==========================
-- CREATURES (Mounts, Familiars, Companions)
-- ==========================
CREATE TABLE creatures (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    type TEXT,
    size TEXT,
    hit_dice TEXT,
    alignment TEXT,
    special_traits TEXT
);

-- ==========================
-- EQUIPMENT (Armor and Shields)
-- ==========================
CREATE TABLE equipment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    armor_bonus TEXT,
    max_dex_bonus TEXT,
    armor_check_penalty TEXT,
    arcane_spell_failure TEXT,
    cost TEXT,
    weight TEXT
);

-- ==========================
-- MAGIC ITEMS
-- ==========================
CREATE TABLE magic_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    aura TEXT,
    caster_level TEXT,
    requirements TEXT,
    cost TEXT,
    weight TEXT
);

-- ==========================
-- SKILLS
-- ==========================
CREATE TABLE skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    ability TEXT,
    trained_only TEXT,
    armor_check_penalty TEXT,
    synergy TEXT,
    special TEXT
);

-- ==========================
-- COMBAT ACTIONS
-- ==========================
CREATE TABLE combat_actions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    attack_roll TEXT,
    steps TEXT,
    feats_affecting TEXT,
    special_modifiers TEXT
);

-- ==========================
-- TEMPLATES
-- ==========================
CREATE TABLE templates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    source TEXT,
    creature_type_change TEXT,
    natural_armor_bonus TEXT,
    ability_changes TEXT,
    level_adjustment TEXT,
    challenge_rating_change TEXT,
    immunities TEXT
);

-- ==========================
-- SPELLS
-- ==========================
CREATE TABLE spells (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    classes TEXT,
    domains TEXT,
    sourcebooks TEXT,
    school TEXT,
    subschool TEXT,
    descriptors TEXT,
    components TEXT,
    casting_time TEXT,
    range TEXT,
    target TEXT,
    duration TEXT,
    saving_throw TEXT,
    spell_resistance TEXT,
    description TEXT,
    special_requirements TEXT
);
