import re
hand = open('regex_sum_2438891.txt')
numlist = list()
count = 0
for line in hand:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    if len(numbers) == 0: continue
    for number in numbers:
        number = int(number)
        numlist.append(number)
        count = count + 1
print(count, sum(numlist))