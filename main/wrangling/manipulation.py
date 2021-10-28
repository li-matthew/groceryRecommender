import pandas as pd

# CREATE MATRIX PAIRING PRODUCTS TOGETHER

data = pd.read_csv("csv/total.csv")
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
        "product_name",
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
        .query("aisle_x < aisle_y")
        .drop(columns=["order_id"])
    )
    list.append(x)
total = pd.concat(list)
print(total)
# Create score for each match
total["match"] = total.apply(
    lambda row: min(row["reordered_x"], row["reordered_y"]), axis=1
)
total["match"] += 1
match = total[["match"]]
total = total.drop(
    [
        "reordered_x",
        "key_x",
        "reordered_y",
        "key_y",
        "match",
    ],
    axis=1,
)
print(total)

# Sort data
a = total[["aisle_x", "aisle_y"]].values
a.sort(axis=1)
newtotal = pd.DataFrame(a, total.index, total.columns)
newtotal["match"] = match
newtotal = newtotal.sort_values(["aisle_x", "aisle_y"])

newtotal = newtotal.groupby(["aisle_x", "aisle_y"]).sum().reset_index()
print(newtotal)
newtotal.to_csv("csv/manipulated.csv", index=False)
