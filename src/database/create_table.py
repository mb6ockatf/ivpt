from .base import DatabaseConnection


class DatabaseCreateTable(DatabaseConnection):
    def create_table_basic_info(self) -> tuple:
        query = """CREATE TABLE IF NOT EXISTS basic_info (
        number INTEGER UNSIGNED NOT NULL,
        abbreviation TEXT UNIQUE NOT NULL,
        CONSTRAINT number_pk PRIMARY KEY (number));"""
        return self.execute_query(query, None)

    def create_table_basic_params(self) -> tuple:
        query = """CREATE TABLE IF NOT EXISTS basic_params (
            number  INTEGER UNSIGNED UNIQUE NOT NULL,
            name    TEXT             UNIQUE NOT NULL,
            weight  REAL             		NOT NULL,
            grp     TEXT,
            period  INTEGER UNSIGNED,
            CONSTRAINT fk_element_number
            FOREIGN KEY (number) REFERENCES basic_info(number));"""
        return self.execute_query(query, None)

    def create_table_congregation(self) -> tuple:
        query = """CREATE TABLE IF NOT EXISTS congregation (
            number        INTEGER UNSIGNED UNIQUE NOT NULL,
            metal         INTEGER UNSIGNED DEFAULT 0,
            amphoteric    INTEGER UNSIGNED DEFAULT 0,
            energy_levels INTEGER UNSIGNED,
            gas           INTEGER UNSIGNED DEFAULT 0,
            semiconductor INTEGER UNSIGNED DEFAULT 0,
            CONSTRAINT fk_element_number
            FOREIGN KEY (number) REFERENCES basic_info(number));"""
        return self.execute_query(query, None)

    def create_table_links(self) -> tuple:
        query = """CREATE TABLE IF NOT EXISTS links (
            number INTEGER, wiki_link TEXT,
            CONSTRAINT fk_element_number
            FOREIGN KEY (number) REFERENCES basic_info(number));"""
        return self.execute_query(query, None)

    def create_all_tables(self) -> list:
        process = [self.create_table_basic_info()]
        process.append(self.create_table_basic_params())
        process.append(self.create_table_congregation())
        process.append(self.create_table_links())
        return process

    def drop_basic_info(self) -> tuple:
        return self.execute_query("DROP TABLE basic_info;", None)

    def drop_basic_params(self) -> tuple:
        return self.execute_query("DROP TABLE basic_params;", None)

    def drop_congregation(self) -> tuple:
        return self.execute_query("DROP TABLE congregation;", None)

    def drop_links(self) -> tuple:
        return self.execute_query("DROP TABLE links;", None)

    def drop_all_tables(self) -> list:
        process = [self.drop_basic_info()]
        process.append(self.drop_basic_params())
        process.append(self.drop_congregation())
        process.append(self.drop_links())
        return process
