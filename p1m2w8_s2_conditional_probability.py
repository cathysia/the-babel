# Session 2 — Conditional probability [block] P(next | current) = count(prev, word) ÷ count(prev). 
# Needs a second dictionary of single-word counts — you already have that program from W6. 
# Done: given a word, print its five likeliest followers with probabilities. 
# Sanity check: the probabilities for one given prev should sum to ≈1.0 (≈, not ==, per the floating-point lesson). 
# Out of scope: unseen pairs / zero probabilities — that's smoothing, and it's M3's problem.
# Note it if you meet it; don't fix it.
import re
words = list()
bigram_counts = dict()
target = 'of'
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
    print(words[:20])
    print(words[-20:])
for i in range(len(words)-1):
    prev = words[i]
    word = words[i+1]
    bigram_counts[(prev, word)] = bigram_counts.get((prev, word), 0) + 1

target_counts = 0

for word in words:
    if word == target:
        target_counts = target_counts + 1


lst = list()
for (key, val) in bigram_counts.items():
    (prev, word) = key
    if prev == target:
        lst.append((val, key))
lst.sort(reverse=True)

total = list()
for counts_pair in lst[:10]:
    (val, key) = counts_pair
    print(key, 'probability=', val, '/', target_counts, val/target_counts)
    
for counts_pair in lst:
    (val, key) = counts_pair
    total.append(val/target_counts)
print(sum(total))

 