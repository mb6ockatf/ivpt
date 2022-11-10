"""DatabaseCreateTable class"""
from .base import DatabaseConnection


class DatabaseCreateTable(DatabaseConnection):

    """Create & drop database tables"""

    def create_table_basic_info(self) -> tuple:
        """Create basic_info table"""
        query = """
        CREATE TABLE IF NOT EXISTS basic_info (
            number INTEGER UNSIGNED NOT NULL,
            abbreviation TEXT UNIQUE NOT NULL, 
                CONSTRAINT number_pk
                PRIMARY KEY (number));
        """
        process = self.execute_query(query, None)
        return process

    def create_table_basic_params(self) -> tuple:
        """Create basic_params table"""
        query = """
        CREATE TABLE IF NOT EXISTS basic_params (
            number  INTEGER UNSIGNED UNIQUE NOT NULL,
            name    TEXT             UNIQUE NOT NULL,
            weight  REAL             		NOT NULL,
            grp     TEXT,
            period  INTEGER UNSIGNED,
                CONSTRAINT fk_element_number
                    FOREIGN KEY (number)
                    REFERENCES basic_info(number));
        """
        process = self.execute_query(query, None)
        return process

    def create_table_congregation(self) -> tuple:
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
        process = self.execute_query(query, None)
        return process

    def create_table_links(self) -> tuple:
        """Create links table"""
        query = """
        CREATE TABLE IF NOT EXISTS links (
            number    INTEGER,
            wiki_link TEXT,
                CONSTRAINT fk_element_number
                    FOREIGN KEY (number)
                    REFERENCES basic_info(number));
        """
        process = self.execute_query(query, None)
        return process

    def create_all_tables(self) -> list:
        """Call all tables' creation methods"""
        process = []
        process += [self.create_table_basic_info()]
        process += [self.create_table_basic_params()]
        process += [self.create_table_congregation()]
        process += [self.create_table_links()]
        return process

    def drop_basic_info(self) -> tuple:
        """Drop basic_info table"""
        process = process = self.execute_query("DROP TABLE basic_info;", None)
        return process

    def drop_basic_params(self) -> tuple:
        """Drop basic_params table"""
        process = self.execute_query("DROP TABLE basic_params;", None)
        return process

    def drop_congregation(self) -> tuple:
        """Drop congregation table"""
        process = self.execute_query("DROP TABLE congregation;", None)
        return process

    def drop_links(self) -> tuple:
        """Drop links table"""
        process = self.execute_query("DROP TABLE links;", None)
        return process

    def drop_all_tables(self) -> list:
        """Call all tables' destructive methods"""
        process = []
        process += [self.drop_basic_info()]
        process += [self.drop_basic_params()]
        process += [self.drop_congregation()]
        process += [self.drop_links()]
        return process
