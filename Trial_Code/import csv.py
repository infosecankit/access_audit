import csv


filename = "user_details_report_1.csv"
filename1 = "Contractors.csv"
fileone = ""
filetwo = ""

# fields = []
# rows = []

with open(filename, 'r') as csvfile, open(filename1, 'r') as csvfile1:

    fileone = csvfile.readlines()
    filetwo = csvfile1.readlines()

with open('update.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)