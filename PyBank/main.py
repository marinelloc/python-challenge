import os
import csv

# budget_csv = os.path.join("..", "Resources", "budget_data.csv")
budget_csv = os.path.join(r"C:\Users\marin\repo\python-challenge\PyBank\Resources\budget_data.csv")

# declaring variables
months = 0
bottomline = 0
profit_loss = []
month_list = []
change = 0

# logic for opening up csv and declaring header
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # initite iterator for csv
    for row in csvreader:
        # tallying all months
        months += 1
        # summing all profits/losses
        bottomline += int(row[1])
        # addinng all profit changes to list
        profit_loss.append((int(row[1])-change))
        # storing current rows profit to be used in comparsion against next row
        change = int(row[1])
        # adding all dates to list
        month_list.append(row[0])

    #calulates average of profits/loss
    average_change   = round(sum(profit_loss)/months)
    # finds postion in list of greastest and worst profits/losses
    greatest_index   = profit_loss.index(max(profit_loss))
    worst_index      = profit_loss.index(min(profit_loss))
    
    # print results to terminal
    print("""Financial Analysis
----------------------------""")
    print(f'Total Months: {months}')
    print(f'Total: ${bottomline}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {month_list[greatest_index]} (${max(profit_loss)})')
    print(f'Greatest Decrease in Profits: {month_list[worst_index]} (${min(profit_loss)})')

#results_csv = os.path.join("..", "Analysis", "results.csv")
results_csv = os.path.join(r"C:\Users\marin\repo\python-challenge\PyBank\Analysis\results.csv")

#  Open the output file
with open(results_csv, "w") as datafile:
    writer = csv.writer(datafile)
     # print results to output csv
    writer.writerow(['Financial Analysis'])
    writer.writerow(['----------------------------'])
    writer.writerow([f'Total Months: {months}'])
    writer.writerow([f'Total: ${bottomline}'])
    writer.writerow([f'Average Change: ${average_change}'])
    writer.writerow([f'Greatest Increase in Profits: {month_list[greatest_index]} (${max(profit_loss)})'])
    writer.writerow([f'Greatest Decrease in Profits: {month_list[worst_index]} (${min(profit_loss)})'])
