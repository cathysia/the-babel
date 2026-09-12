import random

cat = list()
dog = list()
for i in range(300):
    cat.append(random.choice(range(300)))
    dog.append(random.choice(range(300)))

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

print(dot(cat, dog)) # 6062640
print(length(cat)) # 2903.623770394505
print(length(dog)) # 2873.124779747653
print(cosine(cat, dog)) # 0.726719727484669