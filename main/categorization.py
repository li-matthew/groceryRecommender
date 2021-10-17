import pandas as pd

# data = pd.read_csv("csv/total.csv")
# data = data.product_name.unique()

# print(data)
# category = pd.DataFrame(data, columns=["original"])
# category["category"] = category.loc[:, "original"]
# category.to_csv("csv/categories.csv")


categories = pd.read_csv("csv/categories.csv")
count = 0
for index, row in categories.iterrows():
    if "Caesar Salad" in row["category"]:
        row["category"] = "Caesar Salad"
        count = count + 1
categories = categories.sort_values(
    by=["category"], key=lambda x: x.str.len(), ascending=False
)

print(categories.head(50))
print(count)
categories.to_csv("csv/categories.csv", index=False)
