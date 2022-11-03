#!/usr/bin/env python3
"""Configuration class"""
from os import path, mkdir, sep
from tomli import load, TOMLDecodeError
from src.errors_handler import show_exception


class Configuration:
    """Work with IVPT configuration file"""
    home = path.expanduser("~")
    config_path = home + "/.IVPT/config.toml"
    config = None
    default_config = "src/default_config.toml"

    @classmethod
    def touch_config(cls):
        """Make config file if it does not exist"""
        path_items_list = list(cls.config_path.split(sep))[1:]
        for index in range(len(path_items_list)):
            cur_dir = sep + sep.join(path_items_list[0: index])
            if not path.isdir(cur_dir):
                mkdir(cur_dir)
        if not path.isfile(cls.config_path):
            contents = Configuration.get_default_config(cls.default_config)
            with open(cls.config_path, "w", encoding="utf-8") as input_file:
                input_file.write(contents)

    @classmethod
    def read_config(cls):
        """Read config's contents"""
        try:
            with open(cls.config_path, "rb") as file:
                toml_dict = load(file)
                cls.config = toml_dict
        except TOMLDecodeError as error:
            show_exception(error)
        except ValueError as error:
            print("Invalid config file")
            print("Probably, there is a problem with float values")
            print("-" * 100)
            show_exception(error)

    @staticmethod
    def get_default_config(config_path: str):
        """Get default config's contents"""
        with open(config_path, "r", encoding="utf-8") as output_file:
            data = output_file.read()
        return data
