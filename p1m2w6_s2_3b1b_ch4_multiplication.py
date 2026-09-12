#apply your rotation matrix twice in a row to [1, 0]
#see where it lands (180° — predict first)

def apply_matrix(a, b, c, d, e, f, g, h, v):
    return((a*e+b*g)*v[0]+(a*f+b*h)*v[1], (c*e+d*g)*v[0] + (c*f+d*h)*v[1])
print(apply_matrix(1, 1, 0, 1, 0, -1, 1, 0, [1, 0]))