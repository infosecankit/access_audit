import csv
filename = "user_details_report_1.csv"
filename1 = "Contractors.csv"

fields = []
rows = []

with open(filename, 'r') as csvfile:
    with open(filename1, 'r') as csvfile1:

         csvreader = csvfile.readlines()
         csvreader1 = csvfile1.readlines()

        # creating a csv reader object
       # csvreader = csv.reader(csvfile)
       # csvreader1 = csv.reader(csvfile1)

        # extracting field names through first row
       # fields = next(csvreader)
       # fields1 = next(csvreader1)

        # extracting each data row one by one
    counter = 0
    for row in csvreader:
                # rows.append(row)
            if row != csvreader1[counter]:
                print("Match not found")
            counter += 1
        
        # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
    print("Total no. of rows: %d"%(csvreader1.line_num))

        # printing the field names
    print('Field names are:' + ', '.join(field for field in fields))
    print('Field names are:' + ', '.join(field for field in fields1))
    
    #  printing first 5 rows
    # print('\nFirst 5 rows are:\n')
    # for row in rows[:5]:
    #     for row in row1[:5]:
    #     # parsing each column of a row
    #         for col in row:
    #             for col1 in row1:
    #                 if(col == col1):
    #                     print("%10s"%col1,end=" ")
    #                     print("%10s"%col,end=" "),
    #                 else:
    #                     print("No common match found")
    #                 print('\n')

        
 