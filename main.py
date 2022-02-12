import logging
import sys

from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

from app import App
from test import *

# TODO:
#  1. Good checking for proposition's format, duplication, etc
#  2. Unique tactic name(done?)
#  3. Good tactic name format
#  4. Set script file & tactic file

# TODO:
#  1. Finished almost core functionalities! Be ready to write some tests
#  2. After testing, implement general logic to make the python script running
#     and polish the codes(?)
#  3. logging implementation

logfile = "log_pmneo4j.txt"
bolt_url = "bolt://localhost:7687"
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
    print("Running pm-neo4j helper")
    print("Username: '{u}', url: {url}".format)
    App.enable_log(logging.INFO, sys.stdout)
    app = App(bolt_url, user, password)

    s = Script(app)
    s.run()