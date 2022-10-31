#!/usr/bin/env python

import unittest
from src.database.create_table import DatabaseCreateTable
from src.database.insert import DatabaseInsert
from src.config import Configuration


class TestDatabaseConnection(unittest.TestCase):
    def setUp(self):
        self.config = Configuration()
        self.config.touch_config()
        self.config.read_config()
        with DatabaseCreateTable(self.config) as self.table_creator:
            self.table_creator.create_all_tables()
        self.database = DatabaseInsert(self.config)
        self.database.__enter__()

    def test_execute_any_query(self):
        self.database.execute_query("SELECT * from sqlite_master;", None)

    def test_basic_info(self):
        self.database.insert_basic_info(12, "Na")

    def test_basic_info_bad_params(self):
        self.assertRaises(AssertionError, self.database.insert_basic_info, (12,  "CHLORINE"))
        self.assertRaises(AssertionError, self.database.insert_basic_info, (0,   "Na"))
        self.assertRaises(AssertionError, self.database.insert_basic_info, (-20, "Na"))
        self.assertRaises(AssertionError, self.database.insert_basic_info, (12,  ""))

    def test_basic_params(self):
        params = {"number": 12,
                  "name":   "Sulfur",
                  "group":  "chalcogen",
                  "weight": 32.06,
                  "period": 16}  # TODO
        self.database.insert_basic_params(**params)

    def test_basic_params_bad_params(self):
        bad_params = {"number": -10,
                      "name":   "Phosphorus",
                      "group":  "pnictogen",
                      "weight": 30.97,
                      "period": 15}
        self.assertRaises(AssertionError, self.database.insert_basic_params, **bad_params)
        bad_params = {"number": -10,
                      "name":   "Phosphorus",
                      "group":  "somestuff",
                      "weight": 30.97,
                      "period": 15}
        self.assertRaises(AssertionError, self.database.insert_basic_params, **bad_params)
        bad_params = {"number": -10,
                      "name":   "Phosphorus",
                      "group":  "pnictogen",
                      "weight": 30.97,
                      "period": -3}
        self.assertRaises(AssertionError, self.database.insert_basic_params, **bad_params)
        bad_params = {"number": -10,
                      "name":   "Phosphorus",
                      "group":  "pnictogen",
                      "weight": 30.97,
                      "period": 22}
        self.assertRaises(AssertionError, self.database.insert_basic_params, **bad_params)
        bad_params = {"number": -10,
                      "name":   "",
                      "group":  "pnictogen",
                      "weight": 30.97,
                      "period": 15}
        self.assertRaises(AssertionError, self.database.insert_basic_params, **bad_params)

    def test_congregation(self):
        params = {"number":        12,
                  "energy_levels": 5,
                  "period":        11,
                  "metal":         True,
                  "amphoteric":    True,
                  "gas":           False,
                  "semiconductor": False}
        self.database.insert_congregation(**params)

    def test_congregation_bad_params(self):
        bad_params = {"number":        -1,
                      "energy_levels": 5,
                      "period":        11,
                      "metal":         True,
                      "amphoteric":    True,
                      "gas":           False,
                      "semiconductor": False}
        self.assertRaises(AssertionError, self.database.insert_basic_params, **bad_params)
        bad_params = {"number":        12,
                      "energy_levels": 0,
                      "period":        11,
                      "metal":         True,
                      "amphoteric":    True,
                      "gas":           False,
                      "semiconductor": False}
        self.assertRaises(AssertionError, self.database.insert_basic_params, **bad_params)
        bad_params = {"number": 12,
                      "energy_levels": 5,
                      "period":        22,
                      "metal":         True,
                      "amphoteric":    True,
                      "gas":           False,
                      "semiconductor": False}
        self.assertRaises(AssertionError, self.database.insert_basic_params, **bad_params)
        bad_params = {"number":        12,
                      "energy_levels": 5,
                      "period":        11,
                      "metal":         False,
                      "amphoteric":    True,
                      "gas":           False,
                      "semiconductor": False}
        self.assertRaises(AssertionError, self.database.insert_basic_params, **bad_params)

    def test_links(self):
        self.database.insert_links(number=12, wiki_link="en.wikipedia.org/wiki/Magnesium")

    def test_links_bad_params(self):
        bad_params = (-3, "en.wikipedia.org/wiki/Magnesium")
        self.assertRaises(AssertionError, self.database.insert_basic_params, bad_params)
        bad_params = (12, "")
        self.assertRaises(AssertionError, self.database.insert_basic_params, bad_params)
        bad_params = (0, "en.wikipedia.org/wiki/Magnesium")
        self.assertRaises(AssertionError, self.database.insert_basic_params, bad_params)

    def tearDown(self):
        self.database.__exit__()
        with DatabaseCreateTable(self.config) as self.table_creator:
            self.table_creator.drop_all_tables()
