import os
import csv

elec_csv = os.path.join("Resources", "election_data.csv")

# declaring variables
votes = 0
candidates = []
charlie = 0
diana = 0 
raymon = 0

# logic for opening up csv and declaring header
with open(elec_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # initite iterator for csv
    for row in csvreader:
        # creates lists of candidates votes
        candidates.append(row[2])
        
        # tally all votes
        votes += 1
        
        # tally votes for each candidate
        if row[2] == 'Charles Casper Stockham':
            charlie += 1
        if row[2] == 'Diana DeGette':
            diana += 1   
        if row[2] == 'Raymon Anthony Doane':
            raymon += 1

    # create list of candidates
    candidate_list = []
    for x in candidates: 
        if x not in candidate_list: 
            candidate_list.append(x) 

    # determine percetage of votes for each candidate
    charliepct = round((charlie/votes)*100,3)
    dianapct   = round((diana/votes)*100,3)
    raymonpct  = round((raymon/votes)*100,3)

    # compare election results and declare winner variable
    if charliepct > dianapct and raymonpct:
        winner = candidate_list[0]
    if dianapct > charliepct and raymonpct:
        winner = candidate_list[1]
    if raymonpct > dianapct and charliepct:
        winner = candidate_list[2]

    # print results to terminal
    print(f'Total Votes: {votes}')
    print('-------------------------')
    print(f'Charles Casper Stockham: {charliepct}% ({charlie})')
    print(f'Diana DeGette: {dianapct}% ({diana})')
    print(f'Raymon Anthony Doane: {raymonpct}% ({raymon})')
    print('-------------------------')
    print(f'Winner: {winner}')
    print('-------------------------')

results_csv = os.path.join("Analysis", "results.csv")

#  Open the output file
with open(results_csv, "w") as datafile:
    writer = csv.writer(datafile)
    # print results to output csv
    writer.writerow([f'Total Votes: {votes}'])
    writer.writerow(['-------------------------'])
    writer.writerow([f'Charles Casper Stockham: {charliepct}% ({charlie})'])
    writer.writerow([f'Diana DeGette: {dianapct}% ({diana})'])
    writer.writerow([f'Raymon Anthony Doane: {raymonpct}% ({raymon})'])
    writer.writerow(['-------------------------'])
    writer.writerow([f'Winner: {winner}'])
    writer.writerow(['-------------------------'])
