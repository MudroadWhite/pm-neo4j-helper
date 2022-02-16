import logging
import sys

from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

# from test import *
from app import App
from script import Script
import json

# TODO:
#  [ ] Good checking for proposition's format, duplication, etc
#  [x] Unique tactic name(done?)
#  [ ] Good tactic name format
#  [ ] Logging implementation
#  [ ] *** Implement cmd parameters
#  [ ] *** Eliminate redundant relations: check for one node, all relations that doesn't being fed at current time
#  [ ] Collect error messages and output them after the program has finished?

# TODO: to be implemented
logfile = "log_pmneo4j.txt"
bolt_url = "bolt://localhost:7687"
# ALTER USER neo4j SET PASSWORD 'neo4j'
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
    # TODO: test loading multiple files
    pass


def run():
    # TODO:
    #  [x] 1. Default settings in variables
    #  [x] 2. Load settings from some JSON conf file
    #  [ ] 3. Load settings from some command line parameters
    print("PM-Neo4j helper")

    # TODO:
    #  implement cmd parameters
    #  apply conf settings to general running logic, and run the program

    # https://www.datacamp.com/community/tutorials/argument-parsing-in-python
    # cmd parameters:
    # -h --help: show help info
    # -u --username: set username
    # -p --password: set password
    # -b --bolt-url: set bolt_url
    # -l --log-file: set log file location
    # -c --conf: set configuration file
    # -t --tactic: set tactic file
    # -s --script: final argument, a list of scripts....

    # Loading configuration from conf.json
    # TODO: if conf.json exists, change the value...
    # TODO: python variable scope
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

    print("Username: '{u}', url: {url}".format(u=user, url=bolt_url))

    App.enable_log(logging.INFO, sys.stdout)
    app = App(bolt_url, user, password)
    s = Script(app, tactics)

    for ss in scripts:
        print("Running script {ss}...".format(ss=ss))
        s.script = ss
        s.run()
    s.close()


if __name__ == "__main__":
    run()
