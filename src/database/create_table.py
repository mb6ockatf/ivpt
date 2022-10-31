#!/usr/bin/env python

from base import DatabaseConnection


class DatabaseCreateTable(DatabaseConnection):
    def create_table_basic_info(self):
        query = """
        CREATE TABLE IF NOT EXISTS basic_info (
            number INTEGER UNSIGNED NOT NULL, abbreviation TEXT UNIQUE NOT NULL, 
                CONSTRAINT number_pk
                PRIMARY KEY (number));
        """
        self.execute_query(query, None)

    def create_table_basic_params(self):
        query = """
        CREATE TABLE IF NOT EXISTS basic_params (
            number  INTEGER UNSIGNED UNIQUE NOT NULL,
            name    TEXT             UNIQUE NOT NULL,
            weight  REAL             UNIQUE NOT NULL
            group   TEXT CHECK group IN ("alkal-metal",
                                        "alkaline-earth-metal",
                                        "metalloid", 
                                        "reactive-nonmetal",
                                        "transitiom-metals",
                                        "noble-gas",
                                        "post-transition-metal",
                                        "pnictogen", 
                                        "chalcogen", 
                                        "actinoid",
                                        "lanthanoid",
                                        NULL),
            period  INTEGER UNSIGNED,
                CONSTRAINT fk_element_number
                    FOREIGN KEY (number)
                    REFERENCES basic_info(number));
        """
        self.execute_query(query, None)

    def create_table_congregation(self):
        query = """
        CREATE TABLE IF NOT EXISTS congregation (
            number        INTEGER UNSIGNED UNIQUE NOT NULL,
            metal         INTEGER UNSIGNED DEFAULT 0,
            amphoteric    INTEGER UNSIGNED DEFAULT 0,
            energy_levels INTEGER UNSIGNED,
            period        INTEGER UNSIGNED,
            gas           INTEGER UNSIGNED DEFAULT 0,
            semiconductor INTEGER UNSIGNED DEFAULT 0,
                CONSTRAINT fk_element_number
                    FOREIGN KEY (number)
                    REFERENCES basic_info(number));
        """
        self.execute_query(query, None)

    def create_table_links(self):
        query = """
        CREATE TABLE IF NOT EXISTS links (
            number    INTEGER,
            wiki_link TEXT
                CONSTRAINT fk_element_number
                    FOREIGN KEY (number)
                    REFERENCES basic_info(number));
        """
        self.execute_query(query, None)

    def create_all_tables(self):
        self.create_table_basic_info()
        self.create_table_basic_params()
        self.create_table_congregation()
        self.create_table_links()

    def drop_table(self, table_name: str):
        self.execute_query("DROP TABLE ?;", (table_name,))  # TODO

    def drop_all_tables(self):
        tables = ["basic_info", "basic_params", "congregation", "links"]
        for j in tables:
            self.drop_table(j)
