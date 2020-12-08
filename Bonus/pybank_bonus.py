#Pybank tasks:
#* Get total number of months included in the dataset
#* Get total profit/losses over the entire period
#* Get average profit/losses per month over the entire period
#* The greatest increase in profits (date and amount) over the entire period
#* The greatest decrease in losses (date and amount) over the entire period

#Dependenceis
import os
import csv
import pandas as pd
from statistics import mean

#Read Data
df = pd.read_csv("pybank/Resources/budget_data.csv")

#---Get a list of months
monthlist=[]
for item in df["Date"]:
    monthlist.append((str(item)[0:3]))

#----Get the count of unique months
monthcount = (len(set(monthlist)))

#Get total profit/losses" over the entire period
total=sum(df["Profit/Losses"])

#Get average profit/losses over entire period
avg_gain=mean(df["Profit/Losses"])

#Get max and min Profit/Loss
max_gain=max(df["Profit/Losses"])
min_gain=min(df["Profit/Losses"])

#Get associated months
df["profit"]=df["Profit/Losses"]
min_date = str(df.query(f'profit=={min_gain}')['Date'])
max_date = str(df.query(f'profit=={max_gain}')['Date'])

min_date = min_date[6:14]
max_date = max_date[6:14]

#Print Output
pybank_bonus= open(r"pybank_bonus.txt","w+")
pybank_bonus.write("Financial Analysis \n")
pybank_bonus.write("---------------------------- \n")
pybank_bonus.write(f"Total Months: {monthcount} \n")
pybank_bonus.write(f"Total: ${total} \n")
pybank_bonus.write(f"Average  Change: ${avg_gain:.2f} \n")
pybank_bonus.write(f"Greatest Increase in Profits: {max_date} (${min_gain}) \n")
pybank_bonus.write(f"Greatest Decrease in Profits: {min_date} (${max_gain}) \n")

