from bisect import bisect_left

ls = [1, 23, 46, 77, 77, 100]
ind = bisect_left(ls, 47)
print(ind)