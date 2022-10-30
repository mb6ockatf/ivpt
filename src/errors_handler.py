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
		print('Error: %s' % (' '.join(exception_object.args)))
		print("Exception class: ", exception_object.__class__)
		print('Traceback:', "\n", pretty_exception)


if __name__ == "__main__":
	stuff = ErrorHandler()
