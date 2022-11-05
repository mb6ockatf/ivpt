#!/usr/bin/env python3
"""TestDatabaseConnection testcase"""
import unittest
from src.database import DatabaseCreateTable
from src.database import DatabaseInsert
from src.essential.config import configuration


class TestDatabaseConnection(unittest.TestCase):
    """Test database insert methods"""
    def setUp(self):
        """Create tables & open database connection"""
        self.config = configuration()
        self.table_creator = DatabaseCreateTable(self.config)
        self.table_creator.create_all_tables()
        self.table_creator.close()
        self.database = DatabaseInsert(self.config)

    def test_execute_any_query(self):
        """Test if at least any query can be executed"""
        self.database.execute_query("SELECT * from sqlite_master;", None)

    def test_basic_info(self):
        """Test if right values can be inserted into basic_info table"""
        self.database.insert_basic_info(12, "Na")

    def test_basic_info_bad_params(self):
        """Test if AssertionError raises on bad queries to basic_info table"""
        params = {"number": 12, "abb": "CHLORINE"}
        self.assertRaises(AssertionError,
                          self.database.insert_basic_info,
                          **params)
        params = {"number": 0, "abb": "Na"}
        self.assertRaises(AssertionError,
                          self.database.insert_basic_info,
                          **params)
        params = {"number": -20, "abb": "Na"}
        self.assertRaises(AssertionError,
                          self.database.insert_basic_info,
                          **params)
        params = {"number": 12, "abb": ""}
        self.assertRaises(AssertionError,
                          self.database.insert_basic_info,
                          **params)

    def test_basic_params(self):
        """Test if right values can be inserted into basic_params table"""
        params = {"number": 12,
                  "name":   "Sulfur",
                  "grp":  "chalcogen",
                  "weight": 32.06,
                  "period": 16}
        self.database.insert_basic_params(**params)

    def test_basic_params_bad_params(self):
        """Test if AssertionError raises on bad queries to basic_params table"""
        params = {"number": -10,
                  "name":   "Phosphorus",
                  "grp":    "pnictogen",
                  "weight": 30.97,
                  "period": 15}
        self.assertRaises(AssertionError,
                          self.database.insert_basic_params,
                          **params)
        params = {"number": -10,
                  "name":   "Phosphorus",
                  "grp":    "somestuff",
                  "weight": 30.97,
                  "period": 15}
        self.assertRaises(AssertionError,
                          self.database.insert_basic_params,
                          **params)
        params = {"number": -10,
                  "name":   "Phosphorus",
                  "grp":    "pnictogen",
                  "weight": 30.97,
                  "period": -3}
        self.assertRaises(AssertionError,
                          self.database.insert_basic_params,
                          **params)
        params = {"number": -10,
                  "name":   "Phosphorus",
                  "grp":    "pnictogen",
                  "weight": 30.97,
                  "period": 22}
        self.assertRaises(AssertionError,
                          self.database.insert_basic_params,
                          **params)
        params = {"number": -10,
                  "name":   "",
                  "grp":    "pnictogen",
                  "weight": 30.97,
                  "period": 15}
        self.assertRaises(AssertionError,
                          self.database.insert_basic_params,
                          **params)

    def test_congregation(self):
        """Test if right values can be inserted into congregation table"""
        params = {"number":        12,
                  "energy_levels": 5,
                  "metal":         True,
                  "amphoteric":    True,
                  "gas":           False,
                  "semiconductor": False}
        self.database.insert_congregation(**params)

    def test_congregation_bad_params(self):
        """Test if AssertionError raises on bad queries to congregation table"""
        params = {"number":        -1,
                  "energy_levels": 5,
                  "metal":         True,
                  "amphoteric":    True,
                  "gas":           False,
                  "semiconductor": False}
        self.assertRaises(AssertionError,
                          self.database.insert_congregation,
                          **params)
        params = {"number":        12,
                  "energy_levels": 0,
                  "metal":         True,
                  "amphoteric":    True,
                  "gas":           False,
                  "semiconductor": False}
        self.assertRaises(AssertionError,
                          self.database.insert_congregation,
                          **params)
        self.assertRaises(AssertionError,
                          self.database.insert_congregation,
                          **params)
        params = {"number":        12,
                  "energy_levels": 5,
                  "metal":         False,
                  "amphoteric":    True,
                  "gas":           False,
                  "semiconductor": False}
        self.assertRaises(AssertionError,
                          self.database.insert_congregation,
                          **params)

    def test_links(self):
        """Test if right values can be inserted into links table"""
        params = {"number":    12,
                  "wiki_link": "en.wikipedia.org/wiki/Magnesium"}
        self.database.insert_links(**params)

    def test_links_bad_params(self):
        """Test if AssertionError raises on bad queries to links table"""
        args = {"number":    -3,
                "wiki_link": "en.wikipedia.org/wiki/Magnesium"}
        self.assertRaises(AssertionError,
                          self.database.insert_links,
                          **args)
        args = {"number":    12,
                "wiki_link": ""}
        self.assertRaises(AssertionError,
                          self.database.insert_links,
                          **args)
        args = {"number":    0,
                "wiki_link": "en.wikipedia.org/wiki/Magnesium"}
        self.assertRaises(AssertionError,
                          self.database.insert_links,
                          **args)

    def tearDown(self):
        """Close database & drop all tables"""
        self.database.close()
        self.table_creator = DatabaseCreateTable(self.config)
        self.table_creator.drop_all_tables()
        self.table_creator.close()
