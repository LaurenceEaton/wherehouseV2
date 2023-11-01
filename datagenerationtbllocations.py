import csv
import random


csvdata = []



for i in range(1, 101):
    itemid = "{:04}".format(i) #to pad the ItemID e.g. 1 becomes 0001
    randomletter = str(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    randomnumber = str(random.randint(1,9))
    location = randomletter + randomnumber
    csvdata.append([itemid, location]) 



csvfilename = "tblLocations.csv"
with open(csvfilename, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["ItemID", "Location"])
    for row in csvdata:
        csvwriter.writerow(row)

print("CSV file generated: ", csvfilename)
