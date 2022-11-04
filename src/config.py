#!/usr/bin/env python3
"""Configuration function"""
from os import path, mkdir, sep
from tomli import load, TOMLDecodeError
from errors_handler import show_exception


def configuration() -> dict:
    """Touch & read config file"""
    home = path.expanduser("~")
    config_path = home + "/.IVPT/config.toml"
    config = None
    default_config = "src/default_config.toml"
    path_items_list = list(config_path.split(sep))[1:]
    for index in range(len(path_items_list)):
        cur_dir = sep + sep.join(path_items_list[0: index])
        if not path.isdir(cur_dir):
            mkdir(cur_dir)
    if not path.isfile(config_path):
        with open(default_config, "r", encoding="utf-8") as output_file:
            contents = output_file.read()
        with open(config_path, "w", encoding="utf-8") as input_file:
            input_file.write(contents)
    try:
        with open(config_path, "rb") as file:
            toml_dict = load(file)
            config = toml_dict
    except TOMLDecodeError as error:
        show_exception(error)
    except ValueError as error:
        print("Invalid config file")
        print("Probably, there is a problem with float values")
        print("-" * 100)
        show_exception(error)
    return config
