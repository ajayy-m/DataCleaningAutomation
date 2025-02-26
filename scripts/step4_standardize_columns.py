import pandas as pd

def standardize_column_names():
    try:
        df = pd.read_csv("data/data_stage3.csv")

        # Standardize column names
        df.columns = df.columns.str.lower().str.replace(" ", "_")

        # Save output
        df.to_csv("data/data_stage4.csv", index=False)

        print("Step 4: Column names standardized ✅")

    except FileNotFoundError:
        print("Error: data_stage3.csv not found. Run step3_missing_values.py first.")

if __name__ == "__main__":
    standardize_column_names()
