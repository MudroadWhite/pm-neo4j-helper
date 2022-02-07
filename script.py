#
# TODO:
#  change print to log
#  modify recordprop functionality
#  proof: auto uniqueness
#  tactic names should be wrapped in []

from app import App
import logging
import re
# import file system?


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
        self.tactics = []  # [String name, String number1, String number2 ...]

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
        if command == "#":  # Just common comment
            return
        elif command.lower() == "volume":  # set volume to x
            self.volume = parse[1]
        elif command.lower() == "part":  # set part to x
            self.part = parse[1]
        elif command.lower() == "section":  # set section to x
            self.section = parse[1]
        elif command.lower() == "page":  # set page to x
            self.page = parse[1]
        elif command.lower() == "tactic":  # add tactic x
            print("Line {linenum}: tactic not implemented: ".format(linenum=linenum) + line)
        elif command == "Pp" or command == "Df" or command == "Thm":
            # set current proposition to x, and upload the proposition with its type to the database
            self.currentprop = parse[1]
            # TODO: check location info validity
            if not self.app.check_prop_exists(self.currentprop):
                self.app.create_pm_prop(parse[1], self.volume, self.part, self.section, self.page, command)
            else:
                # TODO: implement update
                self.app.update_prop(parse[1], self.volume, self.part, self.section, self.page, command)
        elif command == "<-":  # add proof support for current proposition
            self.parse_proof_line(parse[1:])
        elif command.lower() == "name":  # add name x
            self.app.update_prop_name(self.currentprop, parse[1])
        else:
            print("Unidentified line {linenum}: ".format(linenum=linenum) + line)
        return

    # def parse_prop_line(self):
    #     pass

    def parse_proof_line(self, bs):
        for b in bs:
            if is_prop_number(b):
                self.app.connect_pm(b, self.currentprop)
            else:
                # TODO: add tactic support
                continue
        pass

    def load_tactics(self):
        pass

    def search_tactic(self):
        pass

    def save_tactic(self):
        pass

    def run(self):
        # TODO:
        #  1. read tactics from tactic file
        #  2. load script
        #  3. if found tactic line in script, search/add tactic
        #  4. otherwise generate the corresponded neo4j query
        tactics = open(self.tacticfile)
        # read tactics...
        self.parse_file()
        # write names...
        # write tactics...
        self.close()
