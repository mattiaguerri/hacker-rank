# slope of the regression line
# slope = corr * (std_y / std_x)

import sys

vectors =  [[15, 12, 8, 8, 7, 7, 7, 6, 5, 3],
            [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]]

# mean_0
n = len(vectors[0])
mean_0 = sum(vectors[0]) / n

# mean_1
total = sum(vectors[1])
mean_1 = total / len(vectors[1])

# variance_0
total = 0
for i in range(n):
    total += (vectors[0][i] - mean_0) ** 2
var_0 = total / (n-1)
std_0 = var_0 ** .5

# variance 1
total = 0
for i in range(n):
    total += (vectors[1][i] - mean_1) ** 2
var_1 = total / (n-1)
std_1 = var_1 ** .5

# corr
total = 0
for i in range(n):
    total += (vectors[0][i] - mean_0) * (vectors[1][i] - mean_1)
covar = total / (n-1)
cor = covar / (std_0 * std_1)

m = cor * (std_1 / std_0)
m = round(m, 3)

sys.stdout.write(str(m))
