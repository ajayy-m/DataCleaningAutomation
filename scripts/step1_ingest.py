import pandas as pd
import tkinter as tk
from tkinter import filedialog

def load_data():
    # Open a file selection dialog
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title="Select a CSV file", filetypes=[("CSV files", "*.csv")])

    if not file_path:
        print("No file selected. Exiting...")
        return

    print(f"Selected file: {file_path}")

    # Load CSV file
    df = pd.read_csv(file_path)
    
    # Save intermediate output in the data folder
    df.to_csv("data/data_stage1.csv", index=False)

    print("Step 1: Data Ingestion Complete ✅")

if __name__ == "__main__":
    load_data()
