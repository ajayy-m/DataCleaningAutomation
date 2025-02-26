import pandas as pd

def remove_duplicates():
    try:
        df = pd.read_csv("data/data_stage1.csv")

        # Remove duplicate rows
        df_cleaned = df.drop_duplicates()

        # Save output
        df_cleaned.to_csv("data/data_stage2.csv", index=False)

        print("Step 2: Duplicates removed ✅")

    except FileNotFoundError:
        print("Error: data_stage1.csv not found. Run step1_ingest.py first.")

if __name__ == "__main__":
    remove_duplicates()
