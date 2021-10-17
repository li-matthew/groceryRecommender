import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("csv/total.csv")
products = pd.read_csv("/Users/matthewli/Downloads/instacart/products.csv")
departments = pd.read_csv("/Users/matthewli/Downloads/instacart/departments.csv")
print(data.columns)
# Remove non groceries
print(data.loc[data["department"] == "bulk"]["product_name"])
data = data[data.department != "personal care"]
data = data[data.department != "babies"]
data = data[data.department != "pets"]
data.to_csv("csv/v2.csv", index=False)
x = data.drop(
    [
        "order_id",
        "add_to_cart_order",
        "reordered",
        "department_id",
        "product_id",
        "department",
        "user_id",
        "order_number",
        "order_hour_of_day",
        "aisle",
    ],
    axis=1,
)
print(len(x))
products = x.product_name.unique()
products = pd.DataFrame(products, columns=["original"])
products.to_csv("csv/products.csv", index=False)
