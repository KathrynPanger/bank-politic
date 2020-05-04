#import modules
import os
import csv

#read the data
pybank_csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
pybank_rowlist=[]
pybank_profitlist=[]

with open(pybank_csvpath) as pybank_csvfile:
    pybank_csvreader = csv.reader(pybank_csvfile, delimiter=',')
    pybank_csv_header = next(pybank_csvreader)


    for row in pybank_csvreader:
        pybank_rowlist.append(row[0])
        pybank_profitlist.append(int(row[1]))

#Find all months in the dataset to be counted in final ananalysis
splitlist=[]
for item in pybank_rowlist:
    splitlist.append(item.split("-"))
monthsonly=[]
for entry in splitlist:
    monthsonly.append(entry[0])

#find the total profits
pybank_profitlist.pop(0)
pybank_profitlist_int=[]
for profit in pybank_profitlist:
    pybank_profitlist_int.append(int(profit))
summation=0
for amount in pybank_profitlist_int:
    summation=summation+amount

#get profit differences (note: this code is not original, but comes from https://www.geeksforgeeks.org/python-generate-successive-element-difference-list/)
profit_differences = [pybank_profitlist[i + 1] - pybank_profitlist[i] for i in range(len(pybank_profitlist)-1)]

#get average profit difference
average_diff=0
for differences in profit_differences:
    average_diff+=differences
average_diff=average_diff/len(profit_differences)

#get max and min profit differences

#Note: "x+1" becasue I popped the header off of my row list earlier, changing the indicies
max_difference=(max(profit_differences))
min_difference=(min(profit_differences))
x=(profit_differences.index(max(profit_differences)))
y=(profit_differences.index(min(profit_differences)))
maxmonth=(pybank_rowlist[x+1])
minmonth=(pybank_rowlist[y+1])

#Print the output to the terminal
print("Financial Analysis ")
print("---------------------------- ")
print(f"Total Months: {len(monthsonly)} ")
print(f"Total: ${summation} ")
print(f"Average  Change: ${average_diff:.2f} ")
print(f"Greatest Increase in Profits: {maxmonth} (${max_difference}) ")
print(f"Greatest Decrease in Profits: {minmonth} (${min_difference}) ")


#Print the output to a text file
pybank_output= open(r"pybank_output.txt","w+")
pybank_output.write("Financial Analysis \n")
pybank_output.write("---------------------------- \n")
pybank_output.write(f"Total Months: {len(monthsonly)} \n")
pybank_output.write(f"Total: ${summation} \n")
pybank_output.write(f"Average  Change: ${average_diff:.2f} \n")
pybank_output.write(f"Greatest Increase in Profits: {maxmonth} (${max_difference}) \n")
pybank_output.write(f"Greatest Decrease in Profits: {minmonth} (${min_difference}) \n")