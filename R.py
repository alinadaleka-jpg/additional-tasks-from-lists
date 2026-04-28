a = [int(x) for x in input().split()]
pairs = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            pairs += 1
print(pairs)