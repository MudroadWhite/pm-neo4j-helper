# Note to Readers

Important notes that could be helpful to organize or use the script, will be put in this file.

--------

## Comments are More Useful than You Think 

In some files, I write comments to indicate that, there might be some tactic not being added into the proof relation, because I haven't digested the tests so far yet. It can also be that, the original text has so much ambiguity that unless you comprehend the text, your proof relation might be completely go wrong. If I don't write these comment carefully, the situarion would be worse - and sadly I am not a careful person.

## Known Issues

##### Tactic []=
Some proofs involve lines using `\[etc\] = proposition`. It's needed to figure out what theorem supports this abbrevation.

##### Tactic []<-
Similar to above, some proofs involve `\[etc\] <- proposition`. It appears at later chapter so it's harder to figure out.

##### Tactic Hp-Prop
`Hp` stands for hypothesis. Some proofs in very later chapters uses abbreviations like `Hp77.77` to indicate the hypothesis of proposition `77.77`.

##### Similar Proof
Some proof are omitted and written "similar proof" only. It's severely ambiguous, and the actual proof relation can be known only after one has comprehended the texts.
For tactics above, I have a chance to label those tactics as clearly as I can in comments. But for similar proof, I might be very careless... It's recommended to
check through original text to figure out where `similar proof` has been used to abbreviate the texts.

##### Missing Dot
On page 470, Thm 74.3, there's a line of proof writing `10 11.23.35`. It cannot be determined whether this happens from missing a dot, or misplacing a space.

##### Alternative Proof
Some propositions might be provided more than one proofs. My current way to manage with the proof relation recording is writing both sets of relations in the scripts, but commenting out one of them. 