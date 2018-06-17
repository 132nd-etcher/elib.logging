# coding=utf-8
import logging
import sys

from elib_logging import settings


def get_formatter(log_format: str) -> logging.Formatter:
    return logging.Formatter(log_format)


def get_console_formatter() -> logging.Formatter:
    if hasattr(sys, 'frozen'):
        return get_formatter(settings.log_format_console())
    return get_file_formatter()


def get_file_formatter() -> logging.Formatter:
    return get_formatter(settings.log_format_file())
