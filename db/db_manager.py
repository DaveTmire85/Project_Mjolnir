import sqlite3
from config.settings import Config

class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect(Config.DATABASE_PATH)
        self.cursor = self.conn.cursor()
        self.initialize_schema()

    def initialize_schema(self):
        with open('db/schema.sql', 'r') as f:
            schema_sql = f.read()
        self.conn.executescript(schema_sql)
        self.conn.commit()

    def insert(self, parsed_data):
        if not parsed_data or 'table' not in parsed_data or 'records' not in parsed_data:
            print("[!] Invalid parsed data format.")
            return

        table = parsed_data['table']
        records = parsed_data['records']

        for record in records:
            keys = record.keys()
            placeholders = ", ".join(["?"] * len(keys))
            columns = ", ".join(keys)
            sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

            try:
                self.cursor.execute(sql, tuple(record.values()))
                self.conn.commit()
                print(f"[+] Inserted into {table}: {record.get('name', '[Unnamed Record]')}")
            except sqlite3.Error as e:
                print(f"[!] DB insert error in table {table}: {e}")

    def close(self):
        self.conn.close()
