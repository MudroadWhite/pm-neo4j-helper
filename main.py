import logging
import sys

from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

from app import App

def clear_nodes():
    pass

def check_nodes():
    pass

logfile = "logfile.txt"
bolt_url = "bolt://localhost:7687"
user = "neo4j"
password = "neo4j"

if __name__ == "__main__":
    App.enable_log(logging.INFO, sys.stdout)
    app = App(bolt_url, user, password)

    app.create_pm_prop("1.01", "1", "1", "A", "94", "Df")
    app.create_pm_prop("1.1", "1", "1", "A", "94", "Df")

    app.create_pm_prop("1.11", "1", "1", "A", "95", "Pp")

    app.create_pm_prop("1.2", "1", "1", "A", "96", "Pp")
    app.create_pm_prop("1.3", "1", "1", "A", "96", "Pp")
    app.create_pm_prop("1.4", "1", "1", "A", "96", "Pp")
    app.create_pm_prop("1.5", "1", "1", "A", "96", "Pp")

    app.create_pm_prop("1.6", "1", "1", "A", "97", "Pp")
    app.create_pm_prop("1.7", "1", "1", "A", "97", "Pp")
    app.create_pm_prop("1.71", "1", "1", "A", "97", "Pp")
    app.create_pm_prop("1.72", "1", "1", "A", "97", "Pp")

    app.close()