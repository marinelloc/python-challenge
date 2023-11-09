import os
import csv

# budget_csv = os.path.join("..", "Resources", "election_data.csv")
elec_csv = os.path.join(r"C:\Users\marin\repo\python-challenge\PyPoll\Resources\election_data.csv")

votes = 0
candidates = []
charlie = 0
diana = 0 
raymon = 0

with open(elec_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        candidates.append(row[2])
        votes += 1
        if row[2] == 'Charles Casper Stockham':
            charlie += 1
        if row[2] == 'Diana DeGette':
            diana += 1   
        if row[2] == 'Raymon Anthony Doane':
            raymon += 1

    candidate_list = []
    for x in candidates: 
        if x not in candidate_list: 
            candidate_list.append(x) 
    
    charliepct = round((charlie/votes)*100,3)
    dianapct   = round((diana/votes)*100,3)
    raymonpct  = round((raymon/votes)*100,3)

    if charliepct > dianapct and raymonpct:
        winner = candidate_list[0]
    if dianapct > charliepct and raymonpct:
        winner = candidate_list[1]
    if raymonpct > dianapct and charliepct:
        winner = candidate_list[2]

    print(f'Total Votes: {votes}')
    print('-------------------------')
    print(f'Charles Casper Stockham: {charliepct}% ({charlie})')
    print(f'Diana DeGette: {dianapct}% ({diana})')
    print(f'Raymon Anthony Doane: {raymonpct}% ({raymon})')
    print('-------------------------')
    print(f'Winner: {winner}')
    print('-------------------------')

# budget_csv = os.path.join("..", "Analysis", "results.csv")
results_csv = os.path.join(r"C:\Users\marin\repo\python-challenge\PyPoll\Analysis\results.csv")

#  Open the output file
with open(results_csv, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow([f'Total Votes: {votes}'])
    writer.writerow(['-------------------------'])
    writer.writerow([f'Charles Casper Stockham: {charliepct}% ({charlie})'])
    writer.writerow([f'Diana DeGette: {dianapct}% ({diana})'])
    writer.writerow([f'Raymon Anthony Doane: {raymonpct}% ({raymon})'])
    writer.writerow(['-------------------------'])
    writer.writerow([f'Winner: {winner}'])
    writer.writerow(['-------------------------'])
