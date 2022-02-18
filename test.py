import logging
import sys
from app import App
from script import Script

logfile = "log_pmneo4j.txt"
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


def test_template():
    app = App(bolt_url, user, password)
    app.clear_all()
    # TODO: template

    app.close()

####################################


def test_open_file():
    file = open(logfile, 'r')
    line = file.readline()
    print("Successfully read log file, line 1: " + line)
    file.close()
    file = open("scripts/tactics.txt", 'r')
    line = file.readline()
    print("Successfully read tactics file, line 1: " + line)
    file.close()
    file = open("scripts/pm.txt", 'r')
    line = file.readline()
    print("Successfully read pm file, line 1: " + line)
    file.close()
    return


def test_script_prop():
    app = App(bolt_url, user, password)
    app.clear_all()
    s = Script(app)
    lines = "volume 1\npart 1\nsection A\n\npage 94\nDf 1.01\nThm 1.1\nPp 2.2\n".split("\n")
    i = 0
    for l in lines:
        print("Parsing line " + str(i) + "| " + l)
        s.parse_line(l, i)
        i += 1
    if app.check_prop_exists("1.01"): print("1.01 exists")
    if app.check_prop_exists("1.1"): print("1.1 exists")
    if app.check_prop_exists("2.2"): print("2.2 exists")

    s.close()


def test_script_conn():
    app = App(bolt_url, user, password)
    app.clear_all()
    s = Script(app)
    lines = "volume 1\npart 1\nsection A\n\npage 94\nPp 1.1\nThm 2.2\n<- 1.1".split("\n")
    i = 0
    for l in lines:
        print("Parsing line " + str(i) + "| " + l)
        s.parse_line(l, i)
        i += 1
    print("Checking if connection 1.1 -> 2.2 exists...")
    print(app.check_conn_exists("1.1", "2.2"))

    s.close()


def test_script_name():
    app = App(bolt_url, user, password)
    app.clear_all()
    s = Script(app)

    lines = "volume 1\npart 1\nsection A\n\npage 94\nPp 1.1\nname test".split("\n")
    i = 0
    for l in lines:
        print("Parsing line " + str(i) + "| " + l)
        s.parse_line(l, i)
        i += 1
    print("Name should be generated")

    s.close()


def test_script_load_tactics():
    app = App(bolt_url, user, password)
    app.clear_all()
    s = Script(app)
    # TODO: read file, parse tactics
    s.load_tactics()
    for k in s.tactics:
        print("Tactic {k}: {tt}".format(k=k, tt=s.tactics[k]))

    s.close()


def test_script_use_tactics():
    app = App(bolt_url, user, password)
    app.clear_all()
    s = Script(app)
    print("Reading tactics.txt file...")
    s.load_tactics()
    for k in s.tactics:
        print("Tactic {k}: {tt}".format(k=k, tt=s.tactics[k]))
    print("Reading & parsing testtactics file...")
    s.script = "scripts/testtactics.txt"
    s.parse_file()
    for k in s.tactics:
        print("Tactic {k}: {tt}".format(k=k, tt=s.tactics[k]))
    print("Saving tactics...")
    s.save_tactics()  # Examine the file...
    s.close()


def test_script_run():
    app = App(bolt_url, user, password)
    app.clear_all()
    s = Script(app)
    s.script = "scripts/testtactics.txt"
    print("Running full logic...")
    s.run()
    s.close()


def test_script_run2():
    app = App(bolt_url, user, password)
    app.clear_all()
    s = Script(app)
    s.script = "scripts/test/testtactics.txt"
    print("Running full logic...")
    s.run()
    print("Running for twice...")
    s.run()
    s.close()


def test_script_chinese_comment():
    app = App(bolt_url, user, password)
    app.clear_all()
    s = Script(app)
    s.script = "scripts/test/test_chn_comm.txt"
    print("testing chinese comment...")
    s.run()
    s.close()


def test_script_template():
    app = App(bolt_url, user, password)
    app.clear_all()
    s = Script(app)
    # TODO: template

    s.close()
