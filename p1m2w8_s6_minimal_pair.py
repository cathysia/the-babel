#Session 6 — ⭐ First minimal-pair test [block] 
# Write five pairs by hand: a grammatical sentence and its ungrammatical twin, differing in one word. 
# Two or three with adjacent agreement (the key is / the key are), 
# two or three with long-distance agreement (the keys to the cabinet are / the keys to the cabinet is). 
# Write your prediction down before running anything. 
# The plan's prediction: a bigram model sees one word back, 
# so it should get adjacent agreement right and long-distance agreement wrong. 
# Done: five pairs scored, prediction recorded beforehand, 
# result recorded after — including whether the prediction survived. 
# Out of scope: more than five pairs, statistical testing, Chinese pairs (that's M3+), fixing the model when it fails. 
# A failed prediction is a result, not a bug.

# the door is open / the door are open
# she walks to the door / she walk to the door
# the letter is here / the letter are here
# the letter from his friends is here / the letter from his friends are here
# the woman with the horses is here / the woman with the horses are here

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
if start > end:
    print('Markers out of order', start, end)
    exit()
else: 
    words = re.findall(r'\w+', text[start:end])
    print(words[:20])
    print(words[-20:])
for i in range(len(words)-1):
    prev = words[i]
    word = words[i+1]
    bigram_counts[(prev, word)] = bigram_counts.get((prev, word), 0) + 1
    word_counts[prev] = word_counts.get(prev, 0) + 1
print(word_counts['of']) # 12746
print(len(words), sum(bigram_counts.values())) # 466890 466889

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

print(score('the door is open')) #(-18.189297135201578, 3, 0, -6.063099045067193)
print(score('the door are open')) #(-4.235025135195726, 1, 2, -4.235025135195726)
print('door', bigram_counts.get(('door', 'is'), 0), bigram_counts.get(('door', 'are'), 0)) #door 2 0

print(score('she walks to the door')) #(-6.350562494689752, 2, 2, -3.175281247344876)
print(score('she walk to the door')) #(-9.18377583874597, 3, 1, -3.061258612915323)
print('walks', bigram_counts.get(('she', 'walks'),0), bigram_counts.get(('she', 'walk'),0)) #walks 0 0

print(score('the letter is here')) #(-15.515692838132916, 3, 0, -5.171897612710972)
print(score('the letter are here')) #(-16.415465719054886, 3, 0, -5.471821906351629)
print('letter', bigram_counts.get(('letter','is'),0), bigram_counts.get(('letter', 'are'), 0)) # letter 4 1

print(score('the letter from his friends is here')) #(-27.413693065595808, 6, 0, -4.568948844265968)
print(score('the letter from his friends are here')) #(-25.82855929672978, 6, 0, -4.3047598827882965)
print('friends', bigram_counts.get(('friends', 'is'),0), bigram_counts.get(('friends', 'are'),0)) #friends 1 3

print(score('the woman with the horses is here')) #(-24.523798135287272, 5, 1, -4.904759627057454)
print(score('the woman with the horses are here'))#(-27.790694630340866, 6, 0, -4.631782438390144)
print('horses', bigram_counts.get(('horses', 'is'),0), bigram_counts.get(('horses', 'are'),0)) #horses 0 3


print(score('she said')) # (-3.44517717577869, 1, 0, -3.44517717577869)
print(score('she says')) # (-7.206377291472252, 1, 0, -7.206377291472252)

print(score('eyes are')) # (-5.1298987149230735, 1, 0, -5.1298987149230735)
print(score('eyes is')) # (0.0, 0, 1, 0)

print(word_counts.get('walks',0), word_counts.get('walked',0)) # 5 39
print(bigram_counts.get(('she','said'),0), bigram_counts.get(('she','says'),0)) # 43 1
print(bigram_counts.get(('count','is'),0), bigram_counts.get(('count','are'),0)) # 16 6
print(bigram_counts.get(('eyes','are'),0), bigram_counts.get(('eyes','is'),0)) # 3 0


print(score('she said the'))          # (-4.936450300308977, 2, 0, -2.4682251501544883)

print(bigram_counts[('she','said')])  # 43
print(bigram_counts[('she','says')])  # 1

import locale
print(locale.getpreferredencoding(False))