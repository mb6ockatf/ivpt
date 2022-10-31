#!/usr/bin/env python

from os import path, mkdir, sep
from tomli import load, TOMLDecodeError
from src.errors_handler import ErrorHandler


class Configuration(object):
	HOME = path.expanduser("~")
	CONFIG_PATH = HOME + "/.IVPT/config.toml"
	CONFIG = None

	@classmethod
	def touch_config(cls):
		config_path = cls.CONFIG_PATH
		path_items_list = list(config_path.split(sep))[1:]
		for index in range(len(path_items_list)):
			cur_dir = sep + sep.join(path_items_list[0: index])
			if not path.isdir(cur_dir):
				mkdir(cur_dir)
		if not path.isfile(config_path):
			default_config = Configuration.get_default_config("default_config.toml")
			with open(config_path, "w") as input_file:
				input_file.write(default_config)

	@classmethod
	def read_config(cls):
		config_path = cls.CONFIG_PATH
		try:
			with open(config_path, "rb") as file:
				toml_dict = load(file)
				cls.CONFIG = toml_dict
		except TOMLDecodeError as error:
			ErrorHandler.show_exception(error)
		except ValueError as error:
			print("Invalid config file")
			print("Probably, there is a problem with float values")
			print("-" * 100)
			ErrorHandler.show_exception(error)

	@staticmethod
	def get_default_config(config_path: str):
		with open(config_path, "r") as output_file:
			data = output_file.read()
		return data
