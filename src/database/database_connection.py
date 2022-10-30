#!/usr/bin/env python

from os import sep
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
        config_object.touch_config()
        config_object.read_config()
        config = config_object.CONFIG
        cls.db_path = config["db_dir"] + sep + config["db_file"]

    @classmethod
    def __enter__(cls):
        cls.connection = connect(cls.db_path)
        info("db connection opened")

    @classmethod
    def __exit__(cls, exc_type, exc_val, exc_tb):
        cls.connection.close()
        info("db connection closed")

    @classmethod
    def execute_query(cls, query: str, data: Union[dict, tuple, None]):
        cursor = cls.connection.cursor()
        cursor.execute(query, data)
        cls.connection.commit()
        cursor.close()
        info("db query executed")

    @staticmethod
    def insert_basic_info(number: int, abb: str):
        data = {"number": number, "abbreviation": abb}
        query = """INSERT INTO basic_info (number, abbreviation) VALUES (:number, :abbreviation);"""
        DatabaseConnection.execute_query(query, data)

    @staticmethod
    def insert_basic_params(number: int, name: str, group: str, period: int):
        data = {"number": number, "name": name, "group": group, "period": period}
        query = """INSERT INTO basic_params (number, name, group, period)
        VALUES (:number, :name, :group, :period);"""
        DatabaseConnection.execute_query(query, data)

    @staticmethod
    def insert_congregation(number: int, energy_levels: int, period: int, metal=False,
                            amphoteric=False, gas=False, semiconductor=False):
        data = {"number": number, "energy_levels": energy_levels, "period": period,
                "metal": metal, "amphoteric": amphoteric, "gas": gas,
                "semiconductor": semiconductor}
        query = """INSERT INTO congregation (number, energy_levels, period, metal, amphoteric, gas, 
        semiconductor) 
        VALUES (:number, :energy_levels, :period, :metal, :amphoteric, :gas, :semiconductor);"""
        DatabaseConnection.execute_query(query, data)

    @staticmethod
    def insert_links(number: int, wiki_link: str):
        data = {"number": number, "wiki_link": wiki_link}
        query = """INSERT INTO links (number, wiki_link) VALUES (:number, :wiki_link);"""
        DatabaseConnection.execute_query(query, data)

    @staticmethod
    def select_basic_info():
        query = """SELECT number, abbreviation FROM basic_info ORDER BY 1;"""
        DatabaseConnection.execute_query(query, None)

    @staticmethod
    def select_basic_params(element_number: int):
        query = """SELECT name, group, period FROM basic_params WHERE number = ?;"""
        DatabaseConnection.execute_query(query, (element_number,))

    @staticmethod
    def select_congregation(element_number: int):
        query = """SELECT energy_levels, period, metal, amphoteric, gas, semiconductor
        FROM congregation WHERE number = ?;"""
        DatabaseConnection.execute_query(query, (element_number,))

    @staticmethod
    def select_links(element_number: int):
        query = """SELECT wiki_link FROM links WHERE number = ?;"""
        DatabaseConnection.execute_query(query, (element_number,))


if __name__ == "__main__":
    stuff = DatabaseConnection()
