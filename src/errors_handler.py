#!/usr/bin/env python3ErrorHandler
"""Pretty exception stuff"""
from sys import exc_info
from traceback import format_exception
from logging import error


def show_exception(exception_object):
	"""Print pretty exception"""
	exc_type, exc_value, exc_tb = exc_info()
	pretty_exception = format_exception(exc_type, exc_value, exc_tb)
	error(pretty_exception)
	error_string = " ".join(list(map(str, exception_object.args)))
	print("Error:", error_string)
	print("Exception class:", exception_object.__class__)
	print("Traceback:", "\n", "\n".join(pretty_exception))
