# pm-neo47-helper
## What It Does

Neo4j is a database with visualized graph.

Principia Mathematica is a large book with proofs.

This helper reads simplified script, generates Neo4j queries and send it into Neo4j database, for recording the proof relations in PM.

Related Project: https://github.com/LogicalAtomist/principia

## Script Syntax & Functionalities

### General Location Info Setting

`volume x`, `part x`, `section x`, `page x` set volume, part, section, page to x respectively. 

### Proposition Recording

`Thm x`, `Df x`, `Pp x` send query of proposition x with type Thm, Df or Pp respectively. If a proposition is in the database, it will be updated with the corresponded new values.

`name x` adds a name to an already existing proposition in the database.

### Proof Relation Recording

`<- a b1 b2 b3...` sends relations `b1 proves a`, `b2 proves a`... to Neo4j database. 

`tactic x y1 y2 y3...` adds a tactic involving a proof pattern supported by several propositions, for future translation. Abstracting the proof patterns can simplify the proof in PM. Tactic's name is x, and the involved propositions are ys. These ys will be added into proof relations that proves x. (To be implemented)

Tactics can be saved in a local file. When the helper starts, the helper will try to read tactics from the local file. When the helper is finished, the helper will save/update new tactics back to the local file.



## Restrictions

The script language isn't implemented formally using a parser and lexer. Rather, I do all the things pretty brutal. Therefore,

- Newlines are pretty strict. 
- Don't leave extra symbols like ",", ";" in the script. 
- One, and only one space is required, for most syntaxes mentioned above. Don't leave extra spaces.
- Only one instruction at one line.



## TODO

- [ ] Test functionalities
- [ ] General running logic
- [ ] Then polish the code and functionalities for more
