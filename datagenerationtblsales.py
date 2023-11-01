import csv
import random
from datetime import date
from datetime import timedelta

csvdata = []

def randomsaledate():
    startdate = date(2022, 1, 1)
    enddate = date(2022, 12, 31)
    randomdate = random.randint(0, (enddate - startdate).days)
    return startdate + timedelta(days=randomdate)

for i in range(1, 101):
    randomitemid = random.randint(1,100)
    itemid = "{:04}".format(randomitemid)
    orderid = "{:04}".format(i)
    saledate = randomsaledate().strftime("%Y-%m-%d")
    randomnum = random.uniform(5,100)
    saleprice = round(randomnum, 2)
    quantitysold = random.randint(1,1000)
    csvdata.append([orderid, itemid, saledate, saleprice, quantitysold])



csvfilename = "tblSales.csv"
with open(csvfilename, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["OrderID", "ItemID", "SaleDate", "SalePrice", "QuantitySold"])
    for row in csvdata:
        csvwriter.writerow(row)

print("CSV file generated: ", csvfilename)
