# =====================================================
# COFFEE SHOP KPI DASHBOARD
# =====================================================

# -----------------------------
# IMPORT LIBRARIES
# -----------------------------

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# LOAD CLEANED DATASET
# -----------------------------

df = pd.read_csv(r"X:\Apex\archive\cleaned_coffee_sales.csv")

# -----------------------------
# CALCULATE KPIs
# -----------------------------

# Total revenue
total_revenue = df["money"].sum()

# Total transactions
total_transactions = len(df)

# Top coffee product
top_product = df["coffee_name"].value_counts().idxmax()

# Peak sales hour
peak_hour = df.groupby("hour")["money"].sum().idxmax()

# Most used payment method
payment_method = df["cash_type"].value_counts().idxmax()

# -----------------------------
# CREATE DASHBOARD
# -----------------------------

fig = plt.figure(figsize=(14,8))

# Dashboard title
plt.suptitle(
    "Coffee Shop KPI Dashboard",
    fontsize=20,
    fontweight='bold'
)

# KPI BOX 1
plt.text(
    0.1,
    0.8,
    f"TOTAL REVENUE\n₹ {total_revenue:.2f}",
    fontsize=16,
    bbox=dict(facecolor='lightblue', edgecolor='black')
)

# KPI BOX 2
plt.text(
    0.4,
    0.8,
    f"TOTAL TRANSACTIONS\n{total_transactions}",
    fontsize=16,
    bbox=dict(facecolor='lightgreen', edgecolor='black')
)

# KPI BOX 3
plt.text(
    0.7,
    0.8,
    f"TOP PRODUCT\n{top_product}",
    fontsize=16,
    bbox=dict(facecolor='orange', edgecolor='black')
)

# KPI BOX 4
plt.text(
    0.1,
    0.5,
    f"PEAK SALES HOUR\n{peak_hour}:00",
    fontsize=16,
    bbox=dict(facecolor='pink', edgecolor='black')
)

# KPI BOX 5
plt.text(
    0.4,
    0.5,
    f"PAYMENT METHOD\n{payment_method}",
    fontsize=16,
    bbox=dict(facecolor='yellow', edgecolor='black')
)

# Remove axes
plt.axis('off')

# Save dashboard image
plt.savefig(
    r"X:\Apex\archive\dashboard_mockup.png",
    bbox_inches='tight'
)

# Show dashboard
plt.show()

# Success message
print("\nDASHBOARD CREATED SUCCESSFULLY!")