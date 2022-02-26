# The Best Aptitude Test.

# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

lines = []
for line in sys.stdin:
    lines.append(line)

cases_num = int(lines[0])
lines.pop(0)

outputs = []
for i in range(cases_num):
    N = int(lines[0])
    y = lines[1].split()
    y = [float(x) for x in y]
    x_1 = lines[2].split()
    x_1 = [float(x) for x in x_1]
    x_2 = lines[3].split()
    x_2 = [float(x) for x in x_2]
    x_3 = lines[4].split()
    x_3 = [float(x) for x in x_3]
    x_4 = lines[5].split()
    x_4 = [float(x) for x in x_4]
    x_5 = lines[6].split()
    x_5 = [float(x) for x in x_5]
    for j in range(7):
        lines.pop(0)

    # mu_y
    mu_y = sum(y) / N
    # var_y
    tmp = [(y_i - mu_y) ** 2 for y_i in y]
    var_y = sum(tmp) / (N-1)
    std_y = var_y ** .5
    
    corr_list = []
    feats = [x_1, x_2, x_3, x_4, x_5]
    for x in feats:
        # mu_x
        mu_x = sum(x) / N
        # var_x
        tmp = [(x_i - mu_x) ** 2 for x_i in x]
        var_x = sum(tmp) / (N-1)
        std_x = var_x ** .5
    
        # corr
        tmp = [ (x_i - mu_x) * (y_i - mu_y) for x_i, y_i in zip(x, y)]
        covar = sum(tmp) / (N-1)
        corr = covar / ((std_x * std_y) + 1e-7)
        corr = round(corr, 3)

        corr_list.append(corr)
    
    corr_list = [abs(x) for x in corr_list]
    ma = max(corr_list)
    ind = corr_list.index(ma)
    outputs.append(ind+1)

for out in outputs:
    sys.stdout.write(str(out) + "\n")
