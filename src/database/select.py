#!/usr/bin/env python3

from src.database.base import DatabaseConnection


class DatabaseSelect(DatabaseConnection):
    def select_basic_info(self):
        query = """
        SELECT number, abbreviation
        FROM basic_info
        ORDER BY 1;
        """
        self.execute_query(query, None)

    def select_basic_params(self, element_number: int):
        query = """
        SELECT name, grp, period
        FROM basic_param
        WHERE number = ?;
        """
        self.execute_query(query, (element_number,))

    def select_congregation(self, element_number: int):
        query = """
        SELECT energy_levels, period, metal, amphoteric, gas, semiconductor
        FROM congregation
        WHERE number = ?;
        """
        self.execute_query(query, (element_number,))

    @staticmethod
    def select_links(self, element_number: int):
        query = """
        SELECT wiki_link FROM links
        WHERE number = ?;
        """
        self.execute_query(query, (element_number,))