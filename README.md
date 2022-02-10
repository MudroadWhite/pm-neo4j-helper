# pm-neo47-helper
## What It Does

Neo4j is a database with visualized graph.

Principia Mathematica is a large book with proofs.

This helper reads simplified script, generates Neo4j queries and send it into Neo4j database.



## Script Syntax & Functionalities

### General Location Info

`volume x`, `part x`, `section x`, `page x` set volume, part, section, page to x respectively. 

### Proposition Recording

`Thm x`, `Df x`, `Pp x` send query of proposition x with type Thm, Df or Pp respectively. If a proposition is in the database, it will be updated with the corresponded new values.

`name x` adds a name to an already existing proposition in the database.

### Proof Relation Recording (To be implemented)

`<- a b1 b2 b3...` sends relations `b1 proves a`, `b2 proves a`... to Neo4j database. 

`tactic x y1 y2 y3...` adds a tactic involving a proof pattern supported by several propositions, for future translation. Abstracting the proof patterns can simplify the proof in PM. Tactic's name is x, and the involved propositions are ys. These ys will be added into proof relations that proves x. (To be implemented)

`tactic` will load the tactics from a file, and save/update new tactics back to the file when reading the scripts.



### Restrictions

The script language isn't implemented formally using a parser and lexer. Rather, I do all the things brutally. Newlines are pretty strict, and there's no space for usual symbols like ",", ";" or so. For the syntaxes mentioned above, one & only one space is required. Also, it's recommended to put only one instruction at one line.



### TODO

- [ ] Implement tactic saving
- [ ] App functions: check props/proofs already exists
- [ ] Enhance error report, understand Python logging
- [ ] Main running logic for Script
- [ ] Create -> Update for prop
