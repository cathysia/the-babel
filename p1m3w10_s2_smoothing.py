import re
import math

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
if start > end:
    print('Markers out of order', start, end)
    exit()
else: 
    words = re.findall(r'\w+', text[start:end])
    print(words[:20])
    print(words[-20:])

counts = dict()
for word in words:
    counts[word] = counts.get(word, 0) + 1

import pandas as pd
df = pd.DataFrame(counts.items(), columns=['word', 'count'])
print(df)
df = df.sort_values('count', ascending=False)
print(df[df['count']>100])
print(df.head(10))

for i in range(len(words)-1):
    prev = words[i]
    word = words[i+1]
    bigram_counts[(prev, word)] = bigram_counts.get((prev, word), 0) + 1
    word_counts[prev] = word_counts.get(prev, 0) + 1
print(word_counts['of'])
print(len(words), sum(bigram_counts.values())) 

def score(sentence):
    sw = re.findall(r'\w+', sentence.lower())
    total = 0.0
    found = 0
    missing = 0
    for i in range(len(sw) - 1):
        prev = sw[i]
        word = sw[i + 1]
        if (prev, word) in bigram_counts:
            p = (bigram_counts[(prev, word)]+1) / (word_counts[prev] + 16510)
            total = total + math.log(p)
            found = found + 1
        else:
            bigram_counts[(prev, word)] = bigram_counts.get((prev, word), 0) + 1
            p = (bigram_counts[(prev, word)]+1) / (word_counts[prev] + 16510)
            total = total + math.log(p)
    if found > 0:
        average = total / found
    else: average = 0
    return total, found, missing, average
print(score("the door is open"))
print(score("the door are open"))
print(score("she walks to the door"))
print(score("she walk to the door"))
print(score("the letter is here"))
print(score("the letter are here"))
print(score("the letter from his friends is here"))
print(score("the letter from his friends are here"))
print(score("the woman with the horses is here"))
print(score("the woman with the horses are here"))