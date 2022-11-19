"""Configuration function"""
import os
from tomli import load, TOMLDecodeError
from .errors_handler import show_exception


def configuration() -> dict:
    """Touch & read config file"""
    home = os.path.expanduser("~")
    config_path = [".IVPT", "config.toml"]
    config_path = home + os.sep + os.sep.join(config_path)
    config = None
    default_config = ["src", "essential", "default_config.toml"]
    default_config = os.sep.join(default_config)
    path_items_list = list(config_path.split(os.sep))[1:]
    for index in range(len(path_items_list)):
    	cur_dir = os.sep + os.sep.join(path_items_list[0: index])
    	if not os.path.isdir(cur_dir):
    		os.mkdir(cur_dir)
    if not os.path.isfile(config_path):
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
    	show_exception(error)
    keys = ["db", "log", "accuracy"]
    for j in keys:
        if j not in config:
            raise KeyError("key does not exist in config file")
    return config

