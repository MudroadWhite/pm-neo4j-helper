from app import App
import logging
import re
# import file system?
# import lib?

# TODO:
#  [ ] Change print to log?
#  [ ] Change init method to initiating an App instance from inside rather than outside(refactor class?)
#  [ ] Try app function... catch errors from app

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

    @staticmethod
    def enable_log(level, output_stream):
        handler = logging.StreamHandler(output_stream)
        handler.setLevel(level)
        logging.getLogger("neo4j").addHandler(handler)
        logging.getLogger("neo4j").setLevel(level)

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
            self.parse_proof_line(args, linenum)
        elif command.lower() == "name":  # add name x
            self.app.update_prop_name(self.currentprop, args[0])
        else:
            print("Unidentified line {linenum}: ".format(linenum=(linenum+1)) + line)
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
                    # TODO: enhance the error report
                    print("Unidentified tactic/proposition name {b} in line {linenum}".format(b=b, linenum=linenum))
                    # return

    def load_tactics(self):
        if self.tacticfile == "":
            print("Cannot find tactic file to read")
            print("Setting default tactic file to /scripts/tactics.txt...")
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
                print("Error loading tactics at line {i}: insufficient arguments".format(i=i))
                return
            self.tactics[parse[0]] = parse[1:]
            i += 1

    def save_tactics(self):
        if self.tacticfile == "":
            print("Cannot find tactic file to read")
            print("Setting default tactic file to /scripts/tactics.txt...")
            self.tacticfile = "scripts/tactics.txt"
        print("Saving tactics to {f}...".format(f=self.tacticfile))
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
            print("No scripts loaded")
            return
        else:
            print("Processing script file from {f}...".format(f=self.script))
            self.parse_file()

        print("...Done")
