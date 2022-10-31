#!/usr/bin/env python

from sys import exc_info
from traceback import format_exception
from logging import error


class ErrorHandler(object):
	@staticmethod
	def show_exception(exception_object):
		exc_type, exc_value, exc_tb = exc_info()
		pretty_exception = format_exception(exc_type, exc_value, exc_tb)
		error(pretty_exception)
		error_string = " ".join(list(map(str, exception_object.args)))
		print("Error:", error_string)
		print("Exception class:", exception_object.__class__)
		print("Traceback:", "\n", "\n".join(pretty_exception))
