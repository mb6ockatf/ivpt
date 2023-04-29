from .chemistry import ChemistryLogicChecks as chemistry
from .base import DatabaseConnection


class DatabaseInsert(DatabaseConnection):
    def insert_basic_info(self, number: int, abb: str) -> tuple:
        number = chemistry.check_number(number)
        abb = chemistry.make_abb(abb)
        data = {"number": number, "abbreviation": abb}
        query = """INSERT INTO basic_info (number, abbreviation)
                VALUES (:number, :abbreviation);"""
        return self.execute_query(query, data)

    def insert_basic_params(self, **kvargs) -> tuple:
        number = chemistry.check_number(kvargs["number"])
        name = chemistry.make_name(kvargs["name"])
        group = chemistry.check_group(kvargs["grp"])
        period = chemistry.check_period(kvargs["period"])
        weight = chemistry.check_weight(kvargs["weight"])
        period = chemistry.check_period(kvargs["period"])
        data = {"number": number, "name": name, "grp": group, "weight": weight,
                "period": period}
        query = """INSERT INTO basic_params (number, name, grp, weight, period)
        VALUES (:number, :name, :grp, :weight, :period);"""
        return self.execute_query(query, data)

    def insert_congregation(self, **kvargs) -> tuple:
        """
        :number:        int,
        :energy_levels: int,
        :metal:         =False,
        :amphoteric:    =False,
        :gas:           =False,
        :semiconductor: =False
        Check & insert element's number, energy_levels, period,
        metal-param, amphoteric-param, gas-param, semiconductor-param
        into congregation table
        """
        if "metal" not in kvargs:
            kvargs["metal"] = False
        if "amphoteric" not in kvargs:
            kvargs["amphoteric"] = False
        if "gas" not in kvargs:
            kvargs["gas"] = False
        if "semiconductor" not in kvargs:
            kvargs["semiconductor"] = False
        number = chemistry.check_number(kvargs["number"])
        energy_levels = chemistry.check_energy_levels(kvargs["energy_levels"])
        chemistry.check_amphoteric_metal(kvargs["metal"], kvargs["amphoteric"])
        data = {"number": number, "energy_levels": energy_levels,
                "metal": kvargs["metal"], "amphoteric": kvargs["amphoteric"],
                "gas": kvargs["gas"], "semiconductor": kvargs["semiconductor"]}
        query = """INSERT INTO congregation
            (number, energy_levels, metal, amphoteric, gas, semiconductor)
        VALUES (:number, :energy_levels, :metal, :amphoteric, :gas,\
            :semiconductor);"""
        return self.execute_query(query, data)

    def insert_links(self, number: int, wiki_link: str) -> tuple:
        number = chemistry.check_number(number)
        wiki_link = chemistry.check_link(wiki_link)
        data = {"number": number, "wiki_link": wiki_link}
        query = """INSERT INTO links (number, wiki_link)
            VALUES (:number, :wiki_link);"""
        return self.execute_query(query, data)