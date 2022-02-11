import logging
import sys

from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

from app import App
from test import *

# TODO:
#  1. Finished almost core functionalities! Be ready to write some tests
#  2. After testing, implement general logic to make the python script running
#     and polish the codes(?)

logfile = "logfile.txt"
bolt_url = "bolt://localhost:7687"
user = "neo4j"
password = "neo4j"

if __name__ == "__main__":
    # App.enable_log(logging.INFO, sys.stdout)
    # app = App(bolt_url, user, password)
    # app.create_pm_prop("1.01", "1", "1", "A", "94", "Df")
    # app.close()
    # print("pmneo4j main")

    # test_prop_check_exists() # passed
    # test_update_prop() # passed
    # test_update_prop_name() # passed
    # test_conn_check_exists() # passed
    pass


