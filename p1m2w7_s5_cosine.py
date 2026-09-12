#Session 5 — ⭐ Cosine, in your own code [block] · The bridge session. 
#You already wrote dot(v, w). Now add two more functions, using only tools you have (**0.5 is a square root — W2):
#length(v) → (v[0]**2 + v[1]**2) ** 0.5
#cosine(v, w) → dot(v, w) / (length(v) * length(w))
#Tests: cosine([1,1],[1,1]) → 1.0 (identical direction) · cosine([1,0],[0,1]) → 0.0 (perpendicular) · cosine([1,0],[-1,0]) → −1.0 (opposite) · 
#and the pair from your own discovery: cosine([1,1],[1,1]) vs cosine([3,4],[3,5])
#confirm the identical pair now scores higher, which the raw dot product got wrong.
#This function is the actual measure of word similarity used across NLP. In M4 you'll run it on 300-number vectors instead of 2. Same three lines.
def dot(v, w):
    return v[0]*w[0]+v[1]*w[1]
def length(v):
    return (v[0]**2 + v[1]**2) ** 0.5
def cosine(v, w):
    return dot(v, w)/(length(v) * length(w))
print(cosine([1,1],[1,1]))
print(cosine([1,0],[0,1]))
print(cosine([1,0],[-1,0]))
print(cosine([3,4],[3,5]))