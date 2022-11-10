"""ElementsTable class"""
import periodictable as PT
from .basic import ElementsGroupsInfo


class ElementsTable(ElementsGroupsInfo):
    """"Get information about chemical elements"""
    def __init__(self):
        self.elements = PT.elements

    def get_basic_info(self):
        """Get elements' symbols and number"""
        for j in self.elements:
            if j.name == "neutron":
                continue
            data = {"number": j.number,
                    "abb":    j.symbol}
            yield data

    def get_basic_params(self):
        """Get element's name, group, weight and period"""
        for j in self.elements:
            number = j.number
            if not number:
                continue
            match number:
                case _ if number in self.alkali_metal:
                    group = "alkali-metal"
                case  _ if number in self.alkaline_earth_metals:
                    group = "alkaline-earth-metal"
                case  _ if number in self.metalloid:
                    group = "metalloid"
                case  _ if number in self.reactive_nonmetals:
                    group = "reactive-nonmetal"
                case  _ if number in self.transition_metals:
                    group = "transition-metal"
                case  _ if number in self.noble_gas:
                    group = "noble-gas"
                case  _ if number in self.pnictogen:
                    group = "pnictogen"
                case  _ if number in self.chalcogen:
                    group = "chalcogen"
                case  _ if number in self.actinoid:
                    group = "actinoid"
                case  _ if number in self.lanthanoid:
                    group = "lanthanoid"
                case _:
                    group = "NULL"
            for period in range(1, 19):
                if j.number in self.periods[str(period)]:
                    break
            data = {"number": number,
                    "name":   j.name,
                    "weight": j.mass,
                    "grp":    group,
                    "period": period}
            yield data

    def get_congregation(self):
        """Get some other stuff"""
        for j in self.elements:
            number = j.number
            if not number:
                continue
            energy_level = None
            for n, energy_level in self.energy_levels.items():
                if number in energy_level:
                    break
            metal = number not in self.not_metals
            amphoteric = number in self.amphoteric
            gas = number in self.gases
            semiconductor = number in self.semiconductors
            data = {"number":        number,
                    "metal":         metal,
                    "amphoteric":    amphoteric,
                    "energy_levels": int(n),
                    "gas":           gas,
                    "semiconductor": semiconductor}
            yield data

    def get_links(self):
        """Get wiki links for every element"""
        for j in self.elements:
            number = j.number
            if not number:
                continue
            wiki_link = "https://en.wikipedia.org/wiki/" + j.name
            data = {"number": number, "wiki_link": wiki_link}
            yield data
