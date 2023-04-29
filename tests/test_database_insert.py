#!/usr/bin/env python3
import unittest
from sqlite3 import OperationalError
from src.database import DatabaseCreateTable, DatabaseInsert
from src.elements import ElementsTable
from src.essential import configuration


class TestDatabaseConnection(unittest.TestCase):
    def setUp(self):
        self.config = configuration()
        table_creator = DatabaseCreateTable(self.config)
        table_creator.create_all_tables()
        table_creator.close()
        self.database = DatabaseInsert(self.config)

    def test_execute_any_query(self):
        self.database.execute_query("SELECT * from sqlite_master;", None)

    def test_basic_info(self):
        self.database.insert_basic_info(12, "Na")

    def test_basic_info_bad_params(self):
        action = self.database.insert_basic_info
        params = {"number": 12, "abb": "CHLORINE"}
        self.assertRaises(AssertionError, action, **params)
        params = {"number": 0, "abb": "Na"}
        self.assertRaises(AssertionError, action, **params)
        params = {"number": -20, "abb": "Na"}
        self.assertRaises(AssertionError, action, **params)
        params = {"number": 12, "abb": ""}
        self.assertRaises(AssertionError, action, **params)

    def test_basic_params(self):
        params = {"number": 12, "name": "Sulfur", "grp": "chalcogen",
                  "weight": 32.06, "period": 16}
        self.database.insert_basic_params(**params)

    def test_basic_params_bad_params(self):
        action = self.database.insert_basic_params
        params = {"number": -10, "name": "Phosphorus", "grp": "pnictogen",
                  "weight": 30.97, "period": 15}
        self.assertRaises(AssertionError, action, **params)
        params = {"number": -10, "name": "Phosphorus", "grp": "somestuff",
                  "weight": 30.97, "period": 15}
        self.assertRaises(AssertionError, action, **params)
        params = {"number": -10, "name": "Phosphorus", "grp": "pnictogen",
                  "weight": 30.97, "period": -3}
        self.assertRaises(AssertionError, action, **params)
        params = {"number": -10, "name": "Phosphorus", "grp": "pnictogen",
                  "weight": 30.97, "period": 22}
        self.assertRaises(AssertionError, action, **params)
        params = {"number": -10, "name": "", "grp": "pnictogen",
                  "weight": 30.97, "period": 15}
        self.assertRaises(AssertionError, action, **params)

    def test_congregation(self):
        params = {"number": 12, "energy_levels": 5, "metal": True,
                  "amphoteric": True, "gas": False, "semiconductor": False}
        self.database.insert_congregation(**params)

    def test_congregation_bad_params(self):
        action = self.database.insert_congregation
        params = {"number": -1, "energy_levels": 5, "metal": True,
                  "amphoteric": True, "gas": False, "semiconductor": False}
        self.assertRaises(AssertionError, action, **params)
        params = {"number": 12, "energy_levels": 0, "metal": True,
                  "amphoteric": True, "gas": False, "semiconductor": False}
        self.assertRaises(AssertionError, action, **params)
        self.assertRaises(AssertionError, action, **params)
        params = {"number": 12, "energy_levels": 5, "metal": False,
                  "amphoteric": True, "gas": False, "semiconductor": False}
        self.assertRaises(AssertionError, action, **params)

    def test_links(self):
        params = {"number": 12, "wiki_link": "en.wikipedia.org/wiki/Magnesium"}
        self.database.insert_links(**params)

    def test_links_bad_params(self):
        action = self.database.insert_links
        args = {"number": -3, "wiki_link": "en.wikipedia.org/wiki/Magnesium"}
        self.assertRaises(AssertionError, action, **args)
        args = {"number": 12, "wiki_link": ""}
        self.assertRaises(AssertionError, action, **args)
        args = {"number": 0, "wiki_link": "en.wikipedia.org/wiki/Magnesium"}
        self.assertRaises(AssertionError, action, **args)

    def tearDown(self):
        self.database.close()
        self.table_creator = DatabaseCreateTable(self.config)
        self.table_creator.drop_all_tables()
        self.table_creator.close()
