import pandas as pd
import scipy as sp
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from surprise.model_selection import cross_validate
from sklearn.metrics import mean_squared_error
from sklearn.decomposition import PCA

# PERFORM PCA

data = pd.read_csv("csv/manipulated.csv")
print(data)

df = pd.DataFrame(
    index=data.product_name_x.unique(), columns=data.product_name_y.unique()
)
print(df)
for index, row in data.iterrows():
    # print(row["product_name"])
    df.at[row["product_name_x"], row["product_name_y"]] = row["match"]
df = df.fillna(0)
print(type(df))

pca = PCA(100)
pca.fit(df)
print(pca.components_)
print(pca.explained_variance_ratio_.sum())
