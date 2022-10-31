#!/usr/bin/env python

from re import search


class ChemistryLogicChecks(object):
    @staticmethod
    def make_abb(abb: str) -> str:
        assert not bool(search(r"\d", abb)), "no digits in element's abbreviation"
        assert len(abb) < 3, "abbreviation is shorter, than 3 characters"
        assert len(abb) > 0, "abbreviation has a positive length"
        abb = abb.lower()
        abb = abb.capitalize()
        return abb

    @staticmethod
    def check_number(number: int) -> int:
        assert number > 0, "element's number is a positive value"
        return number

    @staticmethod
    def check_amphoteric_metal(metal: bool, amphoteric: bool):
        if amphoteric:
            assert metal, "amphoteric element always has metal properties"

    @staticmethod
    def check_period(period: int) -> int:
        assert 0 < period, "period value is bigger than 0"
        assert period < 19, "period value is less than 19"
        return period

    @staticmethod
    def check_energy_levels(energy_level_value: int) -> int:
        assert 0 < energy_level_value, "energy level is bigger than 0"
        assert energy_level_value < 8, "energy level is smaller than 8"
        return energy_level_value

    @staticmethod
    def make_element_name(element_name: str) -> str:
        assert len(element_name) > 0
        element_name = element_name.lower()
        element_name = element_name.capitalize()
        return element_name
