import logging
from logging import BASIC_FORMAT

import sys

verbose = logging.Formatter("[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
                                  datefmt="%d/%b/%Y %H:%M:%S")

basic = logging.Formatter(BASIC_FORMAT)

simple = logging.Formatter("%(message)s")

infolog = "info.log" # set date...

errorlog = "error.log" # set date...

def setup_loggers():
    # TODO: logfile.clear()
    print("Initializing logging...")
    nl = logging.getLogger("PMNeo4jHelper")
    nl.setLevel(logging.INFO)

    stdinfo = logging.StreamHandler(sys.stdout)
    stdinfo.setLevel(logging.INFO)
    stdinfo.setFormatter(simple)
    nl.addHandler(stdinfo)
    nl.info("Console logger setup complete")

    stderror = logging.StreamHandler(sys.stdout)
    stderror.setLevel(logging.ERROR)
    stderror.setFormatter(simple)
    nl.addHandler(stderror)
    nl.info("Console output error setup complete")

    fileerror = logging.FileHandler('error.log')
    fileerror.setLevel(logging.ERROR)
    fileerror.setFormatter(verbose)
    nl.addHandler(fileerror)
    nl.info("File error logger setup complete")

    fileinfo = logging.FileHandler('info.log')
    fileinfo.setLevel(logging.DEBUG)
    fileinfo.setFormatter(basic)
    nl.addHandler(fileinfo)
    nl.info("File logger setup complete")

    nl.info("...Setup done")

    logging.getLogger("PMNeo4jHelper").debug("test")