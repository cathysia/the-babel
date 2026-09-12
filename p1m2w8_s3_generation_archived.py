#Session 3 — Generation [block] Pick a starting word, sample the next from its distribution, repeat ~50 times. 
# New tool: random.choice — give it a list, it returns one item at random. 
# That's the whole API. Done: two paragraphs printed side by side — one sampled from single-word frequencies (word salad), one from bigrams (eerily English-shaped). 
# Read both aloud. Out of scope: weighted sampling done properly (random.choices with weights) — a repeated-list approximation is fine here. Trigrams. 
# Making the output good.
# Session 3 is generation, and it's the fun one. 
# Two paragraphs printed side by side — unigram word salad against bigram output that sounds unnervingly like English without meaning anything.
# Read them aloud. That contrast is Shannon's 1948 experiment, reproduced on your own machine, and it's the first time the instrument will do something that feels alive.

import random
import re

fhand = open('Count_of_Mont_Cristo.txt')
text = fhand.read()
text = text.lower()
start = text.rfind('chapter 1.')
end = text.rfind('footnotes:')
if start == -1 or end == -1:
    print('Marker not found', start, end)
    quit()
else:
    words = re.findall(r'\w+', text)
#    print(words[:20])
#    print(words[-20:])

current_word = 'the'
follower = list()


word_salad = current_word 


for i in range(len(words)-1):
    if words[i] == current_word:
        following_word = words[i+1]
        follower.append(following_word)
    else: continue

for r in range(50):
        next = random.choice(follower)
        for i in range(len(words)-1):
            if words[i] == next:
                next_next = words[i+1]
                follower.append(next_next)
            else: continue
        word_salad = word_salad + ' ' + next    
        current_word = next

print(word_salad)
        