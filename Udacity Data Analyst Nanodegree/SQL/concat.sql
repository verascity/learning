--Each company in the accounts table wants to create an email address for each primary_poc in the form of: first name of primary_poc . last name primary_poc @ company name .com.
SELECT first_name || '.' || last_name || '@' || company || '.com' email
FROM 
    (SELECT name company, 
        LEFT(primary_poc, POSITION(' ' IN primary_poc) - 1) first_name,
        RIGHT(primary_poc, LENGTH(primary_poc) - POSITION(' ' IN primary_poc)) last_name
    FROM accounts) tb1;

--See if you can create an email address that will work by removing all of the spaces in the account name.
SELECT LOWER(CONCAT(first_name, '.', last_name, '@', REPLACE(company, ' ', ''), '.com')) email
FROM 
    (SELECT name company, 
        LEFT(primary_poc, POSITION(' ' IN primary_poc) - 1) first_name,
        RIGHT(primary_poc, LENGTH(primary_poc) - POSITION(' ' IN primary_poc)) last_name
    FROM accounts) tb1;

/*We would also like to create an initial password, which they will change after their first log in. The first password will be the first letter of the primary_poc's first name (lowercase), 
then the last letter of their first name (lowercase), the first letter of their last name (lowercase), the last letter of their last name (lowercase), 
the number of letters in their first name, the number of letters in their last name, and then the name of the company they are working with, all capitalized with no spaces.*/
WITH sub AS (SELECT name company, 
             LEFT(primary_poc, POSITION(' ' IN primary_poc) - 1) first_name,
    		RIGHT(primary_poc, LENGTH(primary_poc) - POSITION(' ' IN primary_poc)) last_name
    FROM accounts)
          
SELECT CONCAT(LOWER(LEFT(first_name, 1)), RIGHT(first_name, 1), LOWER(LEFT(last_name, 1)), RIGHT(last_name, 1), 
LENGTH(first_name), LENGTH(last_name), UPPER(REPLACE(company, ' ', ''))) 
FROM sub;




