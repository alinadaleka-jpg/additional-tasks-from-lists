heights = [int(x) for x in input().split()]
x = int(input())
i = 0
while i < len(heights) and heights[i] >= x:
    i += 1
print(i + 1)