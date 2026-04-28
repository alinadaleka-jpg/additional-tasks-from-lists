a = [int(x) for x in input().split()]
idx_min = 0
idx_max = 0
for i in range(1, len(a)):
    if a[i] < a[idx_min]:
        idx_min = i
    if a[i] > a[idx_max]:
        idx_max = i
temp = a[idx_min]
a[idx_min] = a[idx_max]
a[idx_max] = temp
print(*a)