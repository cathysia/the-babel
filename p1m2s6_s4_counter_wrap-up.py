#Python touch: write dot(v, w) for two lists [x, y] — returns v[0]*w[0] + v[1]*w[1]. 
#Test: dot([1,0],[0,1]) → 0 (perpendicular), dot([1,0],[1,0]) → 1 (identical), dot([1,0],[-1,0]) → −1 (opposite).

def dot(v, w):
    return v[0]*w[0] + v[1]*w[1]
print(dot([1, 0], [0, 1]))
print(dot([1, 0], [1, 0]))
print(dot([1, 1], [1, 1]))
print(dot([3, 4], [3, 5]))