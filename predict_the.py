# Enter your code here. Read input from STDIN. Print output to STDOUT
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

import numpy as np
import pandas as pd
import sys

values = []
for line in sys.stdin:
    val = float(line)
    values.append(val)

n = 50
data = []
for i in range(n, len(values)):
    row = values[i-n:i+1]
    data.append(row)

data = np.array(data, dtype="float")
X = data[:, 0:n]
y = data[:, n]

# regr = LinearRegression().fit(X, y)
regr = RandomForestRegressor(n_estimators=300, random_state=0)
regr.fit(X, y)
X_pre = X[-1, :]
X_pre = np.expand_dims(X_pre, 0)

for i in range(30):
    pre = regr.predict(X_pre)
    print(int(pre[0]))
    X_pre[0, 0:-1] = X_pre[0, 1:]
    X_pre[0, -1] = pre
