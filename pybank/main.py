# Modules
import os
import csv

csvpath = os.path.join(r"C:\Users\adamm\python-challenge\pybank\resources\02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

with open(csvpath) as csvfile:


    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    x = 0
    total_value = 0
    greatest_increase = 0
    greatest_decrease = 0
    greatest_month = " "
    worst_month = " "
    for row in csvreader:
        x = x + 1
        total_value = int(row[1]) + total_value
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row [1])
            greatest_month = row [0]
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row [1])
            worst_month = row [0]
        # print(row[1])

      
print("Number of Months" + ":" + " " + str(x))
print("total" + ":" " " + str(total_value))
average_PL = total_value/x
print("average_change" + ":" + " " + str(average_PL))
print("Greatest Profit Increase" + ":" + " " + str(greatest_increase))
print("Greatest Profit Decrease" + ":" + " " + str(greatest_decrease))