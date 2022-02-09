# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# lines = []
# for line in sys.stdin:
#     lines.append(line)

with open("./dataset/input.txt") as f:
    lines = f.readlines()

split = lines[0].split()
n_feats = int(split[0])
n_rows = int(split[1])

# remove first item from lines
lines.pop(0)

# collect the data in an array
data = np.empty((n_rows, n_feats+1))
for i in range(0, n_rows):
    split = lines[i].split()
    for j in range(0, n_feats+1):
        data[i, j] = split[j]
data = data.astype(float)
X = data[:, 0:n_feats]
y = data[:, n_feats]

# collect test data in an array
del lines[:n_rows]
split = lines[0].split()
n_rows = int(split[0])
lines.pop(0)
X_test = np.empty((n_rows, n_feats))
for i in range(0, n_rows):
    split = lines[i].split()
    for j in range(n_feats):
        X_test[i, j] = split[j]
X_test = X_test.astype(float)

# transform the features
poly = PolynomialFeatures(4, include_bias=False)
X_tran = poly.fit_transform(X, y)

# fit the regressor
reg = LinearRegression()
reg.fit(X_tran, y)

# transform the test features and predict
X_tran = poly.transform(X_test)
y_pred = reg.predict(X_tran)

for i in range(n_rows):
    sys.stdout.write(str(y_pred[i]) + "\n")
