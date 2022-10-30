#!/usr/bin/env python

from os import path, mkdir
from tomli import load, TOMLDecodeError
from errors_handler import ErrorHandler


class Configuration(object):
	HOME = path.expanduser("~")
	CONFIG_DIR = HOME + "./IVPT"
	CONFIG_FILE = HOME + CONFIG_DIR + "/config.toml"
	CONFIG = None

	@classmethod
	def touch_config(cls):
		try:
			if not path.isdir(cls.CONFIG_DIR):
				mkdir(cls.CONFIG_DIR)
			if not path.isfile(cls.CONFIG_FILE):
				open(cls.CONFIG_FILE, 'w').close()
		except Exception as error:
			ErrorHandler.show_exception(error)

	@classmethod
	def read_config(cls):
		try:
			file = open(cls.CONFIG_FILE, "rb")
			toml_dict = load(file)
			cls.CONFIG = toml_dict
			file.close()
		except TOMLDecodeError as error:
			ErrorHandler.show_exception(error)
		except ValueError as error:
			print("Invalid config file")
			print("Probably, there is a problem with float values")
			print("-" * 100)
			ErrorHandler.show_exception(error)


"""if __name__ == "__main__":
	stuff = ConfigurationStorage()"""
