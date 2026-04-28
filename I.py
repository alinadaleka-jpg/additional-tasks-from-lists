a = [int(x) for x in input("Введіть список: ").split()]
x= int(input("Введіть число x: "))
closest = a[0]
for current in a:
    if abs(current - x) < abs(closest - x):
        closest = current
print("Найближче число:", closest)