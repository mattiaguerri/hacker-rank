# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

# vectors = []
# for i in range(2):
#     split = lines[i].split()
#     split = split[2:]vectors = []
# for i in range(2):
#     split = lines[i].split()
#     vectors.append(split)

vectors =  [[15, 12, 8, 8, 7, 7, 7, 6, 5, 3],
            [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]]

# mu_x
x = vectors[0]
N = len(x)
mu_x = sum(x) / N

# mu_y
y = vectors[1]
mu_y = sum(y) / N

# var_x
tmp = [(x_i - mu_x) ** 2 for x_i in x]
var_x = sum(tmp) / (N-1)
std_x = var_x ** .5

# var_y
tmp = [(y_i - mu_y) ** 2 for y_i in y]
var_y = sum(tmp) / (N-1)
std_y = var_y ** .5

# corr
tmp = [(x_i - mu_x) * (y_i - mu_y) for x_i, y_i in zip(x, y)]
covar = sum(tmp) / (N-1)
corr = covar / ((std_x * std_y) + 1e-7)
corr = round(corr, 3)

corr = str(corr)
sys.stdout.write(corr)
