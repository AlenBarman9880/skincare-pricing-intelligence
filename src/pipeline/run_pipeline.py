import subprocess
import sys

subprocess.run([sys.executable, "src/scraper/nykaa_scraper.py"])
subprocess.run([sys.executable, "src/processing/clean_data.py"])
subprocess.run([sys.executable, "src/database/load_to_postgres.py"])

print("Pipeline executed successfully!")