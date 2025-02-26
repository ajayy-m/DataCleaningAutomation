import subprocess

scripts = [
    "scripts/step1_ingest.py",
    "scripts/step2_deduplicate.py",
    "scripts/step3_missing_values.py",
    "scripts/step4_standardize_columns.py",
    "scripts/step5_save.py"
]

for script in scripts:
    print(f"Running {script}...")
    subprocess.run(["python", script])  # Executes each script
