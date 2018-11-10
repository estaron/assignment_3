import os
import csv

pollCSV = os.path.join("election_data.csv")

with open(pollCSV, 'r') as pollfile:
    pollreader = csv.reader(pollfile, delimiter=',')

    rows = []



    for i, row in enumerate(pollreader):
        if i==0:
            header = row
        else:
            rows.append(row)
# print(header)
# print(rows[:10])
total_votes=len(rows)

#make list of unique candidates

candidates = []
candidates.append(rows[0][2])
i=1
for row in rows:
    if row[2] not in candidates:
        candidates.append(row[2])

#make list of votes

votes = []
for row in rows:
    votes.append(row[2])

#make a new list with the vote total for each candidate

vote_count = []
for c in candidates:
    n=(votes.count(c))
    vote_count.append(n)

percent = []
for row in vote_count:
    p = round(row/total_votes, 4)
    percent.append(p)

i=0
j=0
max = vote_count[0]
while i<len(candidates):
    if max<vote_count[i]:
        j=i
        max = vote_count[i]
    i=i+1





print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------")
i = 0
while i<len(candidates):
    print(f"{candidates[i]}: {percent[i]*100}% ({vote_count[i]})")
    i=i+1
print("---------------------------")
print(f"Winner: {candidates[j]}" )
print("---------------------------")

#output a txt document

f= open("pypoll.txt","w")
f.write("Election Results\n")
f.write("---------------------------\n")
f.write(f"Total Votes: {total_votes}\n")
f.write("---------------------------\n")
i = 0
while i<len(candidates):
    f.write(f"{candidates[i]}: {percent[i]*100}% ({vote_count[i]})\n")
    i=i+1
f.write("---------------------------\n")
f.write(f"Winner: {candidates[j]}\n" )
f.write("---------------------------\n")