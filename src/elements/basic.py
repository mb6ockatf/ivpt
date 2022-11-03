#!/usr/bin/env python3
"""ElementsGroupsInfo class"""


class ElementsGroupsInfo:
    """Gather element numbers into groups"""

    @property
    def actinoid(self) -> set:
        """Get actinoids' range of numbers"""
        return {*range(89, 104)}

    @property
    def lanthanoid(self) -> set:
        """Get lanthanoids' range of numbers"""
        return {*range(57, 72)}

    @property
    def alkali_metal(self) -> tuple:
        """Get alkali-metals' range of numbers"""
        return (3, 11, 19, 37, 55, 87)

    @property
    def alkaline_earth_metals(self) -> tuple:
        """Get alkaline-earth-metals' range of numbers"""
        return (4, 12, 20, 38, 56, 88)

    @property
    def metalloid(self) -> tuple:
        """Get metalloids' range of numbers"""
        return (5, 14, 32, 52)

    @property
    def reactive_nonmetals(self) -> set:
        """Get reactive nonmetals' range of numbers"""
        result = {1, 10, 18, 36, 54, 8}
        result += {53, 35, 17, 9}
        result += {16, 8}
        return result

    @property
    def transition_metals(self) -> set:
        """Get transition metals' range of numbers"""
        result = {*range(21, 31)}
        result += {*range(39, 49)}
        result += {*range(71, 81)}
        result += {*range(103, 113)}
        return result

    @property
    def noble_gas(self) -> tuple:
        """Get noble gases' range of numbers"""
        return (2, 10, 18, 36, 54, 86, 118)

    @property
    def pnictogen(self) -> tuple:
        """Get pnictogens' range of numbers"""
        return (7, 15, 33, 51, 83, 115)

    @property
    def chalcogen(self) -> tuple:
        """Get chalcogens' range of numbers"""
        return (8, 16, 34, 52, 84, 116)

    @property
    def periods(self) -> dict:
        """Get 18 periods' range of numbers"""
        result = {}
        increment = lambda x: x + 1
        result["1"] = {1, 3, 11, 19, 37, 55, 87}
        result["2"] = {*map(increment, [*result["1"]][1:])}
        result["3"] = {21, 39}
        result["3"] = result["3"] | self.lanthanoid
        result["3"] = result["3"] | self.actinoid
        result["4"] = {22, 40, 72, 104}
        result["5"] = {*map(increment, [*result["4"]])}
        result["6"] = {*map(increment, [*result["5"]])}
        result["7"] = {*map(increment, [*result["6"]])}
        result["8"] = {*map(increment, [*result["7"]])}
        result["9"] = {*map(increment, [*result["8"]])}
        result["10"] = {*map(increment, [*result["9"]])}
        result["11"] = {*map(increment, [*result["10"]])}
        result["12"] = {*map(increment, [*result["11"]])}
        result["13"] = {5, 13, 21, 49, 81, 113}
        result["14"] = {*map(increment, [*result["13"]])}
        result["15"] = {*map(increment, [*result["14"]])}
        result["16"] = {*map(increment, [*result["15"]])}
        result["17"] = {*map(increment, [*result["16"]])}
        result["18"] = [2] + [*map(increment, [*result["17"]])]
        result["18"] = {*result["18"]}
        return result

    @property
    def not_metals(self) -> set:
        """Get not-metals' range of elements"""
        not_metals = self.periods["18"]
        not_metals = not_metals | self.periods["17"]
        not_metals = not_metals | {8, 16, 34, 7, 15, 6}
        not_metals = not_metals | {*[*range(109, 119)]}
        return not_metals

    @property
    def amphoteric(self) -> tuple:
        """Get amphoteric elements' range of numbers"""
        return (29, 30, 13, 4, 50, 82)

    @property
    def energy_levels(self) -> set:
        """Get elements' energy levels"""
        result = {}
        result["1"] = {1, 2}
        result["2"] = {*range(3, 11)}
        result["3"] = {*range(11, 19)}
        result["4"] = {*range(19, 37)}
        result["5"] = {*range(37, 55)}
        result["6"] = {*range(55, 87)}
        result["7"] = {*range(87, 119)}
        return result

    @property
    def gases(self) -> tuple:
        """Get gas-elements' numbers"""
        return (1, 7, 8, 9, 17)

    @property
    def semiconductors(self) -> tuple:
        """Get semiconductors' numbers"""
        return (14, 16, 32, 33, 50)
