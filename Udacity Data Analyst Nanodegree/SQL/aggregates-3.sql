--Which sales reps have more than five accounts?

SELECT s.name rep,
       COUNT(a.name) num_accounts
FROM accounts a
JOIN sales_reps s ON a.sales_rep_id = s.id
GROUP BY 1
HAVING COUNT(a.name) > 5;

--Which accounts have more than 20 orders?

SELECT a.name,
       COUNT(*) num_orders
FROM orders o
JOIN accounts a ON o.account_id = a.id
GROUP BY 1
HAVING COUNT(*) > 20;

--Which accounts spent more than 30,000 across all orders?

SELECT a.name,
       SUM(o.total_amt_usd) total
FROM orders o
JOIN accounts a ON o.account_id = a.id
GROUP BY 1
HAVING SUM(o.total_amt_usd) > 30000;

--Which accounts spent less than 1,000 across all orders?

SELECT a.name,
       SUM(o.total_amt_usd) total
FROM orders o
JOIN accounts a ON o.account_id = a.id
GROUP BY 1
HAVING SUM(o.total_amt_usd) < 1000;

--Which accounts used facebook as a channel more than six times?

SELECT a.name,
       w.channel,
       COUNT(w.channel) use_of_channel
FROM accounts a
JOIN web_events w ON a.id = w.account_id
GROUP BY a.name,
         w.channel
HAVING COUNT(w.channel) > 6
AND w.channel = 'facebook'
ORDER BY use_of_channel;