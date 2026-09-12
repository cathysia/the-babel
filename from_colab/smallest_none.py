smallest = None
print('before', smallest)
for num in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
    print(smallest, num)
print('after', smallest, num)

smallest = None
print('before', smallest)
for num in [9, 41, 12, 3, 74, 15]:
    if smallest is None or smallest > num:
        smallest = num
    print(smallest, num)
print('after', smallest, num)