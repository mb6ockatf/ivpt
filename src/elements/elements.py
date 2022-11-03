#!/usr/bin/env python3
"""ElementsTable class"""
import periodictable as PT
from basic import ElementsGroupsInfo


class ElementsTable(ElementsGroupsInfo):
    """"Get information about chemical elements"""
    def __init__(self):
        self.elements = PT.elements

    def get_basic_info(self):
        """Get elements' symbols and number"""
        number = 0
        for j in self.elements:
            number += 1
            data = {"number": number,
                    "abb":    j.symbol}
            yield data

    def get_basic_params(self):
        """Get element's name, group, weight and period"""
        number = 0
        for j in self.elements:
            number += 1
            match j.number:
                case self.alkali_metal:
                    group = "alkali-metal"
                case self.alkaline_earth_metals:
                    group = "alkaline-earth-metal"
                case self.metalloid:
                    group = "metalloid"
                case self.reactive_nonmetals:
                    group = "reactive-nonmetal"
                case self.transition_metals:
                    group = "transition-metal"
                case self.noble_gas:
                    group = "noble-gas"
                case self.pnictogen:
                    group = "pnictogen"
                case self.chalcogen:
                    group = "chalcogen"
                case self.actinoid:
                    group = "actinoid"
                case self.lanthanoid:
                    group = "lanthanoid"
                case _:
                    group = "NULL"
            for period in range(1, 19):
                if j.number in self.periods[period]:
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
            period_column = None
            for period_column in self.periods.keys():
                if number in self.periods[period_column]:
                    break
            energy_level = None
            for energy_level in self.energy_levels.keys():
                if number in self.energy_levels[energy_level]:
                    break
            metal = number not in self.not_metals
            amphoteric = number in self.amphoteric
            gas = number in self.gases
            semiconductor = number in self.semiconductors
            data = {"number":        number,
                    "metal":         metal,
                    "amphoteric":    amphoteric,
                    "energy_levels": energy_level,
                    "gas":           gas,
                    "semiconductor": semiconductor}
            yield data

    def get_links(self):
        """Get wiki links for every element"""
        for j in self.elements:
            name = j.name
            link = "https://en.wikipedia.org/wiki/" + name
            yield link

a = ElementsTable()
for element in a.get_congregation():
    print(element)
