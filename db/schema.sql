-- Create tables for Project Mjolnir (D&D 3.5e Parser)

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS deities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    source TEXT,
    pantheon TEXT,
    alignment TEXT,
    domains TEXT,
    favored_weapon TEXT,
    symbol TEXT
);

CREATE TABLE IF NOT EXISTS feats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT,
    prerequisites TEXT,
    benefit TEXT,
    normal TEXT,
    special TEXT,
    source TEXT
);

CREATE TABLE IF NOT EXISTS spells (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    school TEXT,
    subschool TEXT,
    descriptors TEXT,
    level_by_class TEXT,
    components TEXT,
    casting_time TEXT,
    range TEXT,
    effect TEXT,
    duration TEXT,
    saving_throw TEXT,
    spell_resistance TEXT,
    source TEXT
);

CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT,
    subtype TEXT,
    cost TEXT,
    weight TEXT,
    properties TEXT,
    effect TEXT,
    source TEXT
);

CREATE TABLE IF NOT EXISTS races (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT,
    subtype TEXT,
    size TEXT,
    speed TEXT,
    ability_mods TEXT,
    traits TEXT,
    languages TEXT,
    source TEXT
);

CREATE TABLE IF NOT EXISTS classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    hit_die TEXT,
    bab_progression TEXT,
    saves TEXT,
    skill_points_per_level INTEGER,
    spellcasting TEXT,
    features TEXT,
    prerequisites TEXT,
    is_prestige INTEGER,
    source TEXT
);

CREATE TABLE IF NOT EXISTS monsters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT,
    subtype TEXT,
    size TEXT,
    hit_dice TEXT,
    initiative TEXT,
    speed TEXT,
    armor_class TEXT,
    base_attack_bonus TEXT,
    grapple_bonus TEXT,
    attack_routine TEXT,
    full_attack TEXT,
    special_attacks TEXT,
    special_qualities TEXT,
    saves TEXT,
    abilities TEXT,
    environment TEXT,
    organization TEXT,
    challenge_rating TEXT,
    treasure TEXT,
    alignment TEXT,
    advancement TEXT,
    level_adjustment TEXT,
    source TEXT
);

CREATE TABLE IF NOT EXISTS templates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    adjustments TEXT,
    prerequisites TEXT,
    type_change TEXT,
    la_adjustment TEXT,
    cr_adjustment TEXT,
    source TEXT
);
