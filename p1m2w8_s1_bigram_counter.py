#Session 1 — The bigram counter [block] Count adjacent word pairs across a trimmed Gutenberg book, 
# reusing the W7b tokenizer: counts[(prev, word)] = counts.get((prev, word), 0) + 1. 
# Done: the ten commonest pairs print, and they look plausible (expect of the, in the, to the…). 
# Out of scope: probabilities, smoothing, punctuation handling, any second text.
import re
bigram_counts = dict()
text = open('Count_of_Mont_Cristo.txt')
text = text.read()
text = text.lower()
start = text.rfind('volume one')
end = text.rfind('footnotes:')
if start == -1 or end == -1:
    print('marker not found', start, end)
else:
    text = text[start:end]

words = re.findall(r'\w+', text)
for i in range(len(words) - 1):
    prev = words[i]
    word = words[i + 1]
    bigram_counts[(prev, word)] = bigram_counts.get((prev, word), 0) + 1

lst = list()
for key, val in bigram_counts.items():
    lst.append((val, key))
lst.sort(reverse=True)
for (val, key) in lst[:10]:
    print(val, key)

print(sum(bigram_counts.values())) 
print(len(words) - 1)

print(repr(text[:200]))
print(repr(text[-200:]))