--Provide the name of the sales_rep in each region with the largest amount of total_amt_usd sales. Use WITH.
WITH reps AS (SELECT s.name sales_rep, r.name region, SUM(o.total_amt_usd) sales
	FROM sales_reps s
	JOIN region r
	ON r.id = s.region_id
	JOIN accounts a
	ON a.sales_rep_id = s.id
	JOIN orders o
	ON a.id = o.account_id
	GROUP BY 2, 1),
    
    max AS (SELECT region, MAX(sales) sales
    FROM reps
    GROUP BY 1)

SELECT reps.sales_rep, max.region, max.sales
FROM max
JOIN reps
ON max.region = reps.region AND reps.sales = max.sales;

--For the region with the largest (sum) of sales total_amt_usd, how many total (count) orders were placed? Use WITH.
WITH sales AS (SELECT r.name region, SUM(o.total_amt_usd) sales
FROM region r
JOIN sales_reps s
ON r.id = s.region_id
JOIN accounts a
ON a.sales_rep_id = s.id
JOIN orders o
ON a.id = o.account_id
GROUP BY 1),

max AS (SELECT MAX(sales)
        FROM sales)
        
SELECT r.name, COUNT(o.total) orders
FROM region r
JOIN sales_reps s
ON r.id = s.region_id
JOIN accounts a
ON a.sales_rep_id = s.id
JOIN orders o
ON a.id = o.account_id
GROUP BY 1
HAVING SUM(o.total_amt_usd) = (SELECT * FROM max);

--For the name of the account that purchased the most (in total over their lifetime as a customer) standard_qty paper, how many accounts still had more in total purchases? Use WITH.
WITH sub AS (SELECT a.name act_name, SUM(o.standard_qty) std_total, SUM(o.total) total
                        FROM accounts a
                        JOIN orders o
                        ON o.account_id = a.id
                        GROUP BY 1
                        ORDER BY 2 DESC
                        LIMIT 1),
      
    sub2 AS (SELECT a.name
    FROM orders o
    JOIN accounts a
    ON a.id = o.account_id
    GROUP BY 1
    HAVING SUM(o.total) > (SELECT total FROM sub)
    )

SELECT COUNT(*)
FROM sub2;

--For the customer that spent the most (in total over their lifetime as a customer) total_amt_usd, how many web_events did they have for each channel? Use WITH.
WITH tops AS (SELECT a.name, SUM(o.total_amt_usd) total_dollars
    FROM accounts a
    JOIN orders o
    ON a.id = o.account_id
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 1)

SELECT tops.name, w.channel, COUNT(*)
FROM tops
JOIN accounts a
ON top.name = a.name
JOIN web_events w
ON a.id = account_id
GROUP BY 1, 2;

--What is the lifetime average amount spent in terms of total_amt_usd for the top 10 total spending accounts? Use WITH.
WITH tops AS (SELECT a.name, SUM(o.total_amt_usd) amts
    FROM accounts a
    JOIN orders o
    ON a.id = o.account_id
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 10)

SELECT AVG(amts)
FROM tops;

--What is the lifetime average amount spent in terms of total_amt_usd for only the companies that spent more than the average of all orders? Use WITH.
WITH sub AS (SELECT a.name, AVG(o.total_amt_usd) avg_totals
    FROM accounts a
    JOIN orders o
    ON a.id = o.account_id
    GROUP BY 1
    HAVING AVG(o.total_amt_usd) > (SELECT AVG(total_amt_usd) FROM orders)
             )

SELECT AVG(avg_totals)
FROM sub;