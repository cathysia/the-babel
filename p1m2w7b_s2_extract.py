#Rewrite one earlier program using regex. 
# Good candidate: extract email addresses from mbox-short.txt — you did this with .split() in Ch.8, 
# so you can compare the two approaches directly. 
# Neither is "better"; note when each is clearer.
#import re
#hand = open('mbox-short.txt')
#for line in hand:
#    line = line.rstrip()
#    lst = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z0-9]', line)
#    if len(lst) > 0: 
#        print(lst)

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    lst = re.findall('\s+[a-zA-Z0-9]+@[a-zA-Z0-9]+\s+', line)
    if len(lst) > 0: 
        print(lst)
