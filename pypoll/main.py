#import modules
import os
import csv

#open the dataset
pypoll_csvpath = os.path.join('..', 'Resources', 'election_data.csv')

pypoll_rowlist=[]
with open(pypoll_csvpath) as pypoll_csvfile:
    pypoll_csvreader = csv.reader(pypoll_csvfile, delimiter=',')
    pypol_csv_header = next(pypoll_csvreader)


    for row in pypoll_csvreader:
        pypoll_rowlist.append(row)

#get list of candidates
candidate_list=[]
for row in pypoll_rowlist:
    candidate_list.append(row[2])

#get votes for each candidate, save this to a dictionary
candidate_wins= {"Khan":0, "Li":0,"O'Tooley":0, "Correy":0, "Missing_Value":0}
for names in candidate_list:
    if names =="Khan":
        candidate_wins["Khan"]+=1
    elif names =="Li":
        candidate_wins["Li"] +=1
    elif names== "O'Tooley":
        candidate_wins["O'Tooley"]+=1
    elif names =="Correy":
        candidate_wins["Correy"]+=1
    else:
        candidate_wins["Missing_Value"]+=1

#get candidate percentage of votes, save this to a dictionary
candidate_percentage=candidate_wins
for names in candidate_wins:
    if names =="Khan":
        candidate_percentage["Khan"]=candidate_percentage["Khan"]/len(pypoll_rowlist)*100
    elif names =="Li":
        candidate_percentage["Li"]=candidate_percentage["Li"]/len(pypoll_rowlist)*100
    elif names== "O'Tooley":
        candidate_percentage["O'Tooley"]=candidate_percentage["O'Tooley"]/len(pypoll_rowlist)*100
    elif names =="Correy":
        candidate_percentage["Correy"]=candidate_percentage["Correy"]/len(pypoll_rowlist)*100
    else:
        if candidate_percentage["Missing_Value"]==0:
            pass
        else:
            candidate_percentage["Missing_Value"]=candidate_percentage["Missing_Value"]/len(pypoll_rowlist)*100

#create a sorted list of the winners and their percentage of total votes
sorted_list=[]
poppable_list=candidate_percentage

while poppable_list:
    winner_name = max(poppable_list, key=poppable_list.get)
    sorted_list.append(winner_name)
    winner_percent = max(poppable_list.values())
    sorted_list.append(winner_percent)
    poppable_list.pop(winner_name)

#print the output to the terminal

print("Election Results")
print("-------------------------")
print(f"Total Votes: {len(pypoll_rowlist)}")
print("-------------------------")
print(f"{sorted_list[0]}: {sorted_list[1]:.0f}% ({(sorted_list[1]/100)*len(pypoll_rowlist):.0f})")
print(f"{sorted_list[2]}: {sorted_list[3]:.0f}% ({(sorted_list[3]/100)*len(pypoll_rowlist):.0f})")
print(f"{sorted_list[4]}: {sorted_list[5]:.0f}% ({(sorted_list[5]/100)*len(pypoll_rowlist):.0f})")
print(f"{sorted_list[6]}: {sorted_list[7]:.0f}% ({(sorted_list[7]/100)*len(pypoll_rowlist):.0f})")
print("-------------------------")
print(f"Winner: {sorted_list[0]}")
print("-------------------------")


#print the output to a text file
pypoll_output= open(r"pypoll_output.txt","w+")

pypoll_output.write("Election Results \n")
pypoll_output.write("-------------------------\n")
pypoll_output.write(f"Total Votes: {len(pypoll_rowlist)} \n")
pypoll_output.write("-------------------------\n")
pypoll_output.write(f"{sorted_list[0]}: {sorted_list[1]:.0f}% ({(sorted_list[1]/100)*len(pypoll_rowlist):.0f}) \n")
pypoll_output.write(f"{sorted_list[2]}: {sorted_list[3]:.0f}% ({(sorted_list[3]/100)*len(pypoll_rowlist):.0f}) \n")
pypoll_output.write(f"{sorted_list[4]}: {sorted_list[5]:.0f}% ({(sorted_list[5]/100)*len(pypoll_rowlist):.0f}) \n")
pypoll_output.write(f"{sorted_list[6]}: {sorted_list[7]:.0f}% ({(sorted_list[7]/100)*len(pypoll_rowlist):.0f}) \n")
pypoll_output.write("------------------------- \n")
pypoll_output.write(f"Winner: {sorted_list[0]} \n")
pypoll_output.write("-------------------------")