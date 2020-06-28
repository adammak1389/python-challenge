# Modules
import os
import csv
from collections import Counter

my_dict = dict()
csvpath = os.path.join(r"resources/02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

with open(csvpath) as csvfile:


    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
            # my_dict[int(row[0])]= row[2]
        my_dict.update({row[0]:row[2]})
        #print(row[0])
        #print(row[0],row[1],row[2],)


    total_vote = int(my_dict.__len__())
res = Counter(my_dict.values())

print ("Election Results")
print ("-----------------")
print ("Total Votes:" + str(total_vote))
print ("-----------------")
for k,v in res.items():
    candidate = k
    candidate_vote = int(v)
    candidate_percent = float(float(candidate_vote)/float(total_vote)) * 100
    print (candidate + "  "+ str(candidate_percent) +"%"  + "  " + "(" + str(candidate_vote) + ")" )

print ("Winner: " + str(next(iter(res))))