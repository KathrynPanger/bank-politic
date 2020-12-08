#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PyPoll tasks:
#* Get total number of votes cast
#* Get list of candidates who received votes
#* Get percentage of votes each candidate won
#* Get total number of votes each candidate won
#* Get winner of the election based on popular vote


# In[2]:


#Dependencies
import pandas as pd


# In[3]:


#Read in data
df=pd.read_csv("../pypoll/Resources/election_data.csv")


# In[4]:


#Get number of votes
unique = df["Voter ID"].unique()
total_votes=len(unique)


# In[5]:


#Get candidate names
candidates = list(df["Candidate"].unique())


# In[6]:


#Get percentage and number of votes per candidate
score_dict = {}
percent_dict={}
for name in candidates: 
   votes = df.loc[df["Candidate"] == name]
   count = len(votes)
   percent = round(((count/total_votes)*100),2)
   print(f"Candidate: {name}, Count: {count}, Percent: {percent}")
   score_dict[name]=count
   percent_dict[name]=percent
maxvotes=max(score_dict.values())

#Get winner
for candidate, score in score_dict.items(): 
    if score == maxvotes:
        winner = candidate


# In[7]:


#print the output to a text file
pypoll_bonus= open(r"pypoll_bonus.txt","w+")

pypoll_bonus.write("Election Results \n")
pypoll_bonus.write("-------------------------\n")
pypoll_bonus.write(f"Total Votes: {total_votes} \n")
pypoll_bonus.write("-------------------------\n")
pypoll_bonus.write(f"{candidates[0]}: {percent_dict[candidates[0]]}% \n")
pypoll_bonus.write(f"{candidates[1]}: {percent_dict[candidates[1]]}% \n")
pypoll_bonus.write(f"{candidates[2]}: {percent_dict[candidates[2]]}% \n")
pypoll_bonus.write(f"{candidates[3]}: {percent_dict[candidates[3]]}% \n")
pypoll_bonus.write("------------------------- \n")
pypoll_bonus.write(f"Winner: {winner} \n")
pypoll_bonus.write("-------------------------")

