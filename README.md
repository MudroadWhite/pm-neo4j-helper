# pm-neo4j-helper
![Proof relations in PM for chapter 1-5](graph.png)
## What It Does

Neo4j is a database with visualized graph.

Principia Mathematica is a large book with proofs.

This helper reads simplified script, generates Neo4j queries and send it into Neo4j database, for recording the proof relations in PM.

Related Project: https://github.com/LogicalAtomist/principia

## Pros

- Allows you separate your queries into several files and still generate robust relation graph.
- Already existed nodes and relations can be checked for uniqueness.
- Makes you type super fast comparing to using no tools at all.

## Restrictions

The script language isn't implemented formally using a parser and lexer. Rather, I do all the things pretty brutal. Therefore,

- Don't leave extra symbols like ",", ";" in the script.
- Only one instruction at one line, and don't split the instruction to multiple lines.
- Capital case matters.

Also, a way to safely *delete* redundant relations being added by mistake has not been designed. It's suggested to clear all nodes in database and reconstruct them again for the time being.

## More Information

Functionalities are being tested on Windows 10 with PyCharm and Python 3.9.0.

## Running the Helper

After installing Python(>=3.9), Python's library for Neo4j is also required.

```commandline
python.exe -m pip install neo4j
```

The suggested way to run the helper is

```commandline
python.exe main.py
```

The Neo4j database must have its bolt connection enabled. To enable bolt connection, go to the database's settings, find these entries or turn them on:

```
dbms.connector.bolt.enabled=true
dbms.connector.bolt.listen_address=:7687
```

On the helper side, username, password, and bolt url for the Neo4j database should be set up in `conf.json` under the root directory. 

Command line arguments are also available. See the [configuration](#configuration) section below.

## Script Syntax & Functionalities

### General Location Info Setting

`volume x`, `part x`, `section x`, `page x` set `volume`, `part`, `section`, `page` to `x` respectively. 

### Proposition Recording

`Thm x`, `Df x`, `Pp x` send queries adding proposition `x` with type `Thm`, `Df` or `Pp` into the database respectively. If a proposition is in the database, it will be updated with the corresponded new type. `x` will also be set as the last proposition being recorded in the script.

`name x` adds a name to an already existing proposition in the database.

### Proof Relation Recording

`<- a1 a2 a3...` sends relations `a1 proves x`, `a2 proves x`... to Neo4j database, where `x` is the last proposition being recorded.

> NOTE: Unrecognized proof relations due to unexist proposition numbers, unexist tactic names, won't affect the rest proof relations being added into the database.

`tactic x y1 y2 y3...` adds a tactic involving a proof pattern supported by several propositions, for future translation. Abstracting the proof patterns can simplify the proof in PM. Tactic's name is `x`, and the involved propositions are `y`s. These `y`s will be added into proof relations that proves the last proposition being recorded.

Tactics can be saved in a local file. When the helper starts, the helper will try to read tactics from the local file. When the helper is finished, the helper will save/update new tactics back to the local file.

### Comments

`# x`, a line starts with a `#` and a space, is a line of comment, for enhancing readability.

Any length of `#` is allowed, for giving weights to the comments. e.g. `#`, `##`, `###`...

## Configuration
By default, the helper can load a `conf.json` file under the project folder, including settings for running the helper. The configuration should include the following entries:

- bolt_url: The bolt url of the database to be linked to. 
- username: The username of the database.
- password: The password of the database.
- logfile: The location for the helper to output its logs(Unimplemented).
- tactics: The location for the helper to load tactics.
- scripts: A list of file paths of scripts that will be sent into the helper. The helper will then process the scripts one by one.

You can also change the configuration file to some other files by changing the variable in `main.py`. Specifically, you might want to focus on this line:
```python
# Configuration file variable
conffile = "conf.json"
```

Command line arguments have higher priority over `conf.json`, and will override the settings in `conf.json`. To see help information for command line arguments, run

```commandline
python.exe main.py --help
```

## TODO

- [x] All core functionalities
- [x] Test all core functionalities
- [x] Implement cmd arguments & options
- [x] Implement logging functionalities
- [x] File supports UTF-8 or so, at least for Chinese
- [ ] Implement a JSON Parser(Important side project)
- [ ] Enhance logging functionality  
- [ ] Make a pip package?
- [ ] Gradually transplant the language onto a parser?  
- [ ] More functionalities to fix bugs...

## PM Recording Progress (Finished)

### Volume 1
[Progress](scripts/v1/) (Finished)

### Volume 2
[Progress](scripts/v2/) (Finished)
> Note: For working on volume 2, volume 1's data is required to generate complete database. Volume 3 also applies.  

### Volume 3
[Progress](scripts/v3/) (Finished)