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

print(len(counts))

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
    for i in range(len(sw) - 1):
        prev = sw[i]
        word = sw[i + 1]
        p = (bigram_counts.get((prev, word),0) + 1) / (word_counts.get(prev,0) + len(counts))
        total = total + math.log(p)
    return total

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

print(bigram_counts.get(('door','is'),0))
print(bigram_counts.get(('door','are'),0))
print(bigram_counts.get(('she','walks'),0))
print(bigram_counts.get(('she','walks'),0))
print(bigram_counts.get(('letter','is'),0))
print(bigram_counts.get(('letter','are'),0))
print(bigram_counts.get(('friends','is'),0))
print(bigram_counts.get(('friends','are'),0))
print(bigram_counts.get(('horses','is'),0))
print(bigram_counts.get(('horses','are'),0))