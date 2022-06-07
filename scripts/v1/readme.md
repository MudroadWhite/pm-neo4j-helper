# Note to Readers

Important notes that could be helpful to organize or use the scripts, will be listed out in this file.

--------

## Detectable Errors
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

##### Tactics of []?
Several tactics involve using [] following by a connective in the proofs. These tactics include:
- tactic []=
- tactic []<-

To my current understanding, these tactics have to deal with 1.11 as it's very fundamental. However there could be some more exact statements in
some chapters stating that they could be used, so I cannot track the exact definitions' numbers they correspond to.

##### Tactics with subscripts(___)
There could be some connectives being added subscript(s), and the use of these connectives are being recognized as using 
a tactic. One example is the `[]<->___` in chapter 40. Currently I have found out that they act as an abbreviation of 
`forall`, as stated in page 22:
```
Fx (->_x) Gx <-> forall x. (Fx -> Gx) Df
```
Since it's a collection of tactics, I won't give complete treatment in the forseeable future to identify exact 
definitions to the connective abbreviations. However, I have made NOTES on where they're being used.

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

## Note on Inference Methods in Principia

In general the most important inference ways I can see currently are the followings:

1. |- (proposition)
2. [] |- (proposition)
3. |- (proposition) ->
   \[(premises)\] |- (proposition) which is tactic `->[]`.
4. [Syll] |- [(1). (2). (3)] -> |- p   
   
Since the material is rare I'll try to make a distinction between these tactics.

##### 1. Ordinary Assumption (p92)
Turnstile just means we assume a proposition. `|- p` means we can assume a proposition p without any requirements. Usually 
this means the proposition `p` is a **primitive proposition** in PM as the foundation of the theory. There could be other
usages in the later chapter.

##### 2. Assumption from brackets (p98, p100) 
(To be finished) There could be multiple ways of usages in this kind of inference. But the most simple
kind of inference just want to use the brackets to mean that
> We are using some conclusions from some previous proofs.

When meaning this we are usually seeing only one propositions in the bracket. For example `Thm 2.01`.

Another kind of usage of brackets is using a sequent of conclusions with a definition or inference rule:

> [(1). (2). *1.11]
> 
> [(1). (*1.01)]
> 
> [(1). (2)]

Several subtle characteristics to be addressed in these lines of brackets. First of all one of them has a pair of rounded brackets while the others don't. Rounded brackets
means this is a definition. Second the 3rd one doesn't get a proposition number as its last element of the sequent. This
usually means *1.11 has been omitted. What does *1.11 says? It says:

> If we can write |- Fx, and we can write |- Fx -> Gx, then we can write |- Gx.

(To be checked)So usually we want to say (1) is some kind of `|- Fx` and (2) is some kind of `|- Fx -> Gx` and we want to 
conclude that we can write `|- Gx` as a conclusion. This is to say we're using an inference rule to derive a conclusion.

The situation of `*(1.01)` is different. It doesn't involve inference, and this is why it's enclosed in rounded brackets `()`.
This means we want to apply a definition.

##### 3. Combined, Simplified Inference (p103, tactic `->[]`)

In the last section we have explained the usage of Pp `1.11`. There's also other ways to use `1.11` and I'll take one of them
as an example to show their underlying reasoning. We have

> |- p ->
> 
> [etc.]  |- q

which means 

> We have proved |- p is true. "etc" is a proof of "|- p -> q is true". So we're now proving q is true.
> We want to make the proof looks like |-p -> |- q with a comment witnessing its validity, so we use a bracket.  

And this according to the author of Principia involves Pp `1.11`.

#### 4. Syllogism
Syllogism is another inference rule. Since the rule is different from `1.11` so the way it can use for simplify the proofs
is also different. Note that it's not some proof like `[(1). (2). (3). Syll]`. However, in the later chapter this kind of
proof abbreviation has been abandoned. If you can understand how 1.11 works you should figure out the underlying reasoning of 
this abbreviation pretty soon.

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