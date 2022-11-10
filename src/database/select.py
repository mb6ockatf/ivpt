"""DatabaseSelect class"""
from .base import DatabaseConnection


class DatabaseSelect(DatabaseConnection):

    """Select data from database tables"""

    def select_basic_info(self) -> tuple:
        """
        Get elements' numbers and symbols from table basic_info
        """
        query = """
        SELECT number, abbreviation
        FROM basic_info
        ORDER BY number;
        """
        process = self.execute_query(query, None)
        return process

    def select_basic_params(self, element_number: int) -> tuple:
        """
        Get elements' name, weight, group
        and period from table basic_params

        :element_number: int
        element's number in periodic table
        """
        query = """
        SELECT name, weight, grp, period
        FROM basic_params
        WHERE number = ?;
        """
        process = self.execute_query(query, (element_number,))
        return process

    def select_congregation(self, element_number: int) -> tuple:
        """
        Get elements' metal parameter, amphoteric parameter,
        energy level's value, gas parameter,
        and semiconductor parameter from table congregation

        :element_number: int
        element's number in periodic table
        """
        query = """
        SELECT metal, amphoteric, energy_levels, gas, semiconductor
        FROM congregation
        WHERE number = ?;
        """
        process = self.execute_query(query, (element_number,))
        return process

    def select_links(self, element_number: int) -> tuple:
        """
        Get elements' wiki link from table links

        :element_number: int
        element's number in periodic table
        """
        query = """
        SELECT wiki_link FROM links
        WHERE number = ?;
        """
        process = self.execute_query(query, (element_number,))
        return process
