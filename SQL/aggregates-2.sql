--Find the earliest order.

SELECT MIN(occurred_at)
FROM orders;

--Find the earliest order without using an aggregate.

SELECT occurred_at
FROM orders
ORDER BY occurred_at
LIMIT 1;

--Find the most recent web event.

SELECT MAX(occurred_at)
FROM web_events;

--Find the most recent web event without using an aggregate.

SELECT occurred_at
FROM web_events
ORDER BY occurred_at DESC
LIMIT 1;

--Find the average sale quantity and cost for each type of sale.

SELECT AVG(standard_qty) AS standard_orders,
       AVG(standard_amt_usd) AS standard_sales,
       AVG(gloss_qty) AS gloss_orders,
       AVG(gloss_amt_usd) AS gloss_sales,
       AVG(poster_qty) AS poster_orders,
       AVG(poster_amt_usd) AS poster_sales
FROM orders;

--Find the median total in USD using aggregates and subqueries.
 --Get the count.

SELECT COUNT(total_amt_usd)
FROM orders;

--Returns 6912, so the median is the average of sorted rows 3456 and 3457.

SELECT MAX(total_amt_usd)
FROM
  (SELECT total_amt_usd
   FROM orders
   ORDER BY total_amt_usd
   LIMIT 3457) AS top_half;


SELECT MAX(total_amt_usd)
FROM
  (SELECT total_amt_usd
   FROM orders
   ORDER BY total_amt_usd
   LIMIT 3456) AS next_max;

--Return values of 2483.16 and 2482.55, giving a median of 2482.855.