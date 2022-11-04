#!/usr/bin/env python3
"""Base sqlite3-DB connection class"""
from os import sep, path, mkdir
from logging import info
from typing import Union
from sqlite3 import connect

class DatabaseConnection:
    """Parental class to handle DB connection"""
    def __init__(self, config: dict):
        home = path.expanduser("~")
        self.db_path = home + sep + config["db"]
        path_items_list = list(self.db_path.split(sep))[1:]
        for index in range(len(path_items_list)):
            cur_dir = sep + sep.join(path_items_list[0:index])
            if not path.isdir(cur_dir):
                mkdir(cur_dir)
        if not path.isfile(self.db_path):
            with open(self.db_path, "w", encoding="utf-8"):
                info("db file created")
        self.connection = connect(self.db_path)
        info("db connection opened")

    def close(self):
        """Close database connection"""
        self.connection.close()
        info("db connection closed")

    def execute_query(self, query: str, data: Union[dict, tuple, None]) -> tuple:
        """Execute SQL query with values"""
        cursor = self.connection.cursor()
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        self.connection.commit()
        result = cursor.fetchall()
        cursor.close()
        info("db query executed")
        return result
