import pandas as pd
import scipy as sp
import numpy as np
from sklearn.decomposition import TruncatedSVD
import seaborn as sns
import matplotlib.pyplot as plt
from surprise import SVD
from surprise.model_selection import cross_validate
from surprise.model_selection import GridSearchCV
from surprise import Reader
from surprise import Dataset
from surprise import KNNBasic

data = pd.read_csv("csv/test.csv")
print(data)
print(len(data.product_name.unique()))

df = data.drop(
    [
        "product_id",
        "add_to_cart_order",
        "department",
        "department_id",
        "user_id",
        "order_number",
        "order_hour_of_day",
    ],
    axis=1,
)
df = df.groupby(by="order_id")
list = []

# Map items to items
for group in df:
    temp = group[1]
    x = (
        pd.merge(group[1].assign(key=1), group[1].assign(key=1), on="order_id")
        .query("product_name_x < product_name_y")
        .drop(columns=["order_id"])
    )
    list.append(x)
total = pd.concat(list)

# Create score for each match
total["match"] = total.apply(
    lambda row: min(row["reordered_x"], row["reordered_y"]), axis=1
)
total["match"] += 1
match = total[["match"]]
total = total.drop(
    ["reordered_x", "aisle_x", "key_x", "reordered_y", "aisle_y", "key_y", "match"],
    axis=1,
)
print(total)

# Sort data
a = total[["product_name_x", "product_name_y"]].values
a.sort(axis=1)
newtotal = pd.DataFrame(a, total.index, total.columns)
newtotal["match"] = match
newtotal = newtotal.sort_values(["product_name_x", "product_name_y"])
newtotal.to_csv("csv/manipulated.csv", index=False)
