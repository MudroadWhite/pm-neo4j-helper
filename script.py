#
# TODO:
#  1. change print to log?
#  2. implement run function

from app import App
import logging
import re
# import file system?
# import lib?


def is_prop_number(s):
    return bool(re.match(r"\d+\.\d+", s))

class Script:
    def __init__(self, app, tacticfile="tactics.txt", script="pm.txt"):
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
        script = open(self.script)
        lines = script.readlines()
        i = 0
        while i < len(lines):
            self.parse_line(lines[i], i)

    def parse_line(self, line, linenum):
        parse = line.split(" ")
        if len(parse) <= 1:
            return
        command = parse[0]
        args = parse[1:]
        if command == "#":  # Just common comment
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
            print("Line {linenum}: tactic not implemented: ".format(linenum=linenum) + line)
        elif command == "Pp" or command == "Df" or command == "Thm":
            # set current proposition to x, and upload the proposition with its type to the database
            self.currentprop = args[0]
            self.app.create_pm_prop(args[0], self.volume, self.part, self.section, self.page, command)
        elif command == "<-":  # add proof support for current proposition
            self.parse_proof_line(args)
        elif command.lower() == "name":  # add name x
            self.app.update_prop_name(self.currentprop, args[0])
        else:
            print("Unidentified line {linenum}: ".format(linenum=linenum) + line)
        return

    def parse_proof_line(self, bs):
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
                    print("Unidentified tactic name {b}".format(b=b))
                    return

    def load_tactics(self):
        # clear the tactics...
        self.tactics = {}
        tactics = open(self.tacticfile).readlines()
        i = 0
        for line in tactics:
            parse = line.split(" ")
            if len(parse) < 2:
                print("Error loading tactics at line {i}: insufficient arguments".format(i=i))
                return
            self.tactics[parse[0]] = parse[1:]
            i += 1

    def write_tactics(self):
        pass

    def run(self):
        # TODO:
        #  1. load tactics from tactic file
        #  2. read script
        #  3. if found tactic line in proofs, search for tactic
        #  4. otherwise generate the corresponded neo4j query
        tactics = open(self.tacticfile)
        # read tactics...
        self.parse_file()
        # write tactics to local file...
        self.close()
