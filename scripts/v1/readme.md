# Note to Readers

Important notes that could be helpful to organize or use the scripts, will be listed out in this file.

--------

## Errors Being Detected
Within the helper I have built a simple error checking system that checks errors while parsing the scripts. Errors that can be detected
includes:

1. General syntax errors that mentioned in [README.md](/README.md).
2. Propositions that don't exist in the database while reading a line.

Because of the nature(brutality), several types of critical errors cannot be detected. They include:
1. Wrong proof relation `a <- b`, assigning a proposition `a` to a proof proposition `b`, where the name `b` *exists* in the database.
2. Missing proof relations, tactics due to carelessness.
3. Missing proposition numbers not being recorded, which should occur at a very low chance.

## Comments are More Useful than You Think 

In some files, I write comments to indicate that, there might be some tactic not being added into the proof relation, because I haven't digested the tests so far yet. It can also be that, the original text has so much ambiguity that unless you comprehend the text, your proof relation might be completely go wrong. If I don't write these comment carefully, the situation would be worse - and sadly I am not a careful person.

## Known Issues

##### Tactic []=
Some proofs involve lines using `\[etc\] = proposition`. It's needed to figure out what theorem supports this abbrevation.

##### Tactic []<-
Similar to above, some proofs involve `\[etc\] <- proposition`. It appears at later chapter so it's harder to figure out.

##### Tactic Hp-Prop
`Hp` stands for hypothesis. Some proofs in very later chapters uses abbreviations like `Hp77.77` to indicate the hypothesis of proposition `77.77`.

##### Similar Proof
Some proofs are omitted and written "similar proof" only. It's severely ambiguous, and the actual proof relation can be known only after one has comprehended the texts.
For tactics above, I have a chance to label those tactics as clearly as I can in comments. But for similar proof, I might be very careless... It's recommended to
check through original text to figure out where `similar proof` has been used to abbreviate the texts.

##### Missing Dot
On page 470, Thm 74.3, there's a line of proof writing `10 11.23.35`. It cannot be determined whether this happens from missing a dot, or misplacing a space.

##### Alternative Proof
Some propositions might be provided more than one proofs. My current way to manage with the proof relation recording is writing both sets of relations in the scripts, but commenting out one of them. 

##### Dft
Dft appears in the very later chapters of the texts, and I cannot understand its meaning. It seems to be different from Df, Thm or Pp, and the real meaning remains to be figured out. 

##### Volatile Ch.8
Most proofs in chapter 8 in Appendix A are given in texts, and in a lot of cases the proofs mention other propositions as "similar proof". Without these mentions, the proofs contain no propositions at all.

--------

## Useful Cypher Snippets

Color the nodes by chapters(APOC library required):
````cypher
MATCH (n:Prop)
WITH DISTINCT n.chapter AS chapter, collect(DISTINCT n) AS props
CALL apoc.create.addLabels(props, [apoc.text.upperCamelCase(chapter)]) YIELD node
RETURN *
````

Change password:
````cypher
ALTER USER neo4j SET PASSWORD 'neo4j'
````

Export whole database to JSON object(APOC library required):
````cypher
CALL apoc.export.json.all("pm.json",{useTypes:true})
````
Find the json object under the database's `import/` folder, or open the project's `import` folder from settings.


--------

## Volume 1 Recording Progress : Finished

### Part 1
#### Section A

- [x] Chapter 1
- [x] Chapter 2
- [x] Chapter 3
- [x] Chapter 4
- [x] Chapter 5 (Texts to be digested)

#### Section B (Texts to be digested)
- [x] Chapter 9
- [x] Chapter 10 (New abbreviation to be checked)
- [x] Chapter 11 (New abbreviation to be checked)
- [x] Chapter 12
- [x] Chapter 13
- [x] Chapter 14
  
#### Section C (Stuck on "similar proof" references, to be checked carefully in future)
- [x] Chapter 20
- [x] Chapter 21 
- [x] Chapter 22
- [x] Chapter 23
- [x] Chapter 24 (New tactic []=)
- [x] Chapter 25 
  
#### Section D
- [x] Chapter 30
- [x] Chapter 31
- [x] Chapter 32
- [x] Chapter 33
- [x] Chapter 34 (New tactic []<-)
- [x] Chapter 35
- [x] Chapter 36
- [x] Chapter 37
- [x] Chapter 38

#### Section E
- [x] Chapter 40 (New tactic []<->___)
- [x] Chapter 41
- [x] Chapter 42
- [x] Chapter 43

### Part 2
#### Section A
- [x] Chapter 50
- [x] Chapter 51
- [x] Chapter 52
- [x] Chapter 53
- [x] Chapter 54
- [x] Chapter 55
- [x] Chapter 56

#### Section B
- [x] Chapter 60
- [x] Chapter 61
- [x] Chapter 62
- [x] Chapter 63
- [x] Chapter 64
- [x] Chapter 65

#### Section C
- [x] Chapter 70
- [x] Chapter 71
- [x] Chapter 72
- [x] Chapter 73 (New tactic hp prop)
- [x] Chapter 74 (2 NOTEs)

#### Section D
- [x] Chapter 80 (1 NOTE)
- [x] Chapter 81
- [x] Chapter 82 (New tactic []<., new tactic []->R)
- [x] Chapter 83
- [x] Chapter 84 (Beautiful proof x1)
- [x] Chapter 85
- [x] Chapter 88

#### Section E
- [x] Chapter 90
- [x] Chapter 91
- [x] Chapter 92
- [x] Chapter 93
- [x] Chapter 94
- [x] Chapter 95 (Unknown symbol "Dft")
- [x] Chapter 96 (1 NOTE)
- [x] Chapter 97

### Appendix A
- [x] Chapter 8 (1 NOTE)

### Appendix B
- [x] Chapter 89