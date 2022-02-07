#
# TODO:
#  change print to log
#  **modify <- functionality**(and name's), cooperate with Pp Thm
#  modify recordprop functionality
#  proof: auto uniqueness
#  is_number...
#  tactic names should be wrapped in []

from app import App
import logging
# import file system?

def is_prop_number(s):
    # TODO: regex
    pass

class Script:
    def __init__(self, app, namefile="names.txt", tacticfile="tactics.txt", script="pm.txt"):
        self.app = app
        self.namefile = namefile
        self.tacticfile = tacticfile
        self.script = script
        self.volume = "null"
        self.part = "null"
        self.section = "null"
        self.page = "null"
        self.currentprop = "null"
        self.name = []  # [String name, String number]
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
            # TODO: check prop already exists in database
            self.app.create_pm_prop(parse[1], self.volume, self.part, self.section, self.page, command)
        elif command == "<-":  # add proof support for current proposition
            self.parse_proof_line(self.currentprop, parse)
        elif command.lower() == "name":  # add name x
            print("Line {linenum}: name not implemented: ".format(linenum=linenum) + line)
        else:
            print("Unidentified line {linenum}: ".format(linenum=linenum) + line)
        return

    def parse_prop_line(self):
        pass

    def parse_proof_line(self, a, bs):
        # TODO: add tactic and name support
        for b in bs:
            if is_prop_number(b):
                self.app.connect_pm(b, a)
            else:
                continue
        pass

    def read_name(self):
        pass

    def check_nname(self):
        # search prop name in database, check if it has name...?
        pass

    def search_name(self):
        # find name exists in local data?
        pass

    def save_name(self):
        # add prop name to local data?
        pass

    def read_tactic(self):
        pass

    def search_tactic(self):
        pass

    def save_tactic(self):
        pass

    def run(self):
        # TODO:
        #  1. read names from name file
        #  2. read tactics from tactic file
        #  3. load script
        #  4. if found name line in script, search/add name
        #  5. if found tactic line in script, search/add tactic
        #  6. otherwise generate the corresponded neo4j query
        names = open(self.namefile)
        # read names...
        tactics = open(self.tacticfile)
        # read tactics...
        self.parse_file()
        # write names...
        # write tactics...
        self.close()
