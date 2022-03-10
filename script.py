from app import App
import logging
import re
# import file system?
# import lib?

# TODO:
#  [ ] Change init method to initiating an App instance from inside rather than outside(refactor class?)
#  [ ] try (App function) ... catch errors from app


# TODO: Syntax to be designed:
#  Script = [Line]*
#  Line = Location (Str) | Prop1 (Str) | Thm (Str) [Info]* | tactic (Str) [(Str)]+
#  Location = volume | part | section | page
#  Prop1 = Df | Pp
#  Info = <- [(Str)]+ | name (Str)

def is_prop_number(s):
    return bool(re.match(r"\d+\.\d+", s))


def is_sharp_only(s):
    return bool(re.match(r"\#+", s))


def is_not_empty(s):
    return not len(s) == 0


class Script:
    def __init__(self, app, tacticfile="", script=""):
        self.app = app
        self.tacticfile = tacticfile
        self.script = script
        self.volume = "null"
        self.part = "null"
        self.section = "null"
        self.page = "null"
        self.currentprop = "null"
        self.tactics = {}  # {String name: List String props...}

    def close(self):
        self.app.close()

    def parse_file(self):
        script = open(self.script, 'r', encoding="utf8")
        lines = script.read().splitlines()
        script.close()
        i = 0
        while i < len(lines):
            self.parse_line(lines[i], i)
            i += 1

    def parse_line(self, line, linenum):
        parse = list(filter(is_not_empty, line.split(" ")))
        if len(parse) <= 1:  # Empty, unuseful line
            return
        command = parse[0]
        args = parse[1:]
        if is_sharp_only(command):  # Just common comments
            return
        elif command.lower() == "volume":  # set volume to x
            self.volume = args[0]
        elif command.lower() == "part":  # set part to x
            self.part = args[0]
        elif command.lower() == "section":  # set section to x
            self.section = args[0]
        elif command.lower() == "page":  # set page to x
            self.page = args[0]
        elif command.lower() == "tactic":  # add tactic x
            self.tactics[args[0]] = args[1:]
        elif command == "Pp" or command == "Df" or command == "Thm":
            # set current proposition to x, and upload the proposition with its type to the database
            # TODO: if is not prop number, set back to "null"
            self.currentprop = args[0]
            self.app.create_pm_prop(args[0], self.volume, self.part, self.section, self.page, command)
        elif command == "<-":  # add proof relation for current proposition
            # TODO: Df ... <- ... (prevent illegal situation)
            self.parse_proof_line(args, linenum)
        elif command.lower() == "name":  # add name x
            self.app.update_prop_name(self.currentprop, args[0])
        else:
            logging.getLogger("PMNeo4jHelper").error("Unidentified line {linenum}: ".format(linenum=(linenum+1)) + line)
        return

    def parse_proof_line(self, bs, linenum):
        for b in bs:
            if is_prop_number(b):
                self.app.connect_pm(b, self.currentprop)
            else:
                # if it isn't a prop number, it is a tactic name
                if b in self.tactics:
                    cs = self.tactics[b]
                    for c in cs:
                        self.app.connect_pm(c, self.currentprop)
                else:
                    logging.getLogger("PMNeo4jHelper").error("Unidentified tactic/proposition name {b} in line {linenum}".format(b=b, linenum=linenum))
                    # return

    def load_tactics(self):
        if self.tacticfile == "":
            logging.getLogger("PMNeo4jHelper").info("Cannot find tactic file to read")
            logging.getLogger("PMNeo4jHelper").info("Setting default tactic file to /scripts/tactics.txt...")
            self.tacticfile = "scripts/tactics.txt"
            return
        # clear the tactics...
        self.tactics = {}
        f = open(self.tacticfile, 'r', encoding="utf8")
        tactics = f.read().splitlines()
        f.close()
        i = 0
        for line in tactics:
            parse = list(filter(is_not_empty, line.split(" ")))
            if len(parse) < 2:
                logging.getLogger("PMNeo4jHelper").error("Error loading tactics at line {i}: insufficient arguments".format(i=i))
                return
            self.tactics[parse[0]] = parse[1:]
            i += 1

    def save_tactics(self):
        if self.tacticfile == "":
            logging.getLogger("PMNeo4jHelper").info("Cannot find tactic file to read")
            logging.getLogger("PMNeo4jHelper").info("Setting default tactic file to /scripts/tactics.txt...")
            self.tacticfile = "scripts/tactics.txt"
        logging.getLogger("PMNeo4jHelper").info("Saving tactics to {f}...".format(f=self.tacticfile))
        f = open(self.tacticfile, 'w', encoding="utf8")
        for k in self.tactics:  # tactic name
            f.write(k)
            for t in self.tactics[k]:  # tactic props
                f.write(" ")
                f.write(t)
            f.write("\n")
        f.close()

    ################

    def run(self):
        # 0. Initializing settings...

        # 1. Process script
        if self.script == "":
            logging.getLogger("PMNeo4jHelper").info("No scripts loaded")
            return
        else:
            logging.getLogger("PMNeo4jHelper").info("Processing script file from {f}...".format(f=self.script))
            self.parse_file()

        logging.getLogger("PMNeo4jHelper").info("...Done")
