#Session 3 — ⭐ THE CHECKPOINT (corrected) [block, protect your best morning] · On your Mac, book closed, no AI, blank file in ~/phd-journey. Read a text file and:
#print how many times ONE specific word (e.g. "the") appears
#print the total number of words
#Tools needed: file reading, .split(), a loop, an if, a counter — all taught in Ch.1–7
#Scoring: ✅ clean = runs correctly, no peeking · ✅ assisted = ≤2 quick lookups · ❌ = stuck. Report the result to Claude verbatim.
#One improvement pass (~15 min): pick ONE thing only. Candidates: handle capitals (.lower() so "The" counts as "the"); notice the punctuation problem ("the," ≠ "the" — that's tokenization, a real research topic, meet it formally in J&M Ch.2); or just rename variables so a stranger could read the code.
fname = input("Enter the filename: ")
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        #word = word.lower()
        if word == 'the' or 'the,':
            count = count + 1
print("There are",count,"of lower 'the' in the file.")