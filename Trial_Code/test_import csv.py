import csv

filename = "user_details_report_1.csv"
filename1 = "Contractors.csv"

data = {}

with open("user_details_report_1.csv") as csv1:
    for row in csv.reader(csv1):
        data[row[0]] = row

with open("Contractors.csv") as csv2:
    for row in csv.reader(csv2):
        if row[0] in data:
            print(data[row[0]])
            