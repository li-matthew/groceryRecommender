import pandas as pd

data = pd.read_csv("csv/total.csv")

data = data[data.groupby("product_id").product_id.transform(len) > 1]
print(data["product_name"].value_counts())
# sns.histplot(data["product_name"].value_counts())
# plt.show()
#
