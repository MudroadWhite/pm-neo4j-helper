#
# TODO:
#  change print to log

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
        self.name = [] # [String name, String number]
        self.tactics = [] # [String name, String number1, String number2 ...]

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
        command = parse[0].lower()
        if command == "volume": # set volume to x
            self.volume = parse[1]
        elif command == "part": # set part to x
            self.part = parse[1]
        elif command == "section": # set section to x
            self.section = parse[1]
        elif command == "page": # set page to x
            self.page = parse[1]
        elif command == "->": # add b proves a relation
            a = parse[1]
            bs = parse[2:]
            self.parse_proof_line(a, bs)
        elif command == "tactic": # add tactic x
            print("Line {linenum}: tactic not implemented: ".format(linenum=linenum) + line)
        elif command == "name": # add name x
            print("Line {linenum}: name not implemented: ".format(linenum=linenum) + line)
        elif command == "Pp" or command == "Df" or command == "Thm":
            [tp, pnum] = [command, parse[1]]
            self.app.create_pm_prop(pnum, self.volume, self.part, self.section, self.page, tp)
        else:
            print("Unidentified line {linenum}: ".format(linenum=linenum) + line)

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

    def search_name(self):
        pass

    def save_name(self):
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
        self.close()
