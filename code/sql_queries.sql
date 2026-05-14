-- 1. Top 5 coffee products by revenue

SELECT coffee_name,
SUM(money) AS total_revenue
FROM coffee_sales
GROUP BY coffee_name
ORDER BY total_revenue DESC
LIMIT 5;



-- 2. Total revenue by payment type

SELECT cash_type,
SUM(money) AS revenue
FROM coffee_sales
GROUP BY cash_type;



-- 3. Average transaction amount

SELECT AVG(money) AS average_transaction
FROM coffee_sales;



-- 4. Highest sales hour

SELECT hour,
SUM(money) AS total_sales
FROM coffee_sales
GROUP BY hour
ORDER BY total_sales DESC;



-- 5. Total transactions per coffee type

SELECT coffee_name,
COUNT(*) AS total_transactions
FROM coffee_sales
GROUP BY coffee_name
ORDER BY total_transactions DESC;



-- 6. Monthly revenue trend

SELECT MONTH(date) AS month,
SUM(money) AS monthly_revenue
FROM coffee_sales
GROUP BY month
ORDER BY month;



-- 7. Revenue by day of week

SELECT day_name,
SUM(money) AS revenue
FROM coffee_sales
GROUP BY day_name
ORDER BY revenue DESC;