from .periodic_table import PeriodicTable
from .basic import ElementsGroupsInfo


class ElementsTable(ElementsGroupsInfo):
    def __init__(self):
       self.elements = PeriodicTable()

    def get_basic_info(self):
        for j in self.elements:
            data = {"number": j.number, "abb": j.symbol}
            yield data

    def get_basic_params(self):
        for j in self.elements:
            if j.number in self.alkali_metal:
                group = "alkali-metal"
            elif j.number in self.alkaline_earth_metals:
                group = "alkaline-earth-metal"
            elif j.number in self.metalloid:
                group = "metalloid"
            elif j.number in self.reactive_nonmetals:
                group = "reactive-nonmetal"
            elif j.number in self.transition_metals:
                group = "transition-metal"
            elif j.number in self.noble_gas:
                group = "noble-gas"
            elif j.number in self.pnictogen:
                group = "pnictogen"
            elif j.number in self.chalcogen:
                group = "chalcogen"
            elif j.number in self.actinoid:
                group = "actinoid"
            elif j.number in self.lanthanoid:
                group = "lanthanoid"
            else:
                group = "NULL"
            for period in range(1, 19):
                if j.number in self.periods[str(period)]:
                    break
            data = {"number": j.number, "name": j.name, "weight": j.mass,
                    "grp": group, "period": period}
            yield data

    def get_congregation(self):
        for j in self.elements:
            number = j.number
            energy_level = None
            for n, energy_level in self.energy_levels.items():
                if j.number in energy_level:
                    break
            metal = j.number not in self.not_metals
            amphoteric = j.number in self.amphoteric
            gas = j.number in self.gases
            semiconductor = j.number in self.semiconductors
            data = {"number": j.number, "metal": metal,
                    "amphoteric": amphoteric, "energy_levels": int(n),
                    "gas": gas, "semiconductor": semiconductor}
            yield data

    def get_links(self):
        for j in self.elements:
            number = j.number
            wiki_link = "https://en.wikipedia.org/wiki/" + j.name
            data = {"number": number, "wiki_link": wiki_link}
            yield data
