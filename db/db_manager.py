import sqlite3
import os

class DBManager:
    def __init__(self, db_path="db/mjolnir.db"):
        self.db_path = db_path
        self.ensure_db_exists()

    def ensure_db_exists(self):
        if not os.path.exists(self.db_path):
            print("[!] Database not found. Creating a new one...")
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
            
            with sqlite3.connect(self.db_path) as conn:
                schema_path = os.path.join('db', 'schema.sql')
                if os.path.exists(schema_path):
                    with open(schema_path, 'r') as f:
                        schema_script = f.read()
                    conn.executescript(schema_script)
                    print("[+] New database created successfully.")
                else:
                    print(f"[!] Schema file not found at {schema_path}. Cannot initialize database.")
                    raise SystemExit(1)

    def connect(self):
        return sqlite3.connect(self.db_path)

    def insert(self, table, records):
        if not records:
            return

        with self.connect() as conn:
            cursor = conn.cursor()

            columns = list(records[0].keys())
            placeholders = ','.join(['?' for _ in columns])
            query = f"INSERT INTO {table} ({','.join(columns)}) VALUES ({placeholders})"

            data = [tuple(record.get(col, None) for col in columns) for record in records]

            try:
                cursor.executemany(query, data)
                conn.commit()
                print(f"[+] Inserted {len(records)} records into {table}")
            except Exception as e:
                print(f"[!] Failed to insert records into {table}: {e}")

                
# Quick shortcut for existing parsers expecting insert_entry
def insert_entry(table, entry):
    db = DBManager()
    db.insert(table, [entry])
