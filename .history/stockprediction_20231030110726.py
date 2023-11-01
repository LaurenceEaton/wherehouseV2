import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta

class WarehousePredictor:
    def __init__(self):
        self.coefficients = None
        self.cost_history = None

    def read_data(self):
        # Read data files and preprocess them
        self.tblsalesstatistics_data = pd.read_csv("tblSalesStatistics.csv")
        self.tblsales_data = pd.read_csv("tblSales.csv")
        self.tblitems_data = pd.read_csv("tblitems.csv")
        self.sales_predict_data = pd.read_csv("sales_predict_data.csv")

        self.tblsales_data["SaleDate"] = pd.to_datetime(self.tblsales_data["SaleDate"])
        self.tblitems_data["ExpiryDate"] = pd.to_datetime(self.tblitems_data["ExpiryDate"])

        self.tblsalesstatistics_data_extract = self.tblsalesstatistics_data[["ItemID", "SalesWeek", "SalesMonth"]]
        self.tblitems_data_extract = self.tblitems_data[["ItemID", "ExpiryDate"]]

        self.tblitems_data_extract["days_to_expire"] = (self.tblitems_data["ExpiryDate"] - self.tblsales_data["SaleDate"]).dt.days
        self.tblitems_days_to_expire_extract = self.tblitems_data_extract[["ItemID", "days_to_expire"]]

        self.first_merge = pd.merge(self.tblsalesstatistics_data_extract, self.tblitems_days_to_expire_extract, on="ItemID", how="left")
        self.merged_data = self.first_merge.drop_duplicates(subset="ItemID", keep="first")
        self.concatenation_with_predict_data = pd.concat([self.merged_data, self.sales_predict_data], axis=1)
        self.normalise_data = self.concatenation_with_predict_data[["SalesWeek", "SalesMonth", "days_to_expire", "predict_sales"]]
        self.avoid_data = self.merged_data["ItemID"]
        self.normalised_data = (self.normalise_data - self.normalise_data.mean()) / self.normalise_data.std()
        self.normalised2_data = pd.concat([self.avoid_data, self.normalised_data.reset_index(drop=True)], axis=1)

    def prepare_inputs_outputs(self):
        # Prepare inputs and outputs for gradient descent
        self.inputs = self.normalised2_data.iloc[:, 1:]
        ones = np.ones([self.inputs.shape[0], 1])
        self.inputs = np.concatenate((ones, self.inputs), axis=1)
        self.outputs = self.normalised2_data["predict_sales"].values
        self.coefficients = np.zeros([1, self.inputs.shape[1]])

    def compute_cost(self):
        # Compute the cost function
        sum1 = np.power(((self.inputs @ self.coefficients.T) - self.outputs), 2)
        return np.sum(sum1) / (2 * len(self.inputs)

    def gradient_descent(self, learning_rate, iterations):
        # Perform gradient descent to optimize coefficients
        cost_history = np.zeros(iterations)
        for i in range(iterations):
            prediction_errors = self.inputs @ self.coefficients.T - self.outputs
            self.coefficients = self.coefficients - (learning_rate / len(self.inputs)) * (prediction_errors.T @ self.inputs)
            cost_history[i] = self.compute_cost()
        self.cost_history = cost_history

    def predict_sales_for_item(self, item_id_input):
        if item_id_input > 0:
            item_predicted_sales = self.normalise_data["predict_sales"].values[0]
            today = date.today()
            next_30_days = [today + timedelta(days=i) for i in range(30)]

            plt.figure(figsize=(10, 6))
            plt.plot(next_30_days, [item_predicted_sales] * 30, marker="o", color="blue", label="Predicted Sales")
            plt.xlabel("Date")
            plt.ylabel("Predicted Sales")
            plt.title(f"Predicted Sales for ItemID {item_id_input} over the next 30 days")
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.tight_layout()
            plt.legend()
            plt.show()
        else:
            print("Incorrect Item ID input")

if __name__ == "__main__":
    warehouse_predictor = WarehousePredictor()
    warehouse_predictor.read_data()
    warehouse_predictor.prepare_inputs_outputs()

    learning_rate = 0.01
    iterations = 1000
    warehouse_predictor.gradient_descent(learning_rate, iterations)

    print("Optimised coefficients:", warehouse_predictor.coefficients)
    final_cost = warehouse_predictor.compute_cost()
    print("Final cost:", final_cost)

    item_ID_input = int(input("Enter the ItemID to predict sales over the next 30 days: "))
    warehouse_predictor.predict_sales_for_item(item_ID_input)
