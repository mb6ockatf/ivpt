#!/usr/bin/env python

from logging import basicConfig, DEBUG


def setup_logging(log_name: str):
    basicConfig(filename=log_name, level=DEBUG, format="%(asctime)s %(message)s")


if __name__ == "__main__":
    from os import unlink
    from errors_handler import ErrorHandler
    try:
        setup_logging("log.txt")
        unlink("log.txt")
    except Exception as error:
        ErrorHandler.show_exception(error)
