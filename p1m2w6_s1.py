#Write apply_matrix(a, b, c, d, v) taking four numbers and a list [x, y], returning [a*x + b*y, c*x + d*y]. 
#(Four separate numbers, not nested lists — nested lists work but are fiddlier; do the simple version first.)
#Test 1 — identity: apply_matrix(1, 0, 0, 1, [3, 4]) → [3, 4], nothing moves.
#Test 2 — 90° rotation: apply_matrix(0, -1, 1, 0, [1, 0]) → [0, 1]. The arrow pointing right now points up. Your code just rotated space.
#Test 3 — the one to sit with: run the rotation on [0, 1] and predict the answer before running.
#Target after this: "a matrix IS the transformation, written as where the basis vectors land" — not "the arguments of a function."

def apply_matrix(a, b, c, d, v):
     return(a*v[0]+ b*v[1], c*v[0] + d*v[1])
print(apply_matrix(1, 0, 0, 1, [3, 4]))
print(apply_matrix(0, -1, 1, 0, [1, 0]))
print(apply_matrix(0, -1, 1, 0, [0, 1]))