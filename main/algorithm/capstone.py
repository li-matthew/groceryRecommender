import numpy as np
import pandas as pd
from six import iteritems
from collections import defaultdict

datas = pd.read_csv("../csv/testmanipulated.csv")
rawRatings = []
for (uid, iid, r) in datas.itertuples(index=False):
    rawRatings.append((uid, iid, float(r), None))

indices = np.arange(len(rawRatings))
splits = 5
start = 0
stop = 0
cv = []
testMeasures = []
components = 100
foldCount = 1


lr = 0.005
reg = 0.02
epochs = 20

# Split Folds
for fold in range(splits):
    start = stop
    stop = stop + (len(indices) // splits)
    if fold < len(indices) % splits:
        stop = stop + 1
    train = []
    test = []
    indexes = []
    for value in indices[:start]:
        indexes.append(value)
    for value in indices[stop:]:
        indexes.append(value)
    for i in indexes:
        train.append(rawRatings[i])
    for i in indices[start:stop]:
        test.append(rawRatings[i])
    rawUsers = {}
    rawItems = {}
    u = 0
    i = 0
    ur = defaultdict(list)
    ir = defaultdict(list)
    for urid, irid, r, timestamp in train:
        try:
            uid = rawUsers[urid]
        except KeyError:
            uid = u
            rawUsers[urid] = u
            u += 1
        try:
            iid = rawItems[irid]
        except KeyError:
            iid = i
            rawItems[irid] = i
            i += 1
        ur[uid].append((iid, r))
        ir[iid].append((uid, r))
    users = len(ur)
    items = len(ir)
    ratings = len(train)
    trainset = [
        ur,
        ir,
        users,
        items,
        ratings,
        (1, datas["match"].max()),
        rawUsers,
        rawItems,
    ]
    testset = []
    for (ruid, riid, r_ui_trans, _) in test:
        testset.append((ruid, riid, r_ui_trans))
    cv.append((trainset, testset))

# SVD on each Fold
for (trainset, testset) in cv:
    print("Fold " + str(foldCount))
    rng = np.random.mtrand._rand
    bu = np.zeros(trainset[2], np.double)
    bi = np.zeros(trainset[3], np.double)
    pu = rng.normal(0, 0.1, (trainset[2], components))
    qi = rng.normal(0, 0.1, (trainset[3], components))

    # SGD
    sgde = []
    allRatings = []
    err = None
    dot = None
    puf = None
    qif = None
    u = None
    i = None
    f = None
    r = None
    for u, ur in iteritems(trainset[0]):
        for i, r in ur:
            allRatings.append((u, i, r))
    temp = []
    for u, i, r in allRatings:
        temp.append(r)
    mean = np.mean(temp)
    print(mean)
    for epoch in range(epochs):
        e = []
        for u, i, r in allRatings:
            # compute current error
            dot = 0  # <q_i, p_u>
            for f in range(components):
                dot += qi[i, f] * pu[u, f]
            err = r - (mean + bu[u] + bi[i] + dot)
            # print(err * err)
            e.append(err * err)

            # update biases
            bu[u] += lr * (err - reg * bu[u])
            bi[i] += lr * (err - reg * bi[i])
            # print(bu)
            # update factors
            for f in range(components):
                puf = pu[u, f]
                qif = qi[i, f]
                pu[u, f] += lr * (err * qif - reg * puf)
                qi[i, f] += lr * (err * puf - reg * qif)
        mse = np.mean(e)
        rmse = np.sqrt(mse)
        sgde.append(rmse)
        # print(rmse)

    predictions = []
    for (uid, iid, ui) in testset:
        try:
            iuid = rawUsers[uid]
        except KeyError:
            iuid = str(uid)
        try:
            iiid = rawUsers[iid]
        except KeyError:
            iiid = str(iid)
        details = {}
        allRatings = []
        for u, u_ratings in iteritems(trainset[0]):
            for i, r in u_ratings:
                allRatings.append(r)
        est = np.mean(allRatings)
        if trainset[0] == iuid:
            est += bu[iuid]
        if trainset[1] == iiid:
            est += bi[iiid]
        if trainset[0] == iuid and trainset[1] == iiid:
            est += np.dot(qi[iiid], pu[iuid])
        lower = 1
        higher = datas["match"].max()
        est = min(higher, est)
        est = max(lower, est)
        pred = [uid, iid, ui, est]
        predictions.append(pred)
        # print(pred)

    # Error
    measures = dict()
    mse = []
    mae = []
    for pred in predictions:
        mse.append(float((pred[2] - pred[3]) ** 2))
        mae.append([float(abs(pred[2] - pred[3]))])
    mse = np.mean(mse)
    mae = np.mean(mae)
    rmse = np.sqrt(mse)
    measures["rmse"] = rmse
    measures["mse"] = mse
    measures["mae"] = mae
    print(measures)
    foldCount += 1
    print(sgde)
    print(np.mean(sgde))
# Predictions
# topn = []
# # for y in datas.product_name_y.unique():

# # if x[0] == "Whole Milk":
# #     topn.append((x[1], x[3]))
# # est = algo.predict("Whole Milk", y).est
# # topn.append((y, est))
# # topn.sort(key=lambda x: x[1], reverse=True)
# print(topn)
# for x in predictions:
#     print(x)
