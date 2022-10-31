#!/usr/bin/env python

from base import DatabaseConnection
from src.chemistry import ChemistryLogicChecks


class DatabaseInsert(DatabaseConnection):
    def insert_basic_info(self, number: int, abb: str):
        number = ChemistryLogicChecks.check_number(number)
        abb = ChemistryLogicChecks.make_abb(abb)
        data = {"number": number, "abbreviation": abb}
        query = """
        INSERT INTO basic_info
        (number, abbreviation)
        VALUES (:number, :abbreviation);
        """
        self.execute_query(query, data)

    def insert_basic_params(self, number: int, name: str, group: str, weight: float, period: int):
        number = ChemistryLogicChecks.check_number(number)
        name = ChemistryLogicChecks.make_element_name(name)
        period = ChemistryLogicChecks.check_period(period)
        data = {"number": number, "name": name, "group": group, "weight": weight, "period": period}
        query = """
        INSERT INTO basic_params
        (number, name, group, period)
        VALUES (:number, :name, :group, :period);
        """
        self.execute_query(query, data)

    def insert_congregation(self,
                            number:        int,
                            energy_levels: int,
                            period:        int,
                            metal=False,
                            amphoteric=False,
                            gas=False,
                            semiconductor=False):
        number = ChemistryLogicChecks.check_number(number)
        energy_levels = ChemistryLogicChecks.check_energy_levels(energy_levels)
        ChemistryLogicChecks.check_amphoteric_metal(metal, amphoteric)
        data = {"number":        number,
                "energy_levels": energy_levels,
                "period":        period,
                "metal":         metal,
                "amphoteric":    amphoteric,
                "gas":           gas,
                "semiconductor": semiconductor}
        query = """
        INSERT INTO congregation 
        (number, energy_levels, period, metal, amphoteric, gas, semiconductor)
        VALUES (:number, :energy_levels, :period, :metal, :amphoteric, :gas, :semiconductor);
        """
        self.execute_query(query, data)

    def insert_links(self, number: int, wiki_link: str):
        number = ChemistryLogicChecks.check_number(number)
        data = {"number": number, "wiki_link": wiki_link}
        query = """
        INSERT INTO links
        (number, wiki_link)
        VALUES (:number, :wiki_link);
        """
        self.execute_query(query, data)
