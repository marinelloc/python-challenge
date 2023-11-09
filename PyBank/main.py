import os
import csv

budget_csv = os.path.join("..", "Resources", "budget_data.csv")
# budget_csv = os.path.join(r"C:\Users\marin\repo\python-challenge\PyBank\Resources\budget_data.csv")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        print(row)

