#Session 4 — ⭐ Build a concordance (KWIC) [block]
#The classic tool of corpus linguistics, and now within reach.
#Write a program that takes a target word and a file, and prints every occurrence with ~40 characters of context on each side — keyword in context.
#Tools: reading a file, re.finditer() or a loop over findall positions, string slicing (Ch.6).
#Ask if the position-finding is unclear — that's the one genuinely new bit.
#Sanity check: run it on a common word and eyeball 10 lines. Does the context look like real sentences?
import re
text = open('Astronomy_for_Amateurs.txt')
text = text.read()
text = text.lower()
text = text.replace('\n', ' ')
for m in re.finditer(r'\buniverse\b', text):
#    if m.start()-40<=0:
#        print(text[0:m.end()+40])
#    else:
#        print(text[m.start()-40:m.end()+40])
    print(text[max(0, m.start()-40) : m.end()+40])