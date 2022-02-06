# pm-neo47-helper
## What It Does

Neo4j is a database with visualized graph.

Principia Mathematica is a large book with proofs.

This helper reads simplified script, generates Neo4j queries and send it into Neo4j database.



## Script Syntax & Functionalities

### General Location Info

`volume x`, `part x`, `section x`, `page x` set volume, part, section, page to x respectively.

### Proposition Recording (To be implemented)

`Thm x`, `Df x`, `Pp x` send query of proposition x with type Thm, Df or Pp respectively.

`name x` adds a name for a proposition x for future translation. (To be implemented)

### Proof Relation Recording (To be implemented)

`-> a b1 b2 b3...` sends relations `b1 proves a`, `b2 proves a`... to Neo4j database.

`tactic x y1 y2 y3...` adds a tactic for proofs, serving for proof simplification in PM, for future translation. Tactic's name is x and the tactic will add ys to the proof relations. (To be implemented)

The script will try to search for name and tactic when it meets some word that doesn't appear to be a proposition number.



### TODO

- [ ] Implement name & tactic searching 
- [ ] Implement name & tactic translation
- [ ] Implement name & tactic saving
