a = [int(x) for x in input().split()]
odds = []
for x in a:
    if x % 2 != 0:
        odds.append(x)
if len(odds) > 0:
    print(min(odds))
else:
    print(0)