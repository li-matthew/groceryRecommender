import pandas as pd

# data = pd.read_csv("csv/total.csv")
# data = data.product_name.unique()

# print(data)
# category = pd.DataFrame(data, columns=["original"])
# category["category"] = category.loc[:, "original"]
# category.to_csv("csv/categories.csv")


categories = pd.read_csv("csv/cat3.csv")
count = 0
for index, row in categories.iterrows():
    if "Hot Dog" in row["original"] and row["category"] == row["original"]:
        print(row["original"])
        row["category"] = "Hot Dog"
        count = count + 1

# for index, row in categories.iterrows():
#     if "Battery" in row["category"]:
#         print(row["category"])
#         categories = categories.drop(index)
#         count = count + 1

# for index, row in categories.iterrows():
#     if row["category"] == row["original"]:
#         count = count + 1
categories = categories.sort_values(
    by=["category"], key=lambda x: x.str.len(), ascending=False
)

# print(categories.head(50))
print(count)
categories.to_csv("csv/cat3.csv", index=False)
