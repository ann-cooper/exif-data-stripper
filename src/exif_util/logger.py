"""
Reference: https://docs.python-guide.org/writing/logging/
"""

import logging
import sys

def get_python_version():
    """Returns the Python version in use."""
    major, minor, micro, level, serial = sys.version_info

    return major, minor


def get_logger(name, level=logging.DEBUG, version=get_python_version()):
    """Sets up a json logger.

    Parameters
    ----------
    name : str
        The module name: `logger = logger.get_logger(__name__)`
    level : int, optional
        Set the logging level, by default logging.DEBUG
    version : int, optional
        Python version, by default get_python_version()

    Returns
    -------
    logging.Logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(level=level)

    log_handler = logging.StreamHandler()

    formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)
    logger.propagate = True
    return logger
