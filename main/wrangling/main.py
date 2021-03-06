import pandas as pd

# CREATE FULL DATA FILE
# data = pd.read_csv("/Users/matthewli/Downloads/instacart/orders.csv")
# products = pd.read_csv("/Users/matthewli/Downloads/instacart/products.csv")
# departments = pd.read_csv("/Users/matthewli/Downloads/instacart/departments.csv")
# items = pd.read_csv("/Users/matthewli/Downloads/instacart/order_products__prior.csv")
# items2 = pd.read_csv("/Users/matthewli/Downloads/instacart/order_products__train.csv")
# items = items.append(items2, ignore_index=True)
# aisles = pd.read_csv("/Users/matthewli/Downloads/instacart/aisles.csv")
# print("done")

# total = pd.merge(items, products, on="product_id", how="inner")
# total = pd.merge(total, departments, on="department_id", how="inner")
# total = pd.merge(total, data, on="order_id", how="inner")
# total = pd.merge(total, aisles, on="aisle_id", how="inner")
# total = total.drop(
#     ["aisle_id", "eval_set", "order_dow", "days_since_prior_order"], axis=1
# )
# total = total.sort_values(by=["order_id"])
# total.to_csv("csv/total.csv", index=False)
# test = total.sample(n=500, replace=False)

total = pd.read_csv("../csv/total.csv")
test2 = total.head(n=100000)
test2.to_csv("../csv/test3.csv", index=False)
