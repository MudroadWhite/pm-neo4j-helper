# pm-neo47-helper
## What It Does

Neo4j is a database with visualized graph.

Principia Mathematica is a large book with proofs.

This helper reads simplified script, generates Neo4j queries and send it into Neo4j database, for recording the proof relations in PM.

Related Project: https://github.com/LogicalAtomist/principia

## How to Run

The suggested way to run the helper for now is

```python.exe pm-neo47-helper/main.py```

Username, password, and bolt url for the Neo4j database should be set in `main.py`. The Neo4j database should have its bolt connection enabled.

## Script Syntax & Functionalities

### General Location Info Setting

`volume x`, `part x`, `section x`, `page x` set volume, part, section, page to x respectively. 

### Proposition Recording

`Thm x`, `Df x`, `Pp x` send query of proposition x with type Thm, Df or Pp respectively. If a proposition is in the database, it will be updated with the corresponded new values. `x` will also be set as the last proposition being recorded in the script.

`name x` adds a name to an already existing proposition in the database.

### Proof Relation Recording

`<- a1 a2 a3...` sends relations `a1 proves x`, `a2 proves x`... to Neo4j database, where `x` is the last proposition being recorded. 

`tactic x y1 y2 y3...` adds a tactic involving a proof pattern supported by several propositions, for future translation. Abstracting the proof patterns can simplify the proof in PM. Tactic's name is x, and the involved propositions are ys. These ys will be added into proof relations that proves x.

Tactics can be saved in a local file. When the helper starts, the helper will try to read tactics from the local file. When the helper is finished, the helper will save/update new tactics back to the local file.

### Comments

`# x`, a line starts with a # and a space, is a line of comment. Use it to enhance the readability of your script. 

Any length of `#` is allowed, for giving weights to the comments. e.g. `#`, `##`, `###`...

## Pros
- Allows you(potentially) feed more than one scripts and still generate solid relation graph.
- Already existed nodes and relations will be checked for uniqueness.

## Restrictions

The script language isn't implemented formally using a parser and lexer. Rather, I do all the things pretty brutal. Therefore,

- Newlines are pretty strict. 
- Don't leave extra symbols like ",", ";" in the script. 
- One, and only one space is required, for all syntaxes mentioned above. Don't leave extra spaces anywhere.
- Only one instruction at one line.
- Didn't figured out a way to *delete* redundant relations that are added by mistake safely.

## More Information

Functionalities are being tested on Windows 10. Potentially the username and the password have to be alternated.

Default file to save tactics is `scripts/tactics.txt`.

Default script file to feed the script is `scripts/pm.txt`.

(Currently, the functionality to change the files is not implemented.)



## TODO

- [ ] Upload generated database to Github?
- [x] All core functionalities
- [x] Test all core functionalities  
- [ ] Set/change script file
- [ ] Set/change tactic file storing/loading location
- [ ] More functionalities to fix bugs...

## PM Relation Progress

### Volume 1
#### Section A

- [x] Chapter 1
- [x] Chapter 2
- [x] Chapter 3
- [ ] Chapter 4
- [ ] Chapter 5

#### Section B
- [ ] Chapter 9
- [ ] ...