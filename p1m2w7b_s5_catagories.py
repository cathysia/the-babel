# Session 5 — ⭐ Answer the parked question [block]
# Run your concordance on in for both books.
# Read ~50 lines from each. Classify what the word is actually doing:
# spatial ("in the sky") · temporal ("in 1801") · discourse-marking ("in fact", "in general") · relative-clause ("in which") · other
# Tally the categories by hand. Then write 3–5 sentences: does the rate difference come from one category dominating, or is it spread evenly?
# Hold the design limit while you write: n = 2 books, so genre, author, translator, date, topic and length are all confounded. 
# No claim about "scientific prose" survives a sample of one scientific book.
# Say what your evidence can support and what it can't — that sentence is worth more than the finding.

import re

i = 0
text = open('Astronomy_for_Amateurs.txt')
text = text.read()
text = text.lower()
text = text.replace('\n', ' ')
begining = text.rfind('chapter i ')
end = text.rfind(' index ')
text = text[begining:end]
#print(text[:200])
#print(text[-200:])
total = len(re.findall(r'\bin\b', text))
step = total // 50
for m in re.finditer(r'\bin\b', text):
    if i % step == 0:
        print(text[max(0, m.start()-40) : m.end()+40])
    i = i + 1

print('\n')
i = 0
text = open('Count_of_Mont_Cristo.txt')
text = text.read()
text = text.lower()
text = text.replace('\n', ' ')
begining = text.rfind(' chapter 1. ')
end = text.rfind(' footnotes: ')
text = text[begining:end]
#print(text[:200])
#print(text[-200:])
total = len(re.findall(r'\bin\b', text))
step = total // 50
for m in re.finditer(r'\bin\b', text):
    if i % step == 0:
        print(text[max(0, m.start()-40) : m.end()+40])
    i = i + 1