# Modules
import os
import csv

csvpath = os.path.join(r"C:\Users\adamm\python-challenge\pypoll\resources\02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

with open(csvpath) as csvfile:


    csvreader = csv.reader(csvfile, delimiter=',')
    
    #test_list = list(csvreader)
    #print (test_list.count('Li'))
   # print(csvreader)

    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    total_votes = 0
    candidates = []
    #can = []
    #vote = []
    #county = []
    #test_list = list(csvreader)
    #print (str(test_list.count))
    for row in csvreader:
        total_votes = total_votes + 1
        #print (str(row[2]))
        #myDict = dict (row[0],row[2])
        if row[2] not in candidates:
            print (str(row[2]))
            candidates.append(row[2])
    #for candidate in candidates:
        #print (candidate)
        #(str.split(row[2]))
        #percent_won = (candidates/total_votes)*100


print("Total Votes Cast" + ":" + " " + str(total_votes))