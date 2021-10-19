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
from collections import defaultdict


data = pd.read_csv("csv/manipulated.csv")
print(data)

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

reader = Reader(rating_scale=(1, data["match"].max()))
dataset = Dataset.load_from_df(
    data[["product_name_x", "product_name_y", "match"]], reader
)
algo = SVD()
cross_validate(algo, dataset, measures=["RMSE", "MAE"], cv=5, verbose=True)

# Predictions
topn = []
# for x in data.aisle_x.unique():
#     temp = []
for y in data.product_name_y.unique():
    est = algo.predict("Whole Milk", y).est
    topn.append((y, est))
topn.sort(key=lambda x: x[1], reverse=True)
print(topn)

# # Auto parameter
# param_grid = {"n_epochs": [5, 10], "lr_all": [0.002, 0.005], "reg_all": [0.4, 0.6]}
# gs = GridSearchCV(SVD, param_grid, measures=["rmse", "mae"], cv=3)
# gs.fit(data)
# print(gs.best_score["rmse"])

# combination of parameters that gave the best RMSE score
# print(gs.best_params["rmse"])
