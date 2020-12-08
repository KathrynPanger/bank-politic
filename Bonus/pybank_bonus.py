#!/usr/bin/env python
# coding: utf-8

# In[120]:


#Pybank tasks:
#* Get total number of months included in the dataset
#* Get total profit/losses over the entire period
#* Get average profit/losses per month over the entire period
#* The greatest increase in profits (date and amount) over the entire period
#* The greatest decrease in losses (date and amount) over the entire period


# In[121]:


#Dependenceis
import os
import csv
import pandas as pd
from statistics import mean


# In[122]:


#Read Data
df = pd.read_csv("pybank/Resources/budget_data.csv")


# In[123]:


#Get the total months included in the dataset

#---Get a list of months
monthlist=[]
for item in df["Date"]:
    monthlist.append((str(item)[0:3]))

#----Get the count of unique months
monthcount = (len(set(monthlist)))


# In[124]:


#Get total profit/losses" over the entire period
total=sum(df["Profit/Losses"])


# In[125]:


#Get average profit/losses over entire period
avg_gain=mean(df["Profit/Losses"])


# In[126]:


max_gain=max(df["Profit/Losses"])
min_gain=min(df["Profit/Losses"])


# In[127]:


df["profit"]=df["Profit/Losses"]
min_date = str(df.query(f'profit=={min_gain}')['Date'])
max_date = str(df.query(f'profit=={max_gain}')['Date'])


# In[128]:


min_date = min_date[6:14]
max_date = max_date[6:14]
max_date


# In[133]:


pybank_bonus= open(r"pybank_bonus.txt","w+")
pybank_bonus.write("Financial Analysis \n")
pybank_bonus.write("---------------------------- \n")
pybank_bonus.write(f"Total Months: {monthcount} \n")
pybank_bonus.write(f"Total: ${total} \n")
pybank_bonus.write(f"Average  Change: ${avg_gain:.2f} \n")
pybank_bonus.write(f"Greatest Increase in Profits: {max_date} (${min_gain}) \n")
pybank_bonus.write(f"Greatest Decrease in Profits: {min_date} (${max_gain}) \n")

