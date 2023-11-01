import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from datetime import timedelta

date = date.today()


tblsalesstatistics_data = pd.read_csv(
    r"C:\Users\laeat\Documents\Coding\wherehouse database stuff\tblSalesStatistics2.csv"
)
tblsales_data = pd.read_csv(
    r"C:\Users\laeat\Documents\Coding\wherehouse database stuff\tblSales.csv"
)
tblitems_data = pd.read_csv(
    r"C:\Users\laeat\Documents\Coding\wherehouse database stuff\tblitems.csv"
)
sales_predict_data = pd.read_csv(
    r"C:\Users\laeat\Documents\Coding\wherehouse database stuff\sales_predict_data.csv"
)

tblsales_data["SaleDate"] = pd.to_datetime(tblsales_data["SaleDate"])
tblitems_data["ExpiryDate"] = pd.to_datetime(tblitems_data["ExpiryDate"])

tblsalesstatistics_data_extract = tblsalesstatistics_data[
    ["ItemID", "SalesWeek", "SalesMonth"]
]
tblitems_data_extract = tblitems_data[["ItemID", "ExpiryDate"]]

tblitems_data_extract["days_to_expire"] = (
    tblitems_data["ExpiryDate"] - tblsales_data["SaleDate"]
).dt.days

tblitems_days_to_expire_extract = tblitems_data_extract[["ItemID", "days_to_expire"]]

first_merge = pd.merge(
    tblsalesstatistics_data_extract,
    tblitems_days_to_expire_extract,
    on="ItemID",
    how="left",
)

merged_data = first_merge.drop_duplicates(subset="ItemID", keep="first")
concatenation_with_predict_data = pd.concat([merged_data, sales_predict_data], axis=1)
normalise_data = concatenation_with_predict_data[
    ["SalesWeek", "SalesMonth", "days_to_expire", "predict_sales"]
]
avoid_data = merged_data["ItemID"]

normalised_data = (normalise_data - normalise_data.mean()) / normalise_data.std()

normalised2_data = pd.concat(
    [avoid_data, normalised_data.reset_index(drop=True)], axis=1
)

#################################################

inputs = normalised2_data.iloc[:, 1:]

ones = np.ones([inputs.shape[0], 1])

inputs = np.concatenate((ones, inputs), axis=1)

outputs = normalised2_data["predict_sales"].values
coefficients = np.zeros([1, inputs.shape[1]])

learningrate = 0.01
iterations = 1000


def computeCost(inputs, outputs, coefficients):
    sum1 = np.power(((inputs @ coefficients.T) - outputs), 2)
    return np.sum(sum1) / (2 * len(inputs))


#################################################


def gradientDescent(inputs, outputs, coefficients, iterations, learningrate):
    costhistory = np.zeros(iterations)
    for i in range(iterations):
        predictionerrors = inputs @ coefficients.T - outputs
        coefficients = coefficients - (learningrate / len(inputs)) * (
            predictionerrors.T @ inputs
        )
        costhistory[i] = computeCost(inputs, outputs, coefficients)

    return coefficients, costhistory


result = gradientDescent(inputs, outputs, coefficients, iterations, learningrate)


optimisedcoefficients = result[0]
costhistory = result[1]

print("Optimised coefficients:", optimisedcoefficients)
finalcost = computeCost(inputs, outputs, optimisedcoefficients)
print("Final cost:", finalcost)

#################################################

item_ID_input = int(input("Enter the ItemID to predict sales over the next 30 days: "))

if item_ID_input > 0:
    item_predicted_sales = normalise_data["predict_sales"].values[0]

    today = date.today()
    next_30_days = [today + timedelta(days=i) for i in range(30)]

    plt.figure(figsize=(10, 6))
    plt.plot(next_30_days, [item_predicted_sales] * 30, marker="o", color="blue", label="Predicted Sales")
    plt.xlabel("Date")
    plt.ylabel("Predicted Sales")
    plt.title(f"Predicted Sales for ItemID {item_ID_input} over the next 30 days")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    plt.show()
else:
    print("Incorrect Item ID input")

    