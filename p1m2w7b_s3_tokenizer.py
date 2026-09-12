#Session 3 — Fix the tokenizer [block] · 
#The punctuation problem you observed in W4 and again in W7 ("the," ≠ "the"), now fixable.
#Rebuild your word counter using re.findall(r'\w+', text.lower()) instead of .split().
#Run it on the same Gutenberg book and diff the results against your old counts. 
#How much did the numbers move? Which words changed rank?
#Then the honest limit: \w+ splits don't into don and t, and mangles hyphenated words. 
#There is no correct tokenizer — every choice is a research decision with consequences.
#This is J&M Ch.2's actual thesis, arriving early through your own hands.


fhand = open('Count_of_Mont_Cristo.txt')
counts=dict()
lst = list()
for line in fhand:
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1
        if word == 'you':
            print(line)
total = sum(counts.values())
for key, val in counts.items():
    lst.append((val, key))
lst.sort(reverse=True)
top = lst[:10]
for single_word in top:
    print(single_word)
print(total)

import re
fhand = open('Count_of_Mont_Cristo.txt')
counts = dict()
lst = list()
for line in fhand:
    line = line.lower()
    line = line.rstrip()
    words = re.findall(r'\w+', line)
    for word in words:
        counts[word] = counts.get(word,0)+1
total = sum(counts.values())
for key, val in counts.items():
    lst.append((val, key))
lst.sort(reverse=True)
top = lst[:10]
for single_word in top:
    print(single_word)
print(total)