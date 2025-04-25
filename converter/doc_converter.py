import os
import subprocess
from config.settings import Config

class DocConverter:
    def __init__(self):
        os.makedirs(Config.CONVERTED_DIR, exist_ok=True)

    def convert(self, file_path):
        if not file_path.endswith('.doc'):
            return

        filename = os.path.basename(file_path)
        new_filename = os.path.splitext(filename)[0] + ".docx"
        output_path = os.path.join(Config.CONVERTED_DIR, new_filename)

        try:
            subprocess.run(
                ["soffice", "--headless", "--convert-to", "docx", "--outdir", Config.CONVERTED_DIR, file_path],
                check=True
            )
            print(f"[+] Converted: {filename} -> {new_filename}")
        except subprocess.CalledProcessError as e:
            print(f"[!] Failed to convert {file_path}: {e}")
