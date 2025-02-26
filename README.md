# 📌 Automating Data Cleaning

## 📖 Project Overview
This project automates the process of cleaning raw CSV data through a series of sequentially executed Python scripts. The workflow includes **ingesting data, removing duplicates, handling missing values, standardizing column names, and saving the final cleaned data**.

## 📂 Folder Structure
```
data_cleaning_project/
├── main.py                # Runs all scripts in order
├── scripts/               # Stores all cleaning scripts
│   ├── step1_ingest.py
│   ├── step2_deduplicate.py
│   ├── step3_missing_values.py
│   ├── step4_standardize_columns.py
│   ├── step5_save.py
├── data/                  # Stores input & output files
│   ├── raw_data.csv       
│   ├── cleaned_data.csv   
├── README.md              # Project documentation
```

## 🚀 How to Use
### **1️⃣ Install Dependencies**
Make sure you have Python installed. Then, install the required libraries:
```bash
pip install pandas
```

### **2️⃣ Run the Project**
Execute the **main.py** script to run all cleaning steps automatically:
```bash
python main.py
```

### **3️⃣ Process Steps**
1. **Ingest Data** – The user selects a CSV file.
2. **Remove Duplicates** – Drops duplicate rows.
3. **Handle Missing Values** – Fills missing numeric values with the mean and text values with 'Unknown'.
4. **Standardize Column Names** – Converts column names to lowercase and replaces spaces with underscores.
5. **Save Cleaned Data** – Saves the final cleaned CSV file.

## 📜 License
This project is licensed under the Apache License 2.0.

---
🔹 **Happy Cleaning~** 🎉

