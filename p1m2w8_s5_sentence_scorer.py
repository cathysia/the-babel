#Session 5 — The sentence scorer [block] 
# A sentence's probability is the product of its conditionals. 
# Multiplying many small numbers underflows, so sum the logs instead. 
# New tool: math.log — and this is your Month 1 math becoming executable: 
# Σ notation is the loop, log-probabilities are negative because probabilities are < 1. 
# Done: score(sentence) returns a number; 
# a plainly English sentence scores higher (less negative) than a scrambled one. 
# Out of scope: normalizing for sentence length, perplexity, 
# handling unseen bigrams gracefully (park it — score what you can).

import math
#print(math.log(0.243))
#print(math.log(0.052))
#print(math.log(0.243*0.052))
#print(math.log(0.243)+math.log(0.052))

import re

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
#    print(words[:20])
#    print(words[-20:])
for i in range(len(words)-1):
    prev = words[i]
    word = words[i+1]
    bigram_counts[(prev, word)] = bigram_counts.get((prev, word), 0) + 1
    word_counts[prev] = word_counts.get(prev, 0) + 1


def score(sentence):
    sw = re.findall(r'\w+', sentence.lower())
    total = 0.0
    found = 0
    missing = 0
    for i in range(len(sw) - 1):
        prev = sw[i]
        word = sw[i + 1]
        if (prev, word) in bigram_counts:
            p = bigram_counts[(prev, word)]/word_counts[prev]
            total = total + math.log(p)
            found = found + 1
        else:
            missing = missing + 1
    if found > 0:
        average = total / found
    else: average = 0
    return total, found, missing, average

print(score('of the'))
print(math.log(3100/12746))

print(score('the count was in the room'))
print(score('room the the was count in'))
print(score('the the'))