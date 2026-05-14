# =========================================================
# COFFEE SHOP SALES DATA CLEANING & TRANSFORMATION PROJECT
# =========================================================

# -----------------------------
# STEP 1 - IMPORT LIBRARIES
# -----------------------------

# Pandas is used for data analysis and cleaning
import pandas as pd

# Matplotlib is used for visualization
import matplotlib.pyplot as plt


# -----------------------------
# STEP 2 - LOAD DATASETS
# -----------------------------

# Load first dataset
df1 = pd.read_csv(r"X:\Apex\archive\index_1.csv")

# Load second dataset
df2 = pd.read_csv(r"X:\Apex\archive\index_2.csv")


# -----------------------------
# STEP 3 - PREVIEW DATA
# -----------------------------

# Display first 5 rows of dataset 1
print("FIRST 5 ROWS OF DATASET 1")
print(df1.head())

# Display first 5 rows of dataset 2
print("\nFIRST 5 ROWS OF DATASET 2")
print(df2.head())


# -----------------------------
# STEP 4 - DATASET INFORMATION
# -----------------------------

# Display structure of dataset 1
print("\nDATASET 1 INFO")
print(df1.info())

# Display structure of dataset 2
print("\nDATASET 2 INFO")
print(df2.info())


# -----------------------------
# STEP 5 - CHECK MISSING VALUES
# -----------------------------

# Count missing values in dataset 1
print("\nMISSING VALUES IN DATASET 1")
print(df1.isnull().sum())

# Count missing values in dataset 2
print("\nMISSING VALUES IN DATASET 2")
print(df2.isnull().sum())


# -----------------------------
# STEP 6 - CHECK DUPLICATES
# -----------------------------

# Count duplicate rows in dataset 1
print("\nDUPLICATES IN DATASET 1")
print(df1.duplicated().sum())

# Count duplicate rows in dataset 2
print("\nDUPLICATES IN DATASET 2")
print(df2.duplicated().sum())


# -----------------------------
# STEP 7 - REMOVE DUPLICATES
# -----------------------------

# Remove duplicate rows from dataset 1
df1 = df1.drop_duplicates()

# Remove duplicate rows from dataset 2
df2 = df2.drop_duplicates()


# -----------------------------
# STEP 8 - CONVERT DATE FORMAT
# -----------------------------

# Convert 'date' column into datetime format
df1["date"] = pd.to_datetime(df1["date"])

# Convert 'datetime' column into datetime format
df1["datetime"] = pd.to_datetime(df1["datetime"])

# Same conversion for dataset 2
df2["date"] = pd.to_datetime(df2["date"])
df2["datetime"] = pd.to_datetime(df2["datetime"])


# -----------------------------
# STEP 9 - CLEAN TEXT FORMATTING
# -----------------------------

# Standardize coffee names by capitalizing properly
df1["coffee_name"] = df1["coffee_name"].str.title()

# Same for dataset 2
df2["coffee_name"] = df2["coffee_name"].str.title()


# -----------------------------
# STEP 10 - FEATURE ENGINEERING
# -----------------------------

# Create new column 'hour' from datetime
df1["hour"] = df1["datetime"].dt.hour

# Same for dataset 2
df2["hour"] = df2["datetime"].dt.hour


# Create new column 'day_name'
df1["day_name"] = df1["date"].dt.day_name()

# Same for dataset 2
df2["day_name"] = df2["date"].dt.day_name()


# -----------------------------
# STEP 11 - PRICE CATEGORY
# -----------------------------

# Categorize transaction amount into High or Low
df1["price_category"] = df1["money"].apply(
    lambda x: "High" if x > 30 else "Low"
)

# Same for dataset 2
df2["price_category"] = df2["money"].apply(
    lambda x: "High" if x > 30 else "Low"
)


# -----------------------------
# STEP 12 - HANDLE MISSING COLUMN
# -----------------------------

# Dataset 2 does not contain 'card' column
# So we create it manually
df2["card"] = "Not Available"


# -----------------------------
# STEP 13 - MERGE DATASETS
# -----------------------------

# Combine both datasets into one final dataset
final_df = pd.concat([df1, df2], ignore_index=True)


# -----------------------------
# STEP 14 - FINAL DATASET INFO
# -----------------------------

# Display information about cleaned dataset
print("\nFINAL CLEANED DATASET INFO")
print(final_df.info())


# -----------------------------
# STEP 15 - DESCRIPTIVE STATISTICS
# -----------------------------

# Show statistical summary
print("\nSTATISTICAL SUMMARY")
print(final_df.describe())


# -----------------------------
# STEP 16 - OUTLIER DETECTION
# -----------------------------

# Create boxplot to detect outliers in money column
plt.boxplot(final_df["money"])

# Add title
plt.title("Transaction Amount Outliers")

# Show graph
plt.show()


# -----------------------------
# STEP 17 - SAVE CLEANED DATASET
# -----------------------------

# Save cleaned dataset into CSV file
final_df.to_csv(
    r"X:\Apex\archive\cleaned_coffee_sales.csv",
    index=False
)


# -----------------------------
# STEP 18 - SUCCESS MESSAGE
# -----------------------------

print("\nDATA CLEANING COMPLETED SUCCESSFULLY!")
print("Cleaned dataset saved as 'cleaned_coffee_sales.csv'")