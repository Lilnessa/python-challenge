<<<<<<< Updated upstream
# PyPoll
# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
# You will be given a set of poll data called election_data.csv. The dataset is composed of 
# three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script 
# that analyzes the votes and calculates each of the following values:

import os
import csv

# Varidables
vote_list = []
total_votes = 0
candidatelist = {}
candidates = []

# Path to collect data from the Resources folder
election_csv = os.path.join('/users/vdumlao/Desktop/Challenges/python-challenge/PyPoll/Resources/election_data.csv')

# Open, read, and split data
with open(election_csv) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_file)

#loop and store data in dictionary
    for row in csv_reader:
        vote_list.append({"BallotID": row[0],"County":row[1],"Candidate": row[2]})
        
# Part1
# The total number of votes cast

total_votes = (len(vote_list))
    # print(total_votes)

print()
print("Election Results")
print()
print("-------------------------")
print()
print(f"Total Votes: {total_votes:,}")
print()
print("-------------------------")
print()

# Part2-4
# 2) A complete list of candidates who received votes. 
# 3) The percentage of votes each candidate won 
# 4) The total number of votes each candidate won

with open(election_csv) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_file)

    for row in csv_reader:
        candidates = row[2]
        votetally = int(row[0])

        if candidates not in candidatelist:
            candidatelist[candidates] = 0
        else:
            candidatelist[candidates] += 1
                     
    for candidates, votetally in candidatelist.items():
        # print(candidatelist)
        # print(candidates)

        print(f'{candidates}: {(votetally/total_votes):.3%} ({votetally:,})')
        print()
print("-------------------------")
print()     

# Part5
# The winner of the election based on popular vote

winner = max(candidatelist, key=candidatelist.get)

print(f'Winner: {winner}')
print()
print("-------------------------")
print() 

budget_csv = os.path.join('/users/vdumlao/Desktop/Challenges/python-challenge/PyPoll/Resources/')
with open("result_file.txt","w") as f:
    print(file=f)
    print("Election Results",file=f)
    print(file=f) 
    print("----------------------------",file=f)
    print(file=f)
    print(f"Total Votes: {total_votes:,}",file=f)
    print(file=f)   
    print("----------------------------",file=f)
    print(file=f)
    print(f'{candidates}: {(votetally/total_votes):.3%} ({votetally:,})',file=f)
    print(file=f)
    print("----------------------------",file=f)
    print(file=f)
    print(f'Winner: {winner}',file=f)
    print(file=f)
    print("----------------------------",file=f)
    print(file=f)
=======
# PyPoll
# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
# You will be given a set of poll data called election_data.csv. The dataset is composed of 
# three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script 
# that analyzes the votes and calculates each of the following values:

import os
import csv

# define variables
vote_list = []
total_votes = 0
candidatelist = {}
candidates = []
candidate_percent = {}

# Path to collect data from the Resources folder
election_csv = os.path.join("Pypoll","Resources","election_data.csv")

# Open, read, and split data
with open(election_csv) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_file)

#loop, store data in dictionary and assign location of candidate and votes
    for row in csv_reader:
        vote_list.append({"BallotID": row[0],"County":row[1],"Candidate": row[2]})
        candidates = row[2]
        votetally = int(row[0])
        # print(vote_list)
        # print(candidates)
        # print(votetally)

# Part1
# The total number of votes cast
        # count total vates
        total_votes = total_votes +1

# Part2-4
# 2) A complete list of candidates who received votes. 
# 3) The percentage of votes each candidate won 
# 4) The total number of votes each candidate won

#Determine the candidates names if it doesn't match the exiting
        if candidates not in candidatelist:
            candidatelist[candidates] = 0
        else:
            candidatelist[candidates] += 1

 # Print statements to terminal and write to text file
with open("PyPoll_result.txt","w") as text_file:
    print("\nElection Results\n")
    print("-------------------------\n")
    print(f"Total Votes: {total_votes:,}\n")
    print("-------------------------\n")
    text_file.write(os.linesep + "Election Results" + os.linesep)
    text_file.write("-------------------------"+ os.linesep)
    text_file.write(f"Total Votes: {total_votes:,}"+ os.linesep)
    text_file.write("-------------------------"+ os.linesep)

# Loop to fine list candidate and number of votes for each cancdate and list them as items.
    for candidates, votetally in candidatelist.items():

# calculate percentage of votes
        candidate_percent = votetally / total_votes
        
        # print(candidates)
        # print(candidate_percent)
        # print(votetally)
        # print(candidatelist)

# Print statements to terminal and write to text file
        print(f'{candidates}: {(candidate_percent):.3%} ({votetally:,})\n')
        text_file.write(f'{candidates}: {(candidate_percent):.3%} ({votetally:,})'+ os.linesep)

# Part5
# The winner of the election based on popular vote
# From the candidate list get the candidate name with the most votes
    winner = max(candidatelist, key=candidatelist.get)

# Print statements to terminal and write to text file
    print("-------------------------\n")
    print(f'Winner: {winner}\n')
    print("-------------------------\n")
    text_file.write("-------------------------"+ os.linesep)
    text_file.write(f'Winner: {winner}'+ os.linesep)
    text_file.write("-------------------------"+ os.linesep)
>>>>>>> Stashed changes
