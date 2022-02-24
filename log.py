import logging
from logging import BASIC_FORMAT

import sys

verbose = logging.Formatter("[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
                                  datefmt="%d/%b/%Y %H:%M:%S")

basic = logging.Formatter(BASIC_FORMAT)

infolog = "info.log" # set date...

errorlog = "error.log" # set date...


def setup():
    nl = logging.getLogger("PMNeo4jHelper")
    stderror = logging.StreamHandler(sys.stdout)
    stderror.setLevel(logging.ERROR)
    stderror.setFormatter(logging.Formatter("%(message)s"))
    nl.addHandler(stderror)

    fileerror = logging.FileHandler('error.log')
    fileerror.setLevel(logging.ERROR)
    fileerror.setFormatter(verbose)
    nl.addHandler(fileerror)

    fileinfo = logging.FileHandler('info.log')
    fileinfo.setLevel(logging.INFO)
    fileinfo.setFormatter(basic)
    nl.addHandler(fileinfo)