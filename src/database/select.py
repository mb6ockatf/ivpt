"""DatabaseSelect class"""
from .base import DatabaseConnection


class DatabaseSelect(DatabaseConnection):
    def select_basic_info(self) -> tuple:
        query = """SELECT number, abbreviation FROM basic_info
        ORDER BY number;"""
        return self.execute_query(query, None)

    def select_basic_params(self, element_number: int) -> tuple:
        query = """SELECT name, weight, grp, period FROM basic_params
        WHERE number = ?;"""
        return self.execute_query(query, (element_number,))

    def select_congregation(self, element_number: int) -> tuple:
        query = """SELECT metal, amphoteric, energy_levels, gas, semiconductor
        FROM congregation WHERE number = ?;"""
        return self.execute_query(query, (element_number,))

    def select_links(self, element_number: int) -> tuple:
        query = """SELECT wiki_link FROM links WHERE number = ?;"""
        return self.execute_query(query, (element_number,))
