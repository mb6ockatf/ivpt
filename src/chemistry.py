#!/usr/bin/env python

from re import search


class ChemistryLogicChecks(object):
    @staticmethod
    def make_abb(abb: str) -> str:
        assert not bool(search(r'\d', abb)), "no digits in element's abbreviation"
        assert len(abb) < 3, "abbreviation is shorter, than 3 characters"
        abb = abb.lower()
        abb = abb.capitalize()
        return abb

    @staticmethod
    def check_number(number: int):
        assert number > 0, "element's number is a positive value"
        return number

    @staticmethod
    def check_amphoteric_metal(metal: bool, amphoteric: bool):
        if amphoteric:
            assert metal, "amphoteric element always has metal properties"

    @staticmethod
    def check_period(period: int):
        assert 0 < period, "period value is bigger than 0"
        assert period < 19, "period value is less than 19"

    @staticmethod
    def check_energy_levels(energy_level_value: int):
        assert 0 < energy_level_value, "energy level is bigger than 0"
        assert energy_level_value < 8, "energy level is smaller than 8"


if __name__ == "__main__":
    ChemistryLogicChecks.make_abb("AB")
