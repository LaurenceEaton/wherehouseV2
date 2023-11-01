import csv
import random
import pandas as pd
import numpy as np

tblsalesstatistics_data = pd.read_csv(r"C:\Users\laeat\Documents\Coding\wherehouse database stuff\tblSalesStatistics.csv")


random_multipliers = np.random.uniform(-1, 4, 100)
tblsalesstatistics_data["predict_sales"] = (tblsalesstatistics_data["SalesMonth"] * np.random.uniform(0, 4, 100)).round().astype(int)

sales_predict_generation = pd.DataFrame(tblsalesstatistics_data["predict_sales"])
sales_predict_generation.to_csv("sales_predict_data.csv")