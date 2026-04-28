a = [int(x) for x in input().split()]
positive_numbers = [x for x in a if x > 0]
print(min(positive_numbers))