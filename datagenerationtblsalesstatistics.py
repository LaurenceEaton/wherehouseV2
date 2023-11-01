import csv
import random


csvdata = []



for i in range(1, 101):
    itemid = "{:04}".format(i) #to pad the ItemID e.g. 1 becomes 0001
    SalesWeek = str(random.randint(1,50))
    SalesMonth = str(random.randint(1,250))
    SalesYear = str(random.randint(1,5000))
    csvdata.append([itemid, SalesWeek, SalesMonth, SalesYear]) 



csvfilename = "tblSalesStatistics.csv"
with open(csvfilename, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["ItemID", "SalesWeek", "SalesMonth", "SalesYear"])
    for row in csvdata:
        csvwriter.writerow(row)

print("CSV file generated: ", csvfilename)
