# coding=utf-8
import logging as base_logging

import elib_logging.logger


def test_basics():
    logger = elib_logging.logger.get_main_logger()
    assert isinstance(logger, base_logging.Logger)


def test_identity():
    assert elib_logging.logger.get_main_logger() is elib_logging.logger.get_main_logger()
