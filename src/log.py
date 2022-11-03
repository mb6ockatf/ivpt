#!/usr/bin/python3

from logging import basicConfig, DEBUG


def setup_logging(log_name: str):
    basicConfig(filename=log_name, level=DEBUG, format="%(asctime)s %(message)s")
