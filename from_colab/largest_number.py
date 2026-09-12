largest = None
print('before', largest)
for value in [9, 41, 12, 3, 74, 15]:
    if largest is None or value > largest:
        largest = value
        print(largest, value)
print('after', largest)