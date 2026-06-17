import subprocess
import sys

scripts = [
    "src/scraper/nykaa_scraper.py",
    "src/processing/clean_data.py",
    "src/processing/normalize_prices.py",
    "src/processing/feature_engineering.py",
    "src/analysis/visualize.py",
    "src/database/load_to_postgres.py"
]

for script in scripts:
    print(f"\n{'='*60}")
    print(f"Running: {script}")
    print(f"{'='*60}")

    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        print(f"\n❌ Pipeline stopped because {script} failed.")
        sys.exit(1)

print("\n✅ Entire pipeline executed successfully!")