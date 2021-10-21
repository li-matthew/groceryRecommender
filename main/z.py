import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

test = pd.read_csv("csv/test.csv")
products = pd.read_csv("csv/cat4.csv")
print(test)
print(products)

for index, row in test.iterrows():
    if row["product_name"] not in products.original.unique():
        test = test.drop(index)


test.to_csv("csv/test2.csv", index=False)
