--Provide the name of the sales_rep in each region with the largest amount of total_amt_usd sales.
SELECT t3.rep_name, t3.region_name, t3.total_amt
FROM
    (SELECT region_name, MAX(total_amt) total_amt
     FROM
        (SELECT s.name rep_name, r.name region_name, SUM(o.total_amt_usd) total_amt
             FROM sales_reps s
             JOIN accounts a
             ON a.sales_rep_id = s.id
             JOIN orders o
             ON o.account_id = a.id
             JOIN region r
             ON r.id = s.region_id
             GROUP BY 1, 2) t1
     GROUP BY 1) t2
JOIN 
    (SELECT s.name rep_name, r.name region_name, SUM(o.total_amt_usd) total_amt
        FROM sales_reps s
        JOIN accounts a
        ON a.sales_rep_id = s.id
        JOIN orders o
        ON o.account_id = a.id
        JOIN region r
        ON r.id = s.region_id
        GROUP BY 1,2
        ORDER BY 3 DESC) t3
ON t3.region_name = t2.region_name AND t3.total_amt = t2.total_amt;

--For the region with the largest (sum) of sales total_amt_usd, how many total (count) orders were placed? 
SELECT r.name, COUNT(o.total) total_sales
FROM region r
JOIN sales_reps s
ON r.id = s.region_id
JOIN accounts a
ON s.id = a.sales_rep_id
JOIN orders o
ON o.account_id = a.id
GROUP BY 1
HAVING SUM(o.total_amt_usd) =
    (SELECT MAX(total_dollars)
    FROM (SELECT r.name, SUM(o.total_amt_usd) total_dollars
         FROM region r
         JOIN sales_reps s
         ON r.id = s.region_id
         JOIN accounts a
         ON s.id = a.sales_rep_id
         JOIN orders o
         ON o.account_id = a.id
         GROUP BY 1) sub);

--For the name of the account that purchased the most (in total over their lifetime as a customer) standard_qty paper, how many accounts still had more in total purchases? 
SELECT COUNT(*)
FROM
    (SELECT a.name
    FROM orders o
    JOIN accounts a
    ON a.id = o.account_id
    GROUP BY 1
    HAVING SUM(o.total) > (SELECT total 
                  FROM (SELECT a.name act_name, SUM(o.standard_qty) std_total, SUM(o.total) total
                        FROM accounts a
                        JOIN orders o
                        ON o.account_id = a.id
                        GROUP BY 1
                        ORDER BY 2 DESC
                        LIMIT 1) sub)
    ) sub2;

--For the customer that spent the most (in total over their lifetime as a customer) total_amt_usd, how many web_events did they have for each channel?
SELECT tops.name, w.channel, COUNT(*)
FROM 
    (SELECT a.name, SUM(o.total_amt_usd) total_dollars
    FROM accounts a
    JOIN orders o
    ON a.id = o.account_id
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 1) tops
JOIN accounts a
ON top.name = a.name
JOIN web_events w
ON a.id = account_id
GROUP BY 1, 2;

--OR

SELECT a.name, w.channel, COUNT(*)
FROM accounts a
JOIN web_events w
ON a.id = w.account_id AND a.name = (SELECT name
                                    FROM 
                                        (SELECT a.name, SUM(o.total_amt_usd) total_dollars
                                        FROM accounts a
                                        JOIN orders o
                                        ON a.id = o.account_id
                                        GROUP BY 1
                                        ORDER BY 2 DESC
                                        LIMIT 1) top)
GROUP BY 1, 2;

--What is the lifetime average amount spent in terms of total_amt_usd for the top 10 total spending accounts?
SELECT AVG(amts)
FROM 
    (SELECT a.name, SUM(o.total_amt_usd) amts
    FROM accounts a
    JOIN orders o
    ON a.id = o.account_id
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 10) tops;

--What is the lifetime average amount spent in terms of total_amt_usd for only the companies that spent more than the average of all orders.
SELECT AVG(avg_totals)
FROM 
    (SELECT a.name, AVG(o.total_amt_usd) avg_totals
    FROM accounts a
    JOIN orders o
    ON a.id = o.account_id
    GROUP BY 1
    HAVING AVG(o.total_amt_usd) > (SELECT AVG(total_amt_usd) 
                                    FROM orders)
    ) sub;