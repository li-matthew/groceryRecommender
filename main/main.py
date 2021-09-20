import pandas as pd

# create full data file
data = pd.read_csv('/Users/matthewli/Downloads/instacart/orders.csv')
products = pd.read_csv('/Users/matthewli/Downloads/instacart/products.csv')
departments = pd.read_csv('/Users/matthewli/Downloads/instacart/departments.csv')
items = pd.read_csv('/Users/matthewli/Downloads/instacart/order_products__prior.csv')
items2 = pd.read_csv('/Users/matthewli/Downloads/instacart/order_products__train.csv')
items = items.append(items2, ignore_index=True)

test = pd.merge(items, products, on='product_id')
test = pd.merge(test, departments, on='department_id')
test = pd.merge(test, data, on='order_id')
test = test.drop(['aisle_id', 'eval_set', 'order_dow', 'days_since_prior_order'], axis=1)
test.to_csv('test.csv', index=False)