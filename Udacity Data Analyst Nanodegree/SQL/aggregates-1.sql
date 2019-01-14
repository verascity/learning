--Find the total number of poster sales.

SELECT SUM(poster_qty) AS total_poster_sales
FROM orders;

--Find the total number of standard sales.

SELECT SUM(standard_qty) AS total_standard_sales
FROM orders;

--Find the total income from all sales.

SELECT SUM(total_amt_usd) AS total_sales
FROM orders;

--Find the total income from standard and gloss sales.

SELECT SUM(standard_amt_usd) AS standard,
       SUM(gloss_amt_usd) AS gloss
FROM orders;

--Find the unit price for standard using aggregates.

SELECT SUM(standard_amt_usd)/SUM(standard_qty) AS unit_price
FROM orders;