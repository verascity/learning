--Do you need a GROUP BY for the below problems or can you solve them another way?
 --Which account placed the earliest order?

SELECT a.name,
       o.occurred_at
FROM accounts a
JOIN orders o ON a.id = o.account_id
ORDER BY o.occurred_at
LIMIT 1;

--Find the total sales in USD for each account. Order starting with the largest totals.

SELECT a.name,
       SUM(o.total_amt_usd) totals
FROM accounts a
JOIN orders o ON a.id = o.account_id
GROUP BY a.name
ORDER BY totals DESC;

--Via what channel did the earliest web event occur, and which account was associated?

SELECT a.name,
       w.occurred_at,
       w.channel
FROM accounts a
JOIN web_events w ON a.id = w.account_id
ORDER BY w.occurred_at
LIMIT 1;

--Find the total number of times each channel was used.

SELECT channel,
       COUNT(*) count
FROM web_events
GROUP BY channel;

--Who is the primary contact associated with the earliest web event?

SELECT a.primary_poc,
       w.occurred_at
FROM web_events w
JOIN accounts a ON w.account_id = a.id
ORDER BY w.occurred_at
LIMIT 1;

--What was the smallest order placed by each account in USD? Order from smallest to largest.

SELECT a.name,
       MIN(o.total_amt_usd) smallest_order
FROM accounts a
JOIN orders o ON a.id = o.account_id
GROUP BY a.name
ORDER BY smallest_order;

--Find the number of sales reps in each region. Order from fewest to most.

SELECT r.name,
       COUNT(s.name) reps
FROM region r
JOIN sales_reps s ON r.id = s.region_id
GROUP BY r.name
ORDER BY reps;

