import logging
import sys
import json
import argparse
from os.path import exists

from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

# from test import *
from app import App
from script import Script

# TODO:
#  [ ] Good checking for proposition's format, duplication, etc
#  [x] Unique tactic name(done?)
#  [ ] Good tactic name format
#  [ ] * Logging implementation
#  [x] *** Implement cmd parameters
#  [ ] ** Eliminate redundant relations: check for one node, all relations that doesn't being fed at current time
#  [ ] Collect error messages and output them after the program has finished?

# TODO: logging file to be implemented

# Cypher commands to color the nodes by chapters(APOC required):
# MATCH (n:Prop)
# WITH DISTINCT n.chapter AS chapter, collect(DISTINCT n) AS props
# CALL apoc.create.addLabels(props, [apoc.text.upperCamelCase(chapter)]) YIELD node
# RETURN *

# Cypher command to change password:
# ALTER USER neo4j SET PASSWORD 'neo4j'

logfile = "log_pmneo4j.txt"
bolt_url = "bolt://localhost:7687"
user = "neo4j"
password = "neo4j"
tactics = "scripts/tactics.txt"
scripts = []


def tests():
    # test_prop_check_exists()  # passed
    # test_update_prop()  # passed
    # test_update_prop_name()  # passed
    # test_conn_check_exists()  # passed
    # test_open_file()  # passed
    # test_script_prop()  # passed
    # test_script_conn()  # passed
    # test_script_name()  # passed
    # test_script_load_tactics()  # passed
    # test_script_use_tactics()  # passed
    # test_script_run()  # passed
    # test_script_run2()  # passed
    pass


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

    # Loading configuration from conf.json
    # python variable scope?
    if exists("conf.json"):
        conff = open("conf.json")
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

    # Loading configuration from command line prompts
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

    ####################################

    print("Username: '{u}', url: {url}".format(u=user, url=bolt_url))

    App.enable_log(logging.INFO, sys.stdout)
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
    pass
