import pandas as pd

reg = pd.read_csv("regmeasures.csv")
sgd = pd.read_csv("sgdmeasures.csv")

print(reg)
rmse = []
mse = []
for x in reg["rmse"]:
    rmse.append((x, "reg"))
for x in reg["mse"]:
    mse.append((x, "reg"))
for x in sgd["rmse"]:
    rmse.append((x, "sgd"))
for x in sgd["mse"]:
    mse.append((x, "sgd"))

# rmse = dict()
# mse = dict()
# rmse["reg"] = regrmse
# rmse["sgd"] = sgdrmse
# mse["reg"] = regmse
# mse["sgd"] = sgdmse
fold = [1, 2, 3, 1, 2, 3]
rmse = pd.DataFrame(rmse, columns=["error", "type"])
mse = pd.DataFrame(mse, columns=["error", "type"])
rmse["fold"] = fold
mse["fold"] = fold
print(rmse)

rmse.to_csv("rmse.csv", index=False)
mse.to_csv("mse.csv", index=False)
