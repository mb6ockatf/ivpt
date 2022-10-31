#!/usr/bin/env python

from os import sep, path, mkdir
from logging import info
from typing import Union
from sqlite3 import connect, Connection
from src.config import Configuration


class DatabaseConnection(object):
    INSTANCE = None
    db_path: str
    connection: Connection

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls.INSTANCE:
            cls.INSTANCE = super().__new__(DatabaseConnection)
        return cls.INSTANCE

    @classmethod
    def __init__(cls, config_object: Configuration):
        config = config_object.CONFIG
        cls.db_path = config_object.HOME + sep + config["db"]
        path_items_list = list(cls.db_path.split(sep))[1:]
        for index in range(len(path_items_list)):
            cur_dir = sep + sep.join(path_items_list[0:index])
            if not path.isdir(cur_dir):
                mkdir(cur_dir)
        if not path.isfile(cls.db_path):
            open(cls.db_path, "w").close()

    @classmethod
    def __enter__(cls):
        cls.connection = connect(cls.db_path)
        info("db connection opened")
        return cls.connection

    @classmethod
    def __exit__(cls):
        cls.connection.close()
        info("db connection closed")

    @classmethod
    def execute_query(cls, query: str, data: Union[dict, tuple, None]):
        cursor = cls.connection.cursor()
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        cls.connection.commit()
        result = cursor.fetchall()
        cursor.close()
        info("db query executed")
        return result

