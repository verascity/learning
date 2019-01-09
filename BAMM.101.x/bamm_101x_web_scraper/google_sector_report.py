
# coding: utf-8

# In[1]:


"""
Modify the following google_sector_report so that it returns a json 
dump that contains the following information about each sector:
1. The sector name
2. The percentage change in sector value
3. The biggest gainer and the percentage change in the biggest gainer
4. The biggest loser and the percentage change in the biggest loser

The structure of the json is given in the assignment description on EdX.

Note:
1. To read files, use:
with open('filename') as f:
    lines = f.readlines()
2. The files needed can be seen in the Jupyter environment, so just use 
the four files to get your answer and DO NOT web scrape anything online.
That means, you only need to return 3 sectors' information.
"""

# do not change anything that is originally written in here
# write the solution in suggested area


# In[2]:


# Run this cell and do not change it
with open('GoogleFinance.htm') as f:
    file1 = f.readlines()


# In[3]:


def google_sector_report(file1):
    from bs4 import BeautifulSoup

    file1 = "".join(file1)
    ref_json = {}

    parent = BeautifulSoup(file1, 'html.parser')
    
    sector_summary = parent.find('div', id='secperf')
    sector_info = []
    for l in sector_summary.find_all(["a", "span"], limit=6):
        info = l.get_text()
        if info[-1] == "%":
            sector_info.append(float(info[:-1]))
        else:
            sector_info.append(info)

    it = iter(sector_info)
    tpls = list(zip(it, it))

    name_dict = {a:{"biggest_gainer":{}, "biggest_loser":{}, "change":b} for a,b in tpls}

    ref_json["results"] = name_dict
    
    temp = {}

    for key in ref_json['results'].keys():
        name_str = key+".htm"
        with open(name_str) as f:
            page = "".join(f.readlines())
        child = BeautifulSoup(page, 'html.parser')
        c_table = child.find("table", class_="topmovers")
        temp[key] = c_table  
        
    for k, v in temp.items():

        wl_names = []
        wl_changes = []

        for item in v.find_all("a", limit=20):
                c_name = item.get_text()
                if len(c_name) > 4:
                    wl_names.append(c_name)

        for item in v.find_all("span", limit=20):
                change = item.get_text()
                if change[0] == "(":
                    wl_changes.append(float(change[1:-2]))

        tpls = list(zip(wl_names, wl_changes))
        sorted_tpls = sorted(tpls, key=lambda x: x[1], reverse=True)

        ref_json["results"][k]["biggest_gainer"]["equity"] = sorted_tpls[0][0]
        ref_json["results"][k]["biggest_gainer"]["change"] = sorted_tpls[0][1]
        ref_json["results"][k]["biggest_loser"]["equity"] = sorted_tpls[-1][0]
        ref_json["results"][k]["biggest_loser"]["change"] = sorted_tpls[-1][1]


    return ref_json


# In[4]:


# Run this cell to get a grade!
#
# AUTOGRADER TEST - DO NOT REMOVE
#


# In[5]:


# Run this cell to get a grade!
#
# AUTOGRADER TEST - DO NOT REMOVE
#


# In[6]:


# Run this cell to get a grade!
#
# AUTOGRADER TEST - DO NOT REMOVE
#


# In[7]:


# Run this cell to get a grade!
#
# AUTOGRADER TEST - DO NOT REMOVE
#


# In[ ]:




