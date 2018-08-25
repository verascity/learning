
# coding: utf-8

# In[1]:


"""
Modify the following get_pnl and get_price so that :
get_price returns the actual price from google finance and
get_pnl returns a dictionary with the company name as the key and the gain as the value
Example :

get_pnl()

should return(format, values will differ):

{'Alphabet, Inc.': -3105.0,
 'Apple, Inc.': 60110.0,
 'General Electric': 12095.0,
 'Goldman Sachs': 112416.5}

Note:
To connect to your MySQL database you have to get your credentials.
You will find your personal database credentials under the Details/Database tab at the top of this page. Complete your Host, password, user and name as string in the startercode below.

Use the provided HTM files to get the stock price from each company!
You can open them with:

filename="AAPL.htm"
with open(filename, 'r') as f:
    response_page = BeautifulSoup(f, 'lxml')

"""

import mysql.connector as conn

User = "u_2268_28390_955"
Name = "db_2268_28390_95596"
Host = "rdscourse.c5oiflamxeov.us-west-2.rds.amazonaws.com"
password = "GjBf91dfwx7w2LB9C977"


"""
Do Not Change!!

"""
db = conn.connect(host = Host, user = User, password = password, database = Name )
cursor = db.cursor()

file = "portfolio.txt"
with open(file,'r') as f:
    line_count = 0
    stocks_set = set()
    for line in f:
        line = line.strip()

        if line_count == 0:
            headers = line.split(':')
            headers = [x.replace(' ','_') for x in headers]
            query1 = "DROP TABLE IF EXISTS stocks;"
            query2 = "DROP TABLE IF EXISTS holdings"
            cursor.execute(query1)
            cursor.execute(query2)
            query1 = "CREATE TABLE IF NOT EXISTS stocks ("
            query1 += headers[0] + " VARCHAR(10),"
            query1 += headers[1] + " VARCHAR(30));"
            query2 = "CREATE TABLE IF NOT EXISTS holdings ("
            query2 += headers[0] + " VARCHAR(10),"
            query2 += headers[2] + " DECIMAL(10,2),"
            query2 += headers[3] + " INT,"
            query2 += headers[4] + " DATE);"
            cursor.execute(query1)
            cursor.execute(query2)
            line_count += 1
            continue        
        data = line.split(':')
        stock_info = (data[0],data[1])
        stocks_set.add(stock_info)
        holdings_query = 'INSERT INTO holdings VALUES ("'
        holdings_query +=data[0] + '",'
        holdings_query +=data[2] + ','
        holdings_query +=data[3] + ',"'
        holdings_query +=data[4] + '");'
        cursor.execute(holdings_query)
for s_info in stocks_set:
    stock_query = 'INSERT INTO stocks VALUES ("'
    stock_query += s_info[0] + '","'
    stock_query += s_info[1] +'");'
    cursor.execute(stock_query)
db.commit()
db.close()

"""
Change get_pnl and get_price

"""

def get_pnl(host=Host,user=User,name=Name,pwd=password):
    import mysql.connector as conn
    gain_dict = {}
    
    db = conn.connect(host = Host, user = User, password = password, database = Name )
    cursor = db.cursor()
    
    query = '''SELECT s.Company_Name, h.Ticker, SUM(h.Purchase_Price*h.Shares), SUM(h.Shares)
    FROM holdings AS h 
    INNER JOIN stocks AS s
    ON h.Ticker = s.Ticker
    GROUP BY s.Company_Name;'''
    cursor.execute(query)
    sums = cursor.fetchall()

    for row in sums:
        company_name = row[0]
        price_now = get_price(row[1])
        num_shares = float(row[3])
        prev_price = float(row[2])

        gain_dict[company_name] = (price_now * num_shares) - prev_price
    
    return gain_dict
   
def get_price(ticker):
    
    import requests
    from bs4 import BeautifulSoup
    filename = ticker + ".htm"
    with open(filename, 'r') as f:
        response_page = BeautifulSoup(f, 'lxml')

    price = response_page.find("span", class_="pr").get_text()
    price = price.replace(",", "")
    price = float(price)
    
    return price


# In[2]:


#
# AUTOGRADER TEST - DO NOT REMOVE
#


# In[3]:


#
# AUTOGRADER TEST - DO NOT REMOVE
#


# In[4]:


#
# AUTOGRADER TEST - DO NOT REMOVE
#


# In[5]:


#
# AUTOGRADER TEST - DO NOT REMOVE
#


# In[6]:



#
# AUTOGRADER TEST - DO NOT REMOVE
#

