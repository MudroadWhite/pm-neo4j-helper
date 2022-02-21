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

--------

## Recording Progress

#### Part 1
##### Section A

- [x] Chapter 1
- [x] Chapter 2
- [x] Chapter 3
- [x] Chapter 4
- [x] Chapter 5 (Texts to be digested)

##### Section B (Texts to be digested)
- [x] Chapter 9
- [x] Chapter 10 (New abbreviation to be checked)
- [x] Chapter 11 (New abbreviation to be checked)
- [x] Chapter 12
- [x] Chapter 13
- [x] Chapter 14
  
##### Section C (Stuck on "similar proof" reference, to be checked carefully in future)
- [x] Chapter 20
- [x] Chapter 21 
- [x] Chapter 22
- [x] Chapter 23
- [x] Chapter 24 (New tactic []=)
- [x] Chapter 25 
  
##### Section D
- [x] Chapter 30
- [x] Chapter 31
- [x] Chapter 32
- [x] Chapter 33
- [x] Chapter 34 (New tactic []<-)
- [x] Chapter 35
- [x] Chapter 36
- [x] Chapter 37
- [x] Chapter 38

##### Section E
- [x] Chapter 40 (New tactic []<->___)
- [x] Chapter 41
- [x] Chapter 42
- [x] Chapter 43

#### Part 2
##### Section A
- [x] Chapter 50
- [x] Chapter 51
- [x] Chapter 52
- [x] Chapter 53
- [x] Chapter 54
- [x] Chapter 55
- [x] Chapter 56

##### Section B
- [x] Chapter 60
- [x] Chapter 61
- [x] Chapter 62
- [x] Chapter 63
- [x] Chapter 64
- [x] Chapter 65

##### Section C
- [x] Chapter 70
- [x] Chapter 71
- [x] Chapter 72
- [x] Chapter 73 (New tactic hp prop)
- [x] Chapter 74 (2 NOTEs)

##### Section D
- [x] Chapter 80 (1 NOTE)
- [x] Chapter 81
- [x] Chapter 82 (New tactic []<., new tactic []->R)
- [x] Chapter 83
- [x] Chapter 84 (Beautiful proof x1)
- [x] Chapter 85
- [x] Chapter 88

##### Section E
- [x] Chapter 90
- [x] Chapter 91
- [x] Chapter 92
- [x] Chapter 93
- [ ] Chapter 94 (In progress)
- [ ] Chapter 95 (In progress)
- [ ] Chapter 96 (In progress)
- [ ] Chapter 97 (In progress)

#### Appendix A
- [ ] Chapter 8

#### Appendix B
- [ ] Chapter 89