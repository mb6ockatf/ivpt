#!/usr/bin/env python3
"""DatabaseInsert class"""
from src.database.base import DatabaseConnection
from src.chemistry import ChemistryLogicChecks


class DatabaseInsert(DatabaseConnection):
    """Insert data into database tables"""
    def insert_basic_info(self, number: int, abb: str):
        """
        Insert element's number and symbol into basic_info table
        """
        number = ChemistryLogicChecks.check_number(number)
        abb = ChemistryLogicChecks.make_abb(abb)
        data = {"number": number, "abbreviation": abb}
        query = """
        INSERT INTO basic_info
        (number, abbreviation)
        VALUES (:number, :abbreviation);
        """
        self.execute_query(query, data)

    def insert_basic_params(self, **kvargs):
        """
        Check & insert element's number, name, group, mass (weight) and period
        into basic_params table
        """
        number = ChemistryLogicChecks.check_number(kvargs["number"])
        name = ChemistryLogicChecks.make_name(kvargs["name"])
        group = ChemistryLogicChecks.check_group(kvargs["grp"])
        period = ChemistryLogicChecks.check_period(kvargs["period"])
        weight = ChemistryLogicChecks.check_weight(kvargs["weight"])
        period = ChemistryLogicChecks.check_period(kvargs["period"])
        data = {"number": number,
                "name":   name,
                "grp":    group,
                "weight": weight,
                "period": period}
        query = """
        INSERT INTO basic_params
        (number, name, grp, weight, period)
        VALUES (:number, :name, :grp, :weight, :period);
        """
        self.execute_query(query, data)

    def insert_congregation(self,
                            number:        int,
                            energy_levels: int,
                            metal=False,
                            amphoteric=False,
                            gas=False,
                            semiconductor=False):
        """
        Check & insert element's number, energy_levels, period,
        metal-param, amphoteric-param, gas-param, semiconductor-param
        into congregation table
        """
        number = ChemistryLogicChecks.check_number(number)
        energy_levels = ChemistryLogicChecks.check_energy_levels(energy_levels)
        ChemistryLogicChecks.check_amphoteric_metal(metal, amphoteric)
        data = {"number":        number,
                "energy_levels": energy_levels,
                "metal":         metal,
                "amphoteric":    amphoteric,
                "gas":           gas,
                "semiconductor": semiconductor}
        query = """
        INSERT INTO congregation 
        (number, energy_levels, metal, amphoteric, gas, semiconductor)
        VALUES (:number,
                :energy_levels,
                :metal, 
                :amphoteric,
                :gas, 
                :semiconductor);
        """
        self.execute_query(query, data)

    def insert_links(self, number: int, wiki_link: str):
        """Check & insert elements's name and wiki link into links table"""
        number = ChemistryLogicChecks.check_number(number)
        wiki_link = ChemistryLogicChecks.check_link(wiki_link)
        data = {"number": number, "wiki_link": wiki_link}
        query = """
        INSERT INTO links
        (number, wiki_link)
        VALUES (:number, :wiki_link);
        """
        self.execute_query(query, data)
