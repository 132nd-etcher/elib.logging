# coding=utf-8
import logging
import sys

from elib_logging.formatter import get_console_formatter, get_file_formatter


def get_file_handler(log_file_path: str, formatter: logging.Formatter = None) -> logging.Handler:
    if formatter is None:
        formatter = get_file_formatter()
    handler = logging.FileHandler(filename=log_file_path, mode='w', encoding='utf8')
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    return handler


def get_console_handler(formatter: logging.Formatter = None) -> logging.Handler:
    if formatter is None:
        formatter = get_console_formatter()
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    return handler
