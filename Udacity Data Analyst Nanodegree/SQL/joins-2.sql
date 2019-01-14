--Find all accounts and sales reps in the Midwest region.

SELECT r.name AS region,
       s.name AS rep,
       a.name AS account
FROM region AS r
JOIN sales_reps AS s ON s.region_id = r.id
JOIN accounts AS a ON a.sales_rep_id = s.id
WHERE r.name = 'Midwest'
ORDER BY a.name;

--Find all accounts and sales reps in the Midwest region who have a sales rep starting with "S."

SELECT r.name AS region,
       s.name AS rep,
       a.name AS account
FROM region AS r
JOIN sales_reps AS s ON s.region_id = r.id
JOIN accounts AS a ON a.sales_rep_id = s.id
WHERE r.name = 'Midwest'
  AND s.name LIKE 'S%'
ORDER BY a.name;

--Find all accounts and sales reps in the Midwest region who have a sales rep whose last name starts with "K."

SELECT r.name AS region,
       s.name AS rep,
       a.name AS account
FROM region AS r
JOIN sales_reps AS s ON s.region_id = r.id
JOIN accounts AS a ON a.sales_rep_id = s.id
WHERE r.name = 'Midwest'
  AND s.name = '% K%'
ORDER BY a.name;

--Find all regions, account names, and unit prices (plus one cent to avoid zero division error) for orders of standard over 100 units.

SELECT r.name AS region,
       a.name AS account,
       o.total_amt_usd/(o.total+0.01) AS unit_price
FROM region AS r
JOIN sales_reps AS s ON r.id = s.region_id
JOIN accounts AS a ON s.id = a.sales_rep_id
JOIN orders AS o ON a.id = o.account_id
WHERE o.standard_qty > 100;

--Find all regions, account names, and unit prices (plus one cent to avoid zero division error) for orders of standard over 100 units and poster over 50 units. Start with the smallest orders.

SELECT r.name AS region,
       a.name AS account,
       o.total_amt_usd/(o.total+0.01) AS unit_price
FROM region AS r
JOIN sales_reps AS s ON r.id = s.region_id
JOIN accounts AS a ON s.id = a.sales_rep_id
JOIN orders AS o ON a.id = o.account_id
WHERE o.standard_qty > 100
  AND poster_qty > 50
ORDER BY o.total_amt_usd;

--Find all regions, account names, and unit prices (plus one cent to avoid zero division error) for orders of standard over 100 units and poster over 50 units. Start with the largest orders.

SELECT r.name AS region,
       a.name AS account,
       o.total_amt_usd/(o.total+0.01) AS unit_price
FROM region AS r
JOIN sales_reps AS s ON r.id = s.region_id
JOIN accounts AS a ON s.id = a.sales_rep_id
JOIN orders AS o ON a.id = o.account_id
WHERE o.standard_qty > 100
  AND poster_qty > 50
ORDER BY o.total_amt_usd DESC;

--Find all distinct channels for account #1001.

SELECT DISTINCT a.name,
                w.channel
FROM accounts AS a
JOIN web_events AS w ON a.id = w.account_id
WHERE a.id = 1001;

--Find all account names, total sales quantity, and total sales dollars for the year 2015, starting with the last sale.

SELECT w.occurred_at,
       a.name,
       o.total,
       o.total_amt_usd
FROM accounts AS a
JOIN web_events AS w ON a.id = w.account_id
JOIN orders AS o ON a.id = o.account_id
WHERE o.occurred_at BETWEEN '2015-01-01' AND '2016-01-01'
ORDER BY o.occurred_at DESC;