# build two lists of 300 numbers each — a loop, random.choice from a small set like [1,2,3,4,5], .append — 
# and call cosine on them. Do not change the functions.

import random
number_salad = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cat = list()
dog = list()
for i in range(300):
    cat.append(random.choice(number_salad))
    dog.append(random.choice(number_salad))

def dot(v, k):
    sum = 0
    for i in range(len(v)):
        sum = sum + v[i]*k[i]
    return sum
def length(v):
    length_before_root = 0
    for i in range(len(v)):
        length_before_root= length_before_root + v[i]**2
    length = length_before_root ** 0.5
    return length
def cosine(v, k):
    return dot(v, k)/(length(v) * length(k))

print(dot(cat, dog)) # 8472
print(length(cat)) # 100.16486409914407
print(length(dog)) # 108.06016842481785
print(cosine(cat, dog)) # 0.7827172422505839
