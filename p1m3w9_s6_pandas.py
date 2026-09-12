import re
bigram_counts = dict()
text = open('Count_of_Mont_Cristo.txt')
text = text.read()
text = text.lower()
start = text.rfind('volume one')
end = text.rfind('footnotes:')
if start == -1 or end == -1:
    print('marker not found', start, end)
    exit()
else:
    text = text[start:end]

counts = dict()
words = re.findall(r'\w+', text)
for word in words:
    counts[word] = counts.get(word,0)+1

import pandas as pd
df = pd.DataFrame(counts.items(), columns=['word', 'count'])
print(df)
df = df.sort_values('count', ascending=False)
print(df[df['count']>100])
print(df.head(10))