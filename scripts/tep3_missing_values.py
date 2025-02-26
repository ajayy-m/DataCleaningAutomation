import pandas as pd

def handle_missing_values():
    try:
        df = pd.read_csv("data/data_stage2.csv")

        # Fill missing numerical values with column mean
        for col in df.select_dtypes(include=['number']).columns:
            df[col].fillna(df[col].mean(), inplace=True)

        # Fill missing categorical values with "Unknown"
        for col in df.select_dtypes(include=['object']).columns:
            df[col].fillna("Unknown", inplace=True)

        # Save output
        df.to_csv("data/data_stage3.csv", index=False)

        print("Step 3: Missing values handled ✅")

    except FileNotFoundError:
        print("Error: data_stage2.csv not found. Run step2_deduplicate.py first.")

if __name__ == "__main__":
    handle_missing_values()
