import pandas as pd
import scipy as sp
import numpy as np
from sklearn.decomposition import TruncatedSVD
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.utils.extmath import randomized_svd
from surprise import SVD
from surprise.model_selection import cross_validate
from surprise.model_selection import GridSearchCV
from surprise import Reader
from surprise import Dataset
from surprise import KNNBasic
from collections import defaultdict
from scipy.sparse.linalg import svds
from sklearn.metrics import mean_squared_error

# PERFORM SVD

data = pd.read_csv("csv/manipulated.csv")
print(data)

# S
df = pd.DataFrame(
    index=data.product_name_x.unique(), columns=data.product_name_y.unique()
)
print(df)
for index, row in data.iterrows():
    # print(row["product_name"])
    df.at[row["product_name_x"], row["product_name_y"]] = row["match"]
df = df.fillna(0)
print(type(df))

# Scipy
# U, s, V = svds(df.to_numpy().astype(np.double), 100, return_singular_vectors=True)
# print(U.shape)
# diag = np.diag(s)
# pred = np.dot(np.dot(U, diag), V)
# preds_df = pd.DataFrame(pred, columns=df.columns, index=df.index)
# print(preds_df.loc["1% Lowfat Milk"].sort_values(ascending=False))

# Scikit
# find number of components
# y = []
# temp = 0
# init = 1
# while temp < 0.9:
#     svd = TruncatedSVD(n_components=init)
#     svd.fit(df)
#     transformed = svd.transform(df)
#     # print(transformed)
#     # print(svd.explained_variance_ratio_)
#     y.append(svd.explained_variance_ratio_.sum())
#     temp = svd.explained_variance_ratio_.sum()
#     init = init + 1
# print(init)
# sns.scatterplot(range(1, init), y)
# # sns.scatterplot(data=svd.singular_values_)
# plt.show()

# svd

svd = TruncatedSVD(df)
cross_validate(
    svd,
)

# U, s, V = randomized_svd(df.to_numpy(), n_components=100)
# print(U.shape)
# # get predictions
# diag = np.diag(s)
# pred = np.dot(np.dot(U, diag), V)
# preds_df = pd.DataFrame(pred, columns=df.columns, index=df.index)
# print(preds_df.loc["1% Lowfat Milk"].sort_values(ascending=False))
# predict = pd.DataFrame(
#     index=data.product_name_x.unique(), columns=data.product_name_y.unique()
# )
# # create prediction matrix
# for x in data.product_name_x.unique():
#     for y in data.product_name_y.unique():
#         predict.at[x, y] = preds_df.loc[x][y]
# print(predict)
# print(mean_squared_error(df.to_numpy(), predict.to_numpy()))


# SURPRISE METHOD
# Item x Item

# reader = Reader(rating_scale=(1, data["match"].max()))
# dataset = Dataset.load_from_df(
#     data[["product_name_x", "product_name_y", "match"]], reader
# )
# algo = SVD()
# cross_validate(algo, dataset, measures=["RMSE", "MAE"], cv=5, verbose=True)

# # Predictions
# topn = []
# # for x in data.aisle_x.unique():
# #     temp = []
# for y in data.product_name_y.unique():
#     est = algo.predict("Whole Milk", y).est
#     topn.append((y, est))
# topn.sort(key=lambda x: x[1], reverse=True)
# print(topn)

# # # Auto parameter
# # param_grid = {"n_epochs": [5, 10], "lr_all": [0.002, 0.005], "reg_all": [0.4, 0.6]}
# # gs = GridSearchCV(SVD, param_grid, measures=["rmse", "mae"], cv=3)
# # gs.fit(data)
# # print(gs.best_score["rmse"])

# # combination of parameters that gave the best RMSE score
# # print(gs.best_params["rmse"])
