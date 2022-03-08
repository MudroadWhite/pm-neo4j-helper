import sys
import json
import argparse
from os.path import exists
from log import setup

# from neo4j import GraphDatabase

# from test import test
from app import App
from script import Script

# TODO:
#  [x] Unique tactic name(done?)
#  [x] Implement cmd parameters
#  [x] Comment support UTF-8 or so, at least for Chinese
#  [x] Logging implementation, collect error messages(log & errors)
#  [ ] ***** Implement a JSON Parser(Side project)
#  [ ] ** Make a pip package
#  [ ] *** App -> Script raise error, for better error printing
#  [ ] * Eliminate redundant relations: check for one node, all relations that doesn't being fed at current time
#  [ ] Good checking for proposition's format, duplication, etc
#  [ ] Good tactic name format
#  [ ] Message printing options for cmd & conf?
#  [ ] Possibility to set up threads?

# TODO: logging file to be implemented

# Configuration file variable
conffile = "conf.json"

# logfile = "log_pmneo4j.txt"
bolt_url = "bolt://localhost:7687"
user = "neo4j"
password = "neo4j"
tactics = "scripts/tactics.txt"
scripts = []

def run():
    print("PM-Neo4j helper")

    ap = argparse.ArgumentParser(description='Sends script commands of PM to Neo4j queries.')
    ap.add_argument("--username", "-u", help="Sets username.")
    ap.add_argument("--password", "-p", help="Sets password.")
    ap.add_argument("--bolt-url", "-b", help="Sets bolt_url.")
    ap.add_argument("--log-file", "-l", help="Sets log file location.")
    ap.add_argument("--conf", "-c", help="Sets configuration file location.")
    ap.add_argument("--tactic", "-t", help="Sets tactic file location.")
    ap.add_argument("--scripts", "-s", nargs="*", help="Sets a list of scripts to be processed.")

    cmd = vars(ap.parse_args())

    # Load configuration from conf.json
    # python variable scope?
    if exists(conffile):
        conff = open(conffile, 'r', encoding="utf8")
        conf = json.load(conff)
        conff.close()

        if "username" in conf:
            user = conf["username"]
        if "password" in conf:
            password = conf["password"]
        if "bolt_url" in conf:
            bolt_url = conf["bolt_url"]
        if "logfile" in conf:
            logfile = conf["logfile"]
        if "tactics" in conf:
            tactics = conf["tactics"]
        if "scripts" in conf:
            scripts = conf["scripts"]

    # Load configuration from command line prompts
    if len(sys.argv) > 1:
        if "username" in cmd:
            user = cmd["username"]
        if "password" in cmd:
            password = cmd["password"]
        if "bolt_url" in cmd:
            bolt_url = cmd["bolt_url"]
        if "logfile" in cmd:
            logfile = cmd["logfile"]
        if "tactics" in cmd:
            tactics = cmd["tactics"]
        if "scripts" in cmd:
            scripts = cmd["scripts"]

    if len(scripts) == 0:
        print("No files found. Quit.")
        exit()

    # logging setup
    setup()

    ####################################

    print("Username: '{u}', url: {url}".format(u=user, url=bolt_url))

    app = App(bolt_url, user, password)
    s = Script(app, tactics)

    s.load_tactics()

    for ss in scripts:
        s.script = ss
        s.run()

    s.save_tactics()
    s.close()


if __name__ == "__main__":
    run()
    # setup()

    # test()
    # TODO: Logging
    #  1. INFO -> log file, detailed formatter/basic formatter option (verbose / basic / silent)
    #  2. ERROR -> error file, detailed formatter
    #  3. ERROR -> stdout, basic formatter
    #  https://stackoverflow.com/questions/16757578/what-is-pythons-default-logging-formatter
    #  https://www.cnblogs.com/yyds/p/6901864.html
    #  https://docs.python.org/3/library/logging.html
    #  https://www.loggly.com/ultimate-guide/python-logging-basics/

    # TODO: Logging for Neo4j.PMNeo4jHelper.Script

    # TODO: Neo4j.PMNeo4jHelper.App error raise to Script class?

    # TODO:
    #  1. Script sets up the logger with name
    #  2. App tries to log with logger in this name?

    # formatter = logging.Formatter("[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
    #                               datefmt="%d/%b/%Y %H:%M:%S")
    # handler = logging.StreamHandler(sys.stdout)
    # handler.setFormatter(formatter)
    # nl = logging.getLogger("App")
    # nl.addHandler(handler)
    # nl.setLevel(logging.DEBUG)
    # nl.debug("Neo4j")
    pass
