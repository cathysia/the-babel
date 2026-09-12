# S5 ★ Vectors, rebuilt by hand (block)
# The calibration session — hands-on, not a reread, because reading has already failed twice. 
# In code, no notes: make three 2-D word vectors by hand (cat = [3, 4], dog = [4, 4], bureaucracy = [-5, 1]), 
# run cosine() on all three pairs, and predict the ranking before running.
# Then say aloud, with the numbers on screen: what makes cat and dog similar here? 
# Not their position — their direction. Cosine ignores length, which is why it beat the raw dot product. 
# Then the leap: nothing changes if the lists hold 300 numbers instead of 2. Same function, same three lines.
# DoneThree sentences in your own words — what a vector is, what cosine measures, 
# and why 300 dimensions changes nothing about the arithmetic.
# Out Real embeddings (M4), visualization, dimensionality reduction.

cat = [3, 4]
dog = [4, 4]
bureaucracy = [-5, 1]

def dot(v, k):
    return v[0]*k[0]+v[1]*k[1]
def length(v):
    return (v[0]**2 + v[1]**2) ** 0.5
def cosine(v, k):
    return dot(v, k)/(length(v) * length(k))
print(dot(cat, dog)) # 28
print(cosine(cat, dog)) #0.9899494936611665
print(cosine(cat, bureaucracy)) #-0.43145549730400484
print(cosine(dog, bureaucracy)) #-0.5547001962252291

big_cat = [30, 40]
print(dot(big_cat, dog)) # 280
print(length(big_cat)) # 50.0
print(length(cat)) # 5.0
print(length(dog)) #5.656854249492381
print(cosine(big_cat, dog)) #0.9899494936611665
print(cosine(cat, big_cat)) # 1.0

# cosine(cat, dog)     =  28  / ( 5  × 5.657 )
# cosine(big_cat, dog) = 280  / ( 50 × 5.657 )


def dot(v, k):
    dot = 0
    for i in range(len(v)):
        dot = dot + v[i]*k[i]
    return dot
def length(v):
    length_before_root = 0
    for i in range(len(v)):
        length_before_root= length_before_root + v[i]**2
    length = length_before_root ** 0.5
    return length
def cosine(v, k):
    return dot(v, k)/(length(v) * length(k))
cat = [3, 4, 1]
dog = [4, 4, 1]
print(cosine(cat, dog)) # 0.9900436758984325

print(dot(cat, dog)) # 29
print(length(cat)) # 5.0990195135927845
print(length(dog)) # 5.744562646538029