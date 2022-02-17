# pm-neo4j-helper
## What It Does

Neo4j is a database with visualized graph.

Principia Mathematica is a large book with proofs.

This helper reads simplified script, generates Neo4j queries and send it into Neo4j database, for recording the proof relations in PM.

Related Project: https://github.com/LogicalAtomist/principia

## Pros

- Allows you separate your queries into several files and still generate solid relation graph.
- Already existed nodes and relations will be checked for uniqueness.

## Restrictions

The script language isn't implemented formally using a parser and lexer. Rather, I do all the things pretty brutal. Therefore,

- Don't leave extra symbols like ",", ";" in the script.
- Only one instruction at one line, and don't split the instruction to multiple lines.

Also, a way to safely *delete* redundant relations being added by mistake has not be implemented. The suggested way is to clear all nodes in database and reconstruct them again for the time being.

## More Information

Functionalities are being tested on Windows 10 with PyCharm.

## Running the Helper

After installing Python, python's library for neo4j is also required.

(To be filled)

The suggested way to run the helper is

```commandline
python.exe main.py
```

Username, password, and bolt url for the Neo4j database should be set in `conf.json`. The Neo4j database must have its bolt connection enabled.

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

It is also possible to send commend line options to run the helper. Options in command line parameters will override the settings in `conf.json`. Command line supports all entries listed in `conf.json`. To see help information, run

```commandline
python.exe main.py --help
```

## TODO

- [x] All core functionalities
- [x] Test all core functionalities
- [x] Implement cmd arguments & options
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
  
##### Section C (Stuck on "similar proof" reference)
- [x] Chapter 20
- [x] Chapter 21 
- [x] Chapter 22
- [x] Chapter 23
- [x] Chapter 24 (New tactic []= to be checked)
- [x] Chapter 25 
  
##### Section D
- [x] Chapter 30
- [x] Chapter 31
- [x] Chapter 32
- [x] Chapter 33
- [ ] Chapter 34 (In progress)
- [ ] Chapter 35 (In progress)
- [ ] Chapter 36 (In progress)
- [ ] Chapter 37 (In progress)
- [ ] Chapter 38 (In progress)

##### Section E
- [ ] Chapter 40
- [ ] Chapter 41
- [ ] Chapter 42
- [ ] Chapter 43

#### Part 2
##### Section A
- [ ] Chapter 50
- [ ] Chapter 51
- [ ] Chapter 52
- [ ] Chapter 53
- [ ] Chapter 54
- [ ] Chapter 55
- [ ] Chapter 56

##### Section B
- [ ] Chapter 60
- [ ] Chapter 61
- [ ] Chapter 62
- [ ] Chapter 63
- [ ] Chapter 64
- [ ] Chapter 65

##### Section C
- [ ] Chapter 70
- [ ] Chapter 71
- [ ] Chapter 72
- [ ] Chapter 73
- [ ] Chapter 74

##### Section D
- [ ] Chapter 80
- [ ] Chapter 81
- [ ] Chapter 82
- [ ] Chapter 83
- [ ] Chapter 84
- [ ] Chapter 85
- [ ] Chapter 88

##### Section E
- [ ] Chapter 90
- [ ] Chapter 91
- [ ] Chapter 92
- [ ] Chapter 93
- [ ] Chapter 94
- [ ] Chapter 95
- [ ] Chapter 96
- [ ] Chapter 97

#### Appendix A
- [ ] Chapter 8

#### Appendix B
- [ ] Chapter 89