--In the accounts table, there is a column holding the website for each company. Pull the website extensions and provide how many of each website type exist in the accounts table.
SELECT RIGHT(website, 3) AS extension, 
    COUNT(website) AS count
FROM accounts
GROUP BY 1;

--Use the accounts table to pull the first letter of each company name to see the distribution of company names that begin with each letter (or number). 
SELECT LEFT(name, 1) AS first_letter, 
    COUNT(name) AS count
FROM accounts
GROUP BY 1
ORDER BY 1;

--Use the accounts table and a CASE statement to create two groups: one group of company names that start with a number and a second group of those company names that start with a letter.
SELECT CASE
    WHEN UPPER(LEFT(name, 1)) BETWEEN 'A' AND 'Z' THEN 'letter'
    WHEN LEFT(name, 1) BETWEEN '1' AND '9' THEN 'number'
    END first_char, 
    COUNT(name) counts
FROM accounts
GROUP BY 1;

--Consider vowels as a, e, i, o, and u. What proportion of company names start with a vowel, and what percent start with anything else?
SELECT CASE
    WHEN UPPER(LEFT(name, 1)) IN ('A', 'E', 'I', 'O', 'U') THEN 'vowel'
    ELSE 'not a vowel'
    END first_char, 
    COUNT(name) counts
FROM accounts
GROUP BY 1;