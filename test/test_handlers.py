# coding=utf-8
import logging as base_logging
import sys

import elib_logging.handlers
import elib_logging.logger


def test_handlers():
    logger = elib_logging.logger.get_main_logger()
    assert len(logger.handlers) == 2
    for handler in logger.handlers:
        assert (isinstance(handler, base_logging.FileHandler) or isinstance(handler, base_logging.StreamHandler))


def test_get_handlers_with_formatter():
    formatter = base_logging.Formatter()
    handler = elib_logging.handlers.get_console_handler(formatter)
    assert isinstance(handler, base_logging.StreamHandler)
    handler = elib_logging.handlers.get_file_handler('test.log', formatter)
    assert isinstance(handler, base_logging.FileHandler)


def test_queued_handler(logging_queue):
    assert logging_queue.empty()
    logger = elib_logging.logger.get_subprocess_logger(logging_queue, 'test_queued_handler')
    assert logging_queue.empty()
    logger.debug('test')
    assert not logging_queue.empty()
    element = logging_queue.get()
    assert isinstance(element, base_logging.LogRecord)
    assert 'test' == element.msg


def test_frozen():
    setattr(sys, 'frozen', True)
    try:
        logger = elib_logging.logger.get_logger()
        for handler in logger.handlers:
            if not isinstance(handler, base_logging.FileHandler):
                assert handler.level == base_logging.INFO
    finally:
        delattr(sys, 'frozen')


def test_handler_level_not_frozen():
    logger = elib_logging.logger.get_logger()
    for handler in logger.handlers:
        if not isinstance(handler, base_logging.FileHandler):
            assert handler.level == base_logging.DEBUG
