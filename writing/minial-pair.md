

The tension
What I did
What I predicted
What happened
The clean case
The correction
Limits

Headline: adjacent agreement 1/3, long distance 1/2: bigram score is close to prediction but hard to tell a story

I wrote 5 pairs sentences to test in a bigram model of 466889, from Count of Mont Cristo. Since the bigram model only sees one word back, it should get grammatical score higher than ungramatical one in adjacent agreement paires and ungramatical one  score higher than gramaticall one in long-distance agreement.

I predicted that should get gramatical sentences higher than their ungramatical twins.

In the 5 pairs, 3 are adjacent agreements and 2 are long-distance.

In 3 pairs of adjacent agreements: 'door is' scores significantly lower than 'door are': -18.189297135201578 and -4.235025135195726. 3 bigrams found in the first one and 0 missing, while the latter one have only 1 found and 2 missing: Missing ones score 0, better than any prababiliy in log which are naturally negative. So I devided the total number by the found number and got average number for each bigram, it's still the ungramatical one 'the door are open' score higher: -4.235025135195726>-6.063099045067193.

I searched 'door is' and 'door are' two bigrams in the book, and found 2 'door is' and 0 'door are'. The gramatical bigram wins the count. But the bigram scores can't tell the story. 

The second adjacent agreement, 'she walks to the door' scores higher than 'she walk to the door', -6.350562494689752 > -9.18377583874597, while the gramatical sentence has 2/2 found and missing while the ungramatical one has 3/1, average score the gramatical one(-3.175281247344876) is actually lower than the ungramatical one(-3.061258612915323), why is that? Probably it's because Dumas used past tense to tell the story in the whole book: I scored 'she said' and 'she says', the past tense obviously higher: -3.44517717577869 > -7.206377291472252, and search the count, 43 : 1, meaning the past tense does dominant the whole book.  

the last adjacent agreement is easier to compare becuase both of the two sentences have 3 bigrams found and 0 missing. And gramatically one scores higher -15.515692838132916 > -16.415465719054886. And I searched the count for both 'letter is' and 'letter are', have 4/1, it's testable.

So in adjacent agreement, 1 out of 3 goes with prediction. 

And 2 pairs of long-distance agreement:

'the letter from his friends is here' scores lower than 'the letter from his friends are here', -25.82855929672978 > -27.413693065595808, goes with prediction: adjacent right and long distance wrong. Both have 6 bigrams found and 0 missing, and 1 'friends is' and 3 'friends are' found, so it's compareble. 

'the woman with the horses is here' scores higher than 'the woman with the horses are', -24.523798135287272 > -27.790694630340866 sounds good but there is 5/1 found/missing in gramaticall one and 6/0 in ungramatical one, so I do the average to see average score in each sentence: the gramatical one scores lower than gramatical one: -4.904759627057454 < -4.631782438390144.  I searched the count of 'horses is' and 'horses are', have 0 'horses is' and 3 'horses are'.

So the 2 pairs of long-distance agreements, 1 failed to the prediction. 

1/3 in adjacent agreement and 1/2 in long distance go with prediction, among all of these pairs, only 'letter' and 'friends' are comparable, so the numbers and results are scrambled. 

Worth to note that I use '\w+' to tokenize, instead of split(), "\w+" treats underscore as a word character, hence underscore italics leak.

if we only look at the count: 'door is' found 2, 'door are', 0; 'letter is', 4, 'letter are', 1; 'friends is', 1, 'friends are', 3; 'horses is', 0, 'horses are', 3; 'count is' 16 and 'count are' 6(while the count is proably being vocative); 'eyes are' 3, 'eyes is' 0: grammatical bigram wins the count but failed the bigram scores, the bigram scores can't tell the story.