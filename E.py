a = [int(x) for x in input().split()]
i = 0
while i < len(a) and a[i] <= 0:
    i += 1
result = (i < len(a)) * i + (i == len(a)) * -1
print(result)
