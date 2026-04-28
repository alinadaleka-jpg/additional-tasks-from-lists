a = [int(x) for x in input().split()]
i = 0
while i < len(a) and a[i] <= 0:
    i += 1
print(i)