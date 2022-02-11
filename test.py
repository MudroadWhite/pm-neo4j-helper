import logging
import sys
from app import App
# from script import Script

logfile = "logfile.txt"
bolt_url = "bolt://localhost:7687"
user = "neo4j"
password = "neo4j"
App.enable_log(logging.INFO, sys.stdout)


def test_prop():
    app = App(bolt_url, user, password)

    app.create_pm_prop("1.01", "1", "1", "A", "94", "Df")
    app.create_pm_prop("1.1", "1", "1", "A", "94", "Df")
    app.create_pm_prop("1.11", "1", "1", "A", "95", "Pp")

    app.close()


def test_update_prop():
    app = App(bolt_url, user, password)

    # TODO: create prop, update prop

    app.close()


def test_check_prop_exists():
    app = App(bolt_url, user, password)

    # TODO: create prop, check if exists

    app.close()


def test_update_prop_name():
    app = App(bolt_url, user, password)

    # TODO: create prop, update its name

    app.close()


def test_conn():
    app = App(bolt_url, user, password)

    # TODO: create connection...

    app.close()


def test_check_conn_exists():
    app = App(bolt_url, user, password)

    # TODO:

    app.close()

####################################


def test_script_prop():
    app = App(bolt_url, user, password)

    # TODO: read file, parse file, create prop

    app.close()


def test_script_tactics():
    app = App(bolt_url, user, password)

    # TODO: read file, parse file, create tactics(?), save tactics(?)

    app.close()


def test_template():
    app = App(bolt_url, user, password)

    # TODO:

    app.close()
