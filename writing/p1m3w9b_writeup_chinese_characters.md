
When you moved from English to Chinese, what step disappeared, and why?
Why does the Chinese output look better than the English — and is it actually better?
What did you see in the generated Chinese text?
What did you call a character at first, and what is the better word for it?
Who gets to decide where a Chinese word ends?
What does BPE do about this problem?


Headline: No tokenization in Chinese processing makes the result very different with English.

I generated an text by character iteration from 紅樓夢, the processed 紅樓夢 and there is an English model to compare, I use Count of Mounte Cristo. Unlike English corpus, tokenization in Chinese processing is skipped. Because in Chinese there's no space between words or characters; and python string is a sequence of characters, so it makes no difference to tokenize it. Besides this, they are built same way. 
Te results look different: in English tokenization trim all punctuation, and split clitics, except for underscores--they are with characters; but when I process Chinese text, the punctuation survived, because there's no tokenization processes in Chinese model.
The Chinese model result comes back with a string of giberrish, looks like a sentence but makes no sense. However, some people names come together: 寶釵, 林姑娘, 黛玉, etc. In the meantime there are also some segmentation ambiguity: 賈珍珠: as 賈珍 is a name and 珍珠 is a word with two morphemes("pearl"). The bigram model can only remember one character back. when 黛 is followed by 玉 every time, it isn't the model knowing a name; it's that's the most likely bigram in the model. words are where the chain has nowhere else to go.
A character in Chinese we call it "hanzi", but a better word probably is morpheme. It's not 100% overlapped with morpheme though, there are lots of examples where one single character can't be a meaningful morpheme. e.g. 花剌子模,	徘徊, 逍遙, 葡萄, etc. 
So who decides whre a Chinese word ends? Annotation standards disagree; native speakers agree at ~0.75 (Sproat, Shih, Gale & Chang 1996). While in BPE, it let the data decide whre the words end.
