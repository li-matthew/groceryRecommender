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
# print(len(data.order_id.unique()))
print(len(data.product_name.unique()))

# SKLEARN METHOD
# df = pd.DataFrame(index=data.order_id.unique(), columns=data.product_name.unique())
# print(df)
# for index, row in data.iterrows():
#     print(row["product_name"])
#     df.at[row["order_id"], row["product_name"]] = row["reordered"] + 1
# df = df.fillna(0)
# print(df)
# svd = TruncatedSVD(n_components=32)
# svd.fit(df)
# transformed = svd.transform(df)
# print(transformed)
# sns.scatterplot(data=svd.singular_values_)
# plt.show()

# SURPRISE METHOD
# Item x Item
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
for group in df:
    temp = group[1]
    x = (
        pd.merge(group[1].assign(key=1), group[1].assign(key=1), on="order_id")
        .query("product_name_x < product_name_y")
        .drop(columns=["order_id"])
    )
    list.append(x)
total = pd.concat(list)

total["match"] = total.apply(
    lambda row: min(row["reordered_x"], row["reordered_y"]), axis=1
)
total["match"] += 1
total = total.drop(
    [
        "reordered_x",
        "aisle_x",
        "key_x",
        "reordered_y",
        "aisle_y",
        "key_y",
    ],
    axis=1,
)
print(total)
print(total.sort_values("match"))
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(
    total[["product_name_x", "product_name_y", "match"]], reader
)
algo = SVD()
cross_validate(algo, data, measures=["RMSE", "MAE"], cv=5, verbose=True)
# param_grid = {"n_epochs": [5, 10], "lr_all": [0.002, 0.005], "reg_all": [0.4, 0.6]}
# gs = GridSearchCV(SVD, param_grid, measures=["rmse", "mae"], cv=3)
# gs.fit(data)
# print(gs.best_score["rmse"])

# # combination of parameters that gave the best RMSE score
# print(gs.best_params["rmse"])
