import logging
from logging import BASIC_FORMAT

verbose = logging.Formatter("[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
                                  datefmt="%d/%b/%Y %H:%M:%S")

basic = logging.Formatter(BASIC_FORMAT)

infolog = "info.log"

errorlog = "error.log"


def enable_log(level, output_stream, v=False):
    formatter = basic if not v else verbose
    handler = logging.StreamHandler(output_stream)
    handler.setLevel(level)  # output stream handler... ERROR / WARNING
    # to be configured using outside control
    # TODO: handler 2: output to file?
    handler.setFormatter(formatter)
    nl = logging.getLogger("PMNeo4jHelper")
    nl.addHandler(handler)
    nl.setLevel(level)

def disable_log():
    # ???
    pass