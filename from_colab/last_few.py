while True:
    line = input('this is:')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('DONE!')

s = 'a\n b\r c\t d'
print(s)
print('c\t')

import math
print(math.log(math.e))