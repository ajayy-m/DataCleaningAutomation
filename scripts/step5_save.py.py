import pandas as pd

def save_final_data():
    try:
        df = pd.read_csv("data/data_stage4.csv")

        # Save final cleaned data
        df.to_csv("data/cleaned_data.csv", index=False)

        print("Step 5: Final cleaned data saved ✅")
        print("Data cleaning process completed successfully! 🎉")

    except FileNotFoundError:
        print("Error: data_stage4.csv not found. Run step4_standardize_columns.py first.")

if __name__ == "__main__":
    save_final_data()
