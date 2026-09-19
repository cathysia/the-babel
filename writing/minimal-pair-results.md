
    September 19 bigram probability after smoothing comparing to no smoothing

    With bigram probability, I add one on numerator, and V to the denominator, using Laplace smoothing to solve the zero cliff. The score compares with the score without smoothing: 

                        Grammaticality Sentence                           Entry           Score     Smoothing Bigram Counts
    Adjacent-Agreement  grammatical   The door is open                    Door is are     ✗ -18.19  ✓ -22.58  2
                        ungrammatical The door are open                                   ✓ -4.24   ✗ -24.25  0
                        grammatical   She walks to the door               She walks walk  ✓ -6.35   ✗ -27.14  0
                        ungrammatical She walk to the door                                ✗ -9.18   ✓ -26.04  0
                        grammatical   The letter is here                  Letter is are   ✓ -15.52  ✓ -21.53  4
                        ungrammatical The letter are here                                 ✗ -16.42  ✗ -22.66  1
    Long-Distance       grammatical   the letter from his friends is here Friends is are  ✗ -27.41  ✗ -41.22  1
                        ungrammatical the letter from his friends are here                ✓ -25.83  ✓ -40.74  3
                        grammatical   the woman with the horses is here   Horses is are   ✓ -24.52  ✗ -42.73  0
                        ungrammatical the woman with the horses are here                  ✗ -27.79  ✓ -41.56  3

    After smoothing, all go with predict，adjacent agreement wins grammatical and long-distance wins ungrammatical, except for she walks/she walk. 

    The result after smoothing should return grammatical one win, but the actual result is countrary. If we look into the counts of "she walks" and she walk"，they are both 0. So when we comparing the difference of these two sentence, we are actually comparing the bigram following: "walks to" and "walks to", because that's the only difference in this pair. 

    This returns ungrammatical win not because "walks to" is rarer than "walk to" in Count of Mont Cristo--when we smoothing their denominators change too: C(walks) + V against C(walk) + V. So a rarer context has a smaller denominator in Laplace, it can also make score higher(This is a limit of Laplace smoothing. But we are not talking about this here). So "walk to" can win is because "walk" is rarer. 