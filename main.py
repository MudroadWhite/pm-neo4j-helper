import logging
import sys

from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

# from test import *
from app import App
from script import Script

# TODO:
#  [ ] Good checking for proposition's format, duplication, etc
#  [x] Unique tactic name(done?)
#  [ ] Good tactic name format
#  [ ] Logging implementation
#  [ ] *** Enhance main init logic, setting options, including setting script file & tactic file
#  [ ] *** Eliminate redundant relations: check for one node, all relations that doesn't being fed at current time

# TODO: to be implemented
logfile = "log_pmneo4j.txt"
bolt_url = "bolt://localhost:7687"
# ALTER USER neo4j SET PASSWORD 'neo4j'
user = "neo4j"
password = "neo4j"


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

if __name__ == "__main__":
    # TODO:
    #  [ ] 1. Default settings in variables
    #  [ ] 2. Load settings from some JSON file
    #  [ ] 3. Load settings from some parameters
    print("Running pm-neo4j helper")
    print("Username: '{u}', url: {url}".format)
    App.enable_log(logging.INFO, sys.stdout)
    app = App(bolt_url, user, password)

    s = Script(app)
    s.run()