# =====================================================
# COFFEE SHOP SALES EDA PROJECT
# =====================================================

# -----------------------------
# IMPORT LIBRARIES
# -----------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# LOAD CLEANED DATASET
# -----------------------------

df = pd.read_csv(r"X:\Apex\archive\cleaned_coffee_sales.csv")

# -----------------------------
# SHOW FIRST 5 ROWS
# -----------------------------

print(df.head())

# -----------------------------
# DESCRIPTIVE STATISTICS
# -----------------------------

print("\nDATASET STATISTICS")
print(df.describe())

# -----------------------------
# CHECK MOST POPULAR COFFEE
# -----------------------------

print("\nCOFFEE SALES COUNT")
print(df["coffee_name"].value_counts())

# -----------------------------
# CHECK PAYMENT METHODS
# -----------------------------

print("\nPAYMENT METHOD COUNT")
print(df["cash_type"].value_counts())

# -----------------------------
# HISTOGRAM
# -----------------------------

# Shows transaction amount distribution

plt.figure(figsize=(8,5))

plt.hist(df["money"], bins=20)

plt.title("Transaction Amount Distribution")
plt.xlabel("Money")
plt.ylabel("Frequency")

plt.show()

# -----------------------------
# BAR CHART
# -----------------------------

# Shows coffee popularity

coffee_counts = df["coffee_name"].value_counts()

plt.figure(figsize=(10,5))

coffee_counts.plot(kind="bar")

plt.title("Most Popular Coffee")
plt.xlabel("Coffee Name")
plt.ylabel("Total Orders")

plt.show()

# -----------------------------
# SCATTER PLOT
# -----------------------------

# Relationship between hour and money

plt.figure(figsize=(8,5))

plt.scatter(df["hour"], df["money"])

plt.title("Hour vs Transaction Amount")
plt.xlabel("Hour")
plt.ylabel("Money")

plt.show()

# -----------------------------
# HEATMAP
# -----------------------------

# Correlation between numerical columns

numeric_df = df.select_dtypes(include=['number'])

correlation = numeric_df.corr()

plt.figure(figsize=(8,6))

sns.heatmap(correlation, annot=True)

plt.title("Correlation Heatmap")

plt.show()

# -----------------------------
# MONTHLY SALES
# -----------------------------

# Convert date column

df["date"] = pd.to_datetime(df["date"])

# Create month column

df["month"] = df["date"].dt.month_name()

# Monthly revenue

monthly_sales = df.groupby("month")["money"].sum()

plt.figure(figsize=(10,5))

monthly_sales.plot(kind="bar")

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.show()

# -----------------------------
# TOP PRODUCTS BY REVENUE
# -----------------------------

top_products = df.groupby("coffee_name")["money"].sum()

print("\nTOP PRODUCTS BY REVENUE")

print(top_products.sort_values(ascending=False))

# -----------------------------
# SUCCESS MESSAGE
# -----------------------------

print("\nEDA COMPLETED SUCCESSFULLY!")