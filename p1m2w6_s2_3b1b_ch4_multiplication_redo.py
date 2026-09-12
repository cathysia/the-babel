#def apply_matrix(a, b, c, d, v):
#    return [a*v[0] + b*v[1], c*v[0] + d*v[1]]

#once = apply_matrix(0, -1, 1, 0, [1, 0])   # first quarter-turn
#twice = apply_matrix(0, -1, 1, 0, once)    # rotate the RESULT again
#print(twice)

def applu_matrix(a, b, c, d, v):
    return[a*v[0]+b*v[1], c*v[0]+d*v[1]]
once = applu_matrix(0, -1, 1, 0, [1,1])
twice = applu_matrix(0, -1, 1, 0, once)
print(twice)