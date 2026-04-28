a = [int(x) for x in input().split()]
count = 0
for i in range(len(a)):
    is_new = True
    for j in range(i):
        if a[i] == a[j]:
            is_new = False
            break
    if is_new:
        count += 1
print(count)