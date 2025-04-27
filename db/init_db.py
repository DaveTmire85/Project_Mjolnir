import sqlite3
import os

def init_database(db_path="db/mjolnir.db"):
    """Initialize the database from schema.sql"""
    
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    with open('db/schema.sql', 'r') as f:
        schema_script = f.read()
    
    cursor.executescript(schema_script)
    
    conn.commit()
    conn.close()
    
    print(f"[+] Your database has been initialized successfully at {db_path}")

if __name__ == "__main__":
    init_database()
