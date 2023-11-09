import os
import csv

# budget_csv = os.path.join("..", "Resources", "budget_data.csv")
budget_csv = os.path.join(r"C:\Users\marin\repo\python-challenge\PyBank\Resources\budget_data.csv")

months = 0
bottomline = 0
profit_loss = []
month_list = []
change = 0

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        months += 1
        bottomline += int(row[1])
        profit_loss.append((int(row[1])-change))
        change = int(row[1])
        month_list.append(row[0])
    
    average_change   = round(sum(profit_loss)/months)
    greatest_index   = profit_loss.index(max(profit_loss))
    worst_index      = profit_loss.index(min(profit_loss))

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

    writer.writerow(['Financial Analysis'])
    writer.writerow(['----------------------------'])
    writer.writerow([f'Total Months: {months}'])
    writer.writerow([f'Total: ${bottomline}'])
    writer.writerow([f'Average Change: ${average_change}'])
    writer.writerow([f'Greatest Increase in Profits: {month_list[greatest_index]} (${max(profit_loss)})'])
    writer.writerow([f'Greatest Decrease in Profits: {month_list[worst_index]} (${min(profit_loss)})'])
