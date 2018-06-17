# coding=utf-8

import logging as base_logging
import threading
from pathlib import Path

import elib_logging
import elib_logging.logger
import elib_logging.settings


def dummy(message: str):
    logger = elib_logging.get_logger()
    logger.info(message)


def test_thread_sub_logger():
    logger = elib_logging.logger.get_thread_logger('thread_name')
    assert isinstance(logger, base_logging.Logger)
    assert f'{elib_logging.settings.logger_name()}.thread.thread_name' == logger.name
    assert 10 == logger.level
    assert 1 == len(logger.handlers)
    assert isinstance(logger.handlers[0], base_logging.FileHandler)


def test_thread_sub_logger_identity():
    logger = elib_logging.logger.get_thread_logger('thread_name')
    assert logger is elib_logging.logger.get_thread_logger('thread_name')


def test_thread(caplog):
    thread = threading.Thread(target=dummy, args=('test message',), name='test_thread')
    thread.start()
    thread.join()
    assert 'test message' in caplog.text
    log_dir = Path(elib_logging.settings.log_dir())
    assert log_dir.exists()
    assert 1 == len(list(log_dir.iterdir()))
    log_file = Path(log_dir.joinpath(f'{elib_logging.settings.logger_name()}.thread.test_thread.log'))
    assert log_file.exists()
    assert 'test message' in log_file.read_text()
    assert f'{elib_logging.settings.logger_name()}.thread.test_thread' in log_file.read_text()
