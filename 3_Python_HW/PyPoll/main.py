import os
import csv

data = os.path.join("Resources", "election_data.csv")

Candidates = []
Total_Votes = []
Vote = []
Percent = []
RunningVoteCount = 0
NumCandidates = 0

with open(data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        Candidates.append(row[2])
        RunningVoteCount += 1

for i in set(Candidates):
    Total_Votes.append(i)
    Vote.append(Candidates.count(i))
    Percent.append(100*((Candidates.count(i))/(RunningVoteCount)))
    NumCandidates += 1

Winner = Total_Votes[Vote.index(max(Vote))]

PyPollFile = "PyPoll.txt"
with open(PyPollFile, "w", newline='') as textfile:
    print("Election Results", file=textfile)
    print("----------------------------", file=textfile)
    print(f'Total Votes: {RunningVoteCount}', file=textfile)
    print("----------------------------", file=textfile)
    for x in range(NumCandidates):
            print(f'{Total_Votes[x]}: {round(Percent[x], 2)}% ({Vote[x]})', file=textfile)
    print("----------------------------", file=textfile)
    print(f'Winner: {Winner}', file=textfile)
    print("----------------------------", file=textfile)