fhand = open('Chinese_Text.txt', encoding = 'utf-8')
text = fhand.read()

import re
import random
start = text.rfind('第一回')
end = text.rfind('休笑世人痴')
if start == -1 or end == -1:
    print('Marker Not Found', start, end)
    exit()
else:
    words = text[start:end]

followers = dict()

for i in range(len(words)-1):
    prev = words[i]
    word = words[i + 1]
    if prev not in followers:
        followers[prev] = list()
    followers[prev].append(word)

total = 0
for key in followers:
    total = total + len(followers[key])
print(total)
print(len(words)-1)

current = '的'
story = current
for i in range(100):
    current = random.choice(followers[current])
    story = story + current
print(story)