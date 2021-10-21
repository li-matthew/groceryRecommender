import pandas as pd

categories = pd.read_csv("csv/categories.csv")
products = pd.read_csv("csv/products.csv")
print(categories)
print(products)

for index, row in categories.iterrows():
    if row["original"] not in products.original.unique():
        categories = categories.drop(index)
        print(row["original"])

categories.to_csv("csv/cat2.csv", index=False)
