#!/usr/bin/python3
from os import path, mkdir, sep
from logging import basicConfig, DEBUG


def setup_logging(log_name: str):
	home = path.expanduser("~")
	log_path = home + log_name
	path_items_list = list(log_path.split(sep))[1:]
	for index in range(len(path_items_list)):
		cur_dir = sep + sep.join(path_items_list[0: index])
		if not path.isdir(cur_dir):
			mkdir(cur_dir)
	if not path.isfile(log_path):
		with open(log_path, "w", encoding="utf-8"):
			...
	basicConfig(filename=log_path, level=DEBUG, format="%(asctime)s %(message)s")
