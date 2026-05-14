import pandas as pd
import sqlite3

# Load dataset
df = pd.read_csv(r"X:\Apex\archive\cleaned_coffee_sales.csv")

# Create database connection
conn = sqlite3.connect("coffee_sales.db")

# Convert dataframe into SQL table
df.to_sql(
    "coffee_sales",
    conn,
    if_exists="replace",
    index=False
)

# SQL Query
query = '''

SELECT coffee_name,
SUM(money) AS revenue

FROM coffee_sales

GROUP BY coffee_name

ORDER BY revenue DESC

LIMIT 5

'''

# Execute query
result = pd.read_sql(query, conn)

# Print output
print("\nTOP 5 PRODUCTS BY REVENUE\n")

print(result)

# Close database
conn.close()