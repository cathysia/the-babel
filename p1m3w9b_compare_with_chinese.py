import re
import random

bigram_counts = dict()
word_counts = dict()
fhand = open('Count_of_Mont_Cristo.txt')
text = fhand.read()
text = text.lower()
start = text.rfind('chapter 1.')
end = text.rfind('footnotes:')
if start == -1 or end == -1:
    print('Marker Not Found', start, end)
    exit()
else: 
    words = re.findall(r'\w+', text[start:end])

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

current = 'the'
story = current
for i in range(100):
    current = random.choice(followers[current])
    story = story + ' ' + current
print(story)