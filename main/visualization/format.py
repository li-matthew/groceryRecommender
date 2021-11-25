import pandas as pd

reg = pd.read_csv("../csv/regmeasures.csv")
sgd = pd.read_csv("../csv/sgdmeasures.csv")

print(reg)
rmse = []
mae = []
for x in reg["rmse"]:
    rmse.append((x, "reg"))
for x in reg["mae"]:
    mae.append((x, "reg"))
for x in sgd["rmse"]:
    rmse.append((x, "sgd"))
for x in sgd["mae"]:
    mae.append((x, "sgd"))

# rmse = dict()
# mae = dict()
# rmse["reg"] = regrmse
# rmse["sgd"] = sgdrmse
# mae["reg"] = regmae
# mae["sgd"] = sgdmae
fold = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
rmse = pd.DataFrame(rmse, columns=["error", "type"])
mae = pd.DataFrame(mae, columns=["error", "type"])
rmse["fold"] = fold
mae["fold"] = fold
print(rmse)

rmse.to_csv("../csv/rmse.csv", index=False)
mae.to_csv("../csv/mae.csv", index=False)
