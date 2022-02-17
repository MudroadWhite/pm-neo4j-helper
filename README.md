# pm-neo4j-helper
## What It Does

Neo4j is a database with visualized graph.

Principia Mathematica is a large book with proofs.

This helper reads simplified script, generates Neo4j queries and send it into Neo4j database, for recording the proof relations in PM.

Related Project: https://github.com/LogicalAtomist/principia

## How to Run

The suggested way to run the helper for now is

```python.exe main.py```

Username, password, and bolt url for the Neo4j database should be set in `main.py`. The Neo4j database should have its bolt connection enabled.

## Script Syntax & Functionalities

### General Location Info Setting

`volume x`, `part x`, `section x`, `page x` set volume, part, section, page to x respectively. 

### Proposition Recording

`Thm x`, `Df x`, `Pp x` send query of proposition x with type Thm, Df or Pp respectively. If a proposition is in the database, it will be updated with the corresponded new type. `x` will also be set as the last proposition being recorded in the script.

`name x` adds a name to an already existing proposition in the database.

### Proof Relation Recording

`<- a1 a2 a3...` sends relations `a1 proves x`, `a2 proves x`... to Neo4j database, where `x` is the last proposition being recorded. 

`tactic x y1 y2 y3...` adds a tactic involving a proof pattern supported by several propositions, for future translation. Abstracting the proof patterns can simplify the proof in PM. Tactic's name is x, and the involved propositions are ys. These ys will be added into proof relations that proves the last proposition being recorded.

Tactics can be saved in a local file. When the helper starts, the helper will try to read tactics from the local file. When the helper is finished, the helper will save/update new tactics back to the local file.

### Comments

`# x`, a line starts with a # and a space, is a line of comment. Use it to enhance the readability of your script. 

Any length of `#` is allowed, for giving weights to the comments. e.g. `#`, `##`, `###`...

## Configuration
By default, the helper can load a `conf.json` file under the project folder, including settings for running the helper. The configuration should include the following entries:

- bolt_url: The bolt url of the database to be linked to. 
- username: The username of the database.
- password: The password of the database.
- logfile: The location for the helper to output its logs.
- tactics: The location for the helper to load tactics.
- scripts: A list of file paths of scripts that will be fed into the helper. The helper will then translate the scripts to queries, one by one.

## Pros
- Allows you separate your queries into several files and still generate solid relation graph.
- Already existed nodes and relations will be checked for uniqueness.

## Restrictions

The script language isn't implemented formally using a parser and lexer. Rather, I do all the things pretty brutal. Therefore,

- Newlines are pretty strict. 
- Don't leave extra symbols like ",", ";" in the script. 
- One, and only one space is required, for all syntaxes mentioned above. Don't leave extra spaces anywhere.
- Only one instruction at one line.

Also, a way to safely *delete* redundant relations being added by mistake has not be implemented. The suggested way is to clear all nodes in database and reconstruct them again for the time being.

## More Information

Functionalities are being tested on Windows 10 with PyCharm.

## TODO

- [x] All core functionalities
- [x] Test all core functionalities
- [ ] (Important)Implement cmd arguments & options
- [ ] Implement logging functionalities?
- [ ] Gradually transplant the language onto a parser?  
- [ ] More functionalities to fix bugs...

## PM Relation Progress

### Volume 1
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
  
##### Section C
- [ ] Chapter 20
- [ ] Chapter 21
- [ ] Chapter 22  
- [ ] Chapter 23  
- [ ] Chapter 24  
- [ ] Chapter 25
  
##### Section D
- [ ] Chapter 31
- [ ] ...