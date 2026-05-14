# =====================================================
# CUSTOMER SEGMENTATION ANALYSIS
# =====================================================

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset

df = pd.read_csv(r"X:\Apex\archive\cleaned_coffee_sales.csv")

# -----------------------------
# CREATE CUSTOMER SEGMENTS
# -----------------------------

def segment_customer(amount):

    if amount >= 40:
        return "High Value"

    elif amount >= 20:
        return "Medium Value"

    else:
        return "Low Value"

# Apply segmentation

df["customer_segment"] = df["money"].apply(segment_customer)

# -----------------------------
# COUNT SEGMENTS
# -----------------------------

segment_counts = df["customer_segment"].value_counts()

print(segment_counts)

# -----------------------------
# VISUALIZE SEGMENTS
# -----------------------------

plt.figure(figsize=(8,5))

segment_counts.plot(kind="bar")

plt.title("Customer Segmentation")
plt.xlabel("Segment")
plt.ylabel("Total Transactions")

plt.show()

# -----------------------------
# SAVE DATASET
# -----------------------------

df.to_csv(
    r"X:\Apex\archive\segmented_coffee_sales.csv",
    index=False
)

print("\nSEGMENTATION COMPLETED!")