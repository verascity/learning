--How many GROUP BYs do you need for the problems below?
 --Find the average quantity for each type for each account.

SELECT a.name,
       AVG(o.standard_qty) standard,
       AVG(o.gloss_qty) gloss,
       AVG(o.poster_qty) poster
FROM orders o
JOIN accounts a ON o.account_id = a.id
GROUP BY a.name;

--Find the average total in USD for each type for each account.

SELECT a.name,
       AVG(o.standard_amt_usd) standard,
       AVG(o.gloss_amt_usd) gloss,
       AVG(poster_amt_usd) poster
FROM accounts a
JOIN orders o ON a.id = o.account_id
GROUP BY a.name;

--Find the number of times each channel was used in the web_events table for each sales rep.

SELECT s.name,
       w.channel,
       COUNT(*) EVENTS
FROM web_events w
JOIN accounts a ON a.id = w.account_id
JOIN sales_reps s ON a.sales_rep_id = s.id
GROUP BY s.name,
         w.channel
ORDER BY EVENTS DESC;

--Find the number of times each channel was used in the web_events table for each region.

SELECT r.name,
       w.channel,
       COUNT(*) EVENTS
FROM region r
JOIN sales_reps s ON r.id = s.region_id
JOIN accounts a ON a.sales_rep_id = s.id
JOIN web_events w ON a.id = w.account_id
GROUP BY r.name,
         w.channel
ORDER BY EVENTS DESC;