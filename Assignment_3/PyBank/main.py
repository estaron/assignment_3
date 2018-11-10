import os
import csv

budgetCSV = os.path.join("budget_data.csv")

with open(budgetCSV, 'r') as budgetfile:
    budgetreader = csv.reader(budgetfile, delimiter=',')

    rows = []



    for i, row in enumerate(budgetreader):
        if i==0:
            header = row
        else:
            rows.append(row)

TotalMonths = len(rows)
Total = 0
for row in rows:
    Total = Total + float(row[1])
Average = (float(rows[TotalMonths-1][1]) - float(rows[0][1]))/(TotalMonths-1)
i=1
j=0
gInc = float(rows[1][1])-float(rows[0][1])
while i<TotalMonths-1:
    g=float(rows[i+1][1])-float(rows[i][1])
    if g>gInc:
        gInc=g
        j=i    
    i=i+1
gIncMonth = j+1

i=1
j=0
gDec = float(rows[1][1])-float(rows[0][1])
while i<TotalMonths-1:
    d=float(rows[i+1][1])-float(rows[i][1])
    if d<gDec:
        gDec=d
        j=i    
    i=i+1
gDecMonth = j+1

print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {TotalMonths}")
print(f"Total: ${Total} ")
print(f"Average Change: ${Average}")
print(f"Greatest Increase in Profits: {rows[gIncMonth][0]} ({gInc})")
print(f"Greatest Decrease in Profits: {rows[gDecMonth][0]} ({gDec})")

f= open("pypoll.txt","w")
f.write("Financial Analysis")
f.write("--------------------------") 