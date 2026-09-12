followers = dict()
prev = list()

import re
import random
fhand = open('Count_of_Mont_Cristo.txt')
text = fhand.read()
text = text.lower()
start = text.rfind('chapter 1.')
end = text.rfind('footnotes:')
if start == -1 or end == -1:
    print('Marker not found', start, end)
    quit()
else:
    words = re.findall(r'\w+', text[start:end])
#    print(words[:20])
#    print(words[-20:])

for i in range(len(words)-1):
    prev = words[i]
    word = words[i + 1]
    if prev not in followers:
        followers[prev] = list()
    followers[prev].append(word)

print(len(followers['of']))

current = 'the'
story = current
for i in range(50):
    current = random.choice(followers[current])
    story = story + ' ' + current
print(story)

