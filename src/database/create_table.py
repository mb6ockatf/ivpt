#!/usr/bin/env python3
"""DatabaseCreateTable class"""
from src.database.base import DatabaseConnection


class DatabaseCreateTable(DatabaseConnection):
    """Create & drop database tables"""
    def create_table_basic_info(self):
        """Create basic_info table"""
        query = """
        CREATE TABLE IF NOT EXISTS basic_info (
            number INTEGER UNSIGNED NOT NULL,
            abbreviation TEXT UNIQUE NOT NULL, 
                CONSTRAINT number_pk
                PRIMARY KEY (number));
        """
        self.execute_query(query, None)

    def create_table_basic_params(self):
        """Create basic_params table"""
        query = """
        CREATE TABLE IF NOT EXISTS basic_params (
            number  INTEGER UNSIGNED UNIQUE NOT NULL,
            name    TEXT             UNIQUE NOT NULL,
            weight  REAL             UNIQUE NOT NULL,
            grp     TEXT,
            period  INTEGER UNSIGNED,
                CONSTRAINT fk_element_number
                    FOREIGN KEY (number)
                    REFERENCES basic_info(number));
        """
        self.execute_query(query, None)

    def create_table_congregation(self):
        """Create congregation table"""
        query = """
        CREATE TABLE IF NOT EXISTS congregation (
            number        INTEGER UNSIGNED UNIQUE NOT NULL,
            metal         INTEGER UNSIGNED DEFAULT 0,
            amphoteric    INTEGER UNSIGNED DEFAULT 0,
            energy_levels INTEGER UNSIGNED,
            gas           INTEGER UNSIGNED DEFAULT 0,
            semiconductor INTEGER UNSIGNED DEFAULT 0,
                CONSTRAINT fk_element_number
                    FOREIGN KEY (number)
                    REFERENCES basic_info(number));
        """
        self.execute_query(query, None)

    def create_table_links(self):
        """Create links table"""
        query = """
        CREATE TABLE IF NOT EXISTS links (
            number    INTEGER,
            wiki_link TEXT,
                CONSTRAINT fk_element_number
                    FOREIGN KEY (number)
                    REFERENCES basic_info(number));
        """
        self.execute_query(query, None)

    def create_all_tables(self):
        """Call all tables' creation methods"""
        self.create_table_basic_info()
        self.create_table_basic_params()
        self.create_table_congregation()
        self.create_table_links()

    def drop_basic_info(self):
        """Drop basic_info table"""
        self.execute_query("DROP TABLE basic_info;", None)

    def drop_basic_params(self):
        """Drop basic_params table"""
        self.execute_query("DROP TABLE basic_params;", None)

    def drop_congregation(self):
        """Drop congregation table"""
        self.execute_query("DROP TABLE congregation;", None)

    def drop_links(self):
        """Drop links table"""
        self.execute_query("DROP TABLE links;", None)

    def drop_all_tables(self):
        """Call all tables' destructive methods"""
        self.drop_basic_info()
        self.drop_basic_params()
        self.drop_congregation()
        self.drop_links()
