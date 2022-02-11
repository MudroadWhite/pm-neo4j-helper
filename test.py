import logging
import sys
from app import App
# from script import Script

logfile = "logfile.txt"
bolt_url = "bolt://localhost:7687"
user = "neo4j"
password = "neo4j"
App.enable_log(logging.INFO, sys.stdout)


def test_prop_check_exists():
    app = App(bolt_url, user, password)
    app.clear_all()

    app.create_pm_prop("1.01", "1", "1", "A", "94", "Df")
    print("Check prop exists")
    print(app.check_prop_exists("1.01"))

    app.close()


def test_update_prop():
    app = App(bolt_url, user, password)
    app.clear_all()

    app.create_pm_prop("1.01", "1", "1", "A", "94", "Df")
    print("Check prop exists")
    print(app.check_prop_exists("1.01"))

    print("Updating prop for test...")
    app.create_pm_prop("1.01", "1", "1", "A", "94", "Thm")

    app.close()


def test_update_prop_name():
    app = App(bolt_url, user, password)
    app.clear_all()

    app.create_pm_prop("1.01", "1", "1", "A", "94", "Df")
    print("Updating prop name...")
    app.update_prop_name("1.01", "test")

    app.close()


def test_conn_check_exists():
    app = App(bolt_url, user, password)
    app.clear_all()

    app.create_pm_prop("1.01", "1", "1", "A", "94", "Df")
    app.create_pm_prop("2.02", "1", "1", "A", "94", "Df")

    app.connect_pm("1.01", "2.02")
    print(app.check_conn_exists("1.01", "2.02"))

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
    app.clear_all()

    # TODO:

    app.close()
