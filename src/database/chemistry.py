"""ChemistryLogicChecks class"""
from re import search


class ChemistryLogicChecks:
    """Check some chemistry logic"""
    @staticmethod
    def make_abb(abb: str) -> str:
        """Check element's symbol (abbreviation)"""
        assert not bool(search(r"\d", abb)), "no digits in abbreviation"
        assert len(abb) < 3, "abbreviation is shorter, than 3 characters"
        assert len(abb) > 0, "abbreviation has a positive length"
        abb = abb.lower()
        abb = abb.capitalize()
        return abb

    @staticmethod
    def check_number(number: int) -> int:
        """Check element's number"""
        assert number > 0, "element's number is a positive value"
        return number

    @staticmethod
    def check_amphoteric_metal(metal: bool, amphoteric: bool):
        """Check amphoteric & metal dependency"""
        if amphoteric:
            assert metal, "amphoteric element always has metal properties"

    @staticmethod
    def check_period(period: int) -> int:
        """Check element's period"""
        assert 0 < period, "period value is bigger than 0"
        assert period < 19, "period value is less than 19"
        return period

    @staticmethod
    def check_energy_levels(energy_level_value: int) -> int:
        """Check elements' energy level value"""
        assert 0 < energy_level_value, "energy level is bigger than 0"
        assert energy_level_value < 8, "energy level is smaller than 8"
        return energy_level_value

    @staticmethod
    def make_name(element_name: str) -> str:
        """Capitalize element's name"""
        assert len(element_name) > 0
        element_name = element_name.lower()
        element_name = element_name.capitalize()
        return element_name

    @staticmethod
    def check_group(element_group: str) -> str:
        """Check if element's group exist"""
        possible_groups = ("alkali-metal",
                            "alkaline-earth-metal",
                            "metalloid",
                            "reactive-nonmetal",
                            "transition-metal",
                            "noble-gas",
                            "pnictogen",
                            "chalcogen",
                            "actinoid",
                            "lanthanoid",
                            "NULL")
        assert element_group in possible_groups, "group name not permitted"
        return element_group

    @staticmethod
    def check_link(link: str) -> str:
        """Check if link string is not empty"""
        assert len(link) > 0, "link length is positive"
        return link

    @staticmethod
    def check_weight(weight: float) -> float:
        """Check if mass (weight) value is positive"""
        assert weight > 0, "weight is a positive value"
        return weight
