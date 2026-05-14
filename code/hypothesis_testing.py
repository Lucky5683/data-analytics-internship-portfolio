# =====================================================
# HYPOTHESIS TESTING
# =====================================================

# Import libraries

import pandas as pd
from scipy.stats import ttest_ind

# -------------------------------------------------
# LOAD DATASET
# -------------------------------------------------

df = pd.read_csv(r"X:\Apex\archive\segmented_coffee_sales.csv")

# -------------------------------------------------
# SELECT CUSTOMER GROUPS
# -------------------------------------------------

high_value = df[df["customer_segment"] == "High Value"]["money"]

low_value = df[df["customer_segment"] == "Low Value"]["money"]

# -------------------------------------------------
# PERFORM T-TEST
# -------------------------------------------------

t_stat, p_value = ttest_ind(high_value, low_value)

# -------------------------------------------------
# PRINT RESULTS
# -------------------------------------------------

print("\nHYPOTHESIS TESTING RESULTS\n")

print("T-Statistic:", t_stat)

print("P-Value:", p_value)

# -------------------------------------------------
# INTERPRETATION
# -------------------------------------------------

if p_value < 0.05:

    print("\nResult: Statistically Significant Difference Found")

else:

    print("\nResult: No Statistically Significant Difference Found")