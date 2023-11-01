import csv
import random
from datetime import date
from datetime import timedelta

items = ["Pet Food", "Pet Shampoo", "Pet Toy", "Pet Bed", "Pet Collar"]


def randomexpirydate():
    startdate = date(2024, 1, 1)
    enddate = date(2024, 12, 31)
    randomdate = random.randint(0, (enddate - startdate).days)
    return startdate + timedelta(days=randomdate)



csvdata = []
for i in range(1, 101):
    itemid = "{:04}".format(i) #to pad the ItemID e.g. 1 becomes 0001
    itemname = random.choice(items)
    expirydate = randomexpirydate().strftime("%Y-%m-%d") #returns the date/time value to a string using datetime library
    csvdata.append([itemid, itemname, expirydate]) #adding resulting data to the comma seperated file



csvfilename = "items3.csv"
with open(csvfilename, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["ItemID", "ItemName", "ExpiryDate"])
    for row in csvdata:
        csvwriter.writerow(row)

print("CSV file generated: ", csvfilename)
