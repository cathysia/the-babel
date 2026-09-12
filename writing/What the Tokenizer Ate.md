What the tokenizer ate

There are two obvious ways to split a book into words, and on one book they disagree about seven thousand of them.

I tokenized The Count of Monte Cristo twice. Python's .split() cuts at whitespace and leaves everything else attached: 464,025 words. A regular expression, \w+, keeps runs of letters and digits and discards the rest: 471,186. Both are defensible. Neither is a bug.

I assumed the gap was contractions. .split() leaves don't whole; \w+ shreds it into don and t. That seemed the obvious source of seven thousand extra tokens.

It wasn't. I took the word with the largest gap — you, which \w+ finds 2,235 more times — and looked at what was attached to each occurrence. Opening quotation marks accounted for 34%. Trailing commas, 31%. Sentence-final punctuation, 28%. Em-dashes, 6%. Contractions: 0.4%. My intuition was wrong by two orders of magnitude.

Sorted by gap size, the words come out in an order that isn't random: you 37%, he 13%, the 2%, his 1%. That is the order of how often each word sits at the edge of a quotation or a clause. you is vocative and it ends questions; the almost never ends anything, because English obliges it to have a noun on its right. So a word's .split() shortfall is a readout of its syntactic distribution — the tokenizer is accidentally measuring grammar.

What I can't claim: one book, one translation, one language, and a nineteenth-century one at that. A modern corpus with fewer quotation marks would give different numbers. \w+ is no clean baseline either — underscore is a word character, so Gutenberg's italics markup survives as data. And I sampled the mechanism from a single word; you may not be typical.

330 words. Now look at what it does.

It opens at the disagreement, not at me. No "I've been learning Python." The first sentence is a fact that makes you want the second one.

Numbers live inside sentences. Not a table. "Contractions: 0.4%" lands because the sentence before it built the expectation that contractions were the answer.

The wrong idea gets stated in full before the right one. That's the whole engine. A reader who never hears what you expected can't feel the correction — they just get a list of percentages.

"What I can't claim" is specific, not modest. Not "of course this is only preliminary." Instead: this book, this century, this one sampled word. Naming the limits precisely is what makes the rest credible.

Your turn, same shape:

Beat	Yours
The tension	A model that sees one word back; a rule that reaches across four
What I did	Bigram model from scratch, five sessions, 466,891 bigrams, no libraries
What I predicted	Adjacent agreement right, long-distance wrong — written down first
What happened	4/4 and 0/2
The clean case	friends — six bigrams both sides, fair fight, model still wrong
The correction	The zero cliff: −10.25 for seen-once, 0.00 for never-seen, scrambled sentence wins
Limits	Single-digit counts, one book, count are probably vocative, two pairs untestable