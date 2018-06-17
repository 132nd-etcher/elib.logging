# coding=utf-8
import logging as base_logging
import multiprocessing
import sys
from concurrent import futures
from pathlib import Path

import pytest
from mockito import mock, verifyStubbedInvocationsAreUsed, when

import elib_logging.exc
import elib_logging.logger
import elib_logging.settings


def dummy(logging_queue, msg: str):
    logger = elib_logging.logger.get_logger(logging_queue)
    logger.debug(msg)


def test_sub_process_logger(logging_queue):
    logger = elib_logging.logger.get_subprocess_logger(logging_queue, 'test_sub_process_logger')
    assert elib_logging.settings.logger_name() + '.subprocess.test_sub_process_logger' == logger.name


def test_subprocess_logger_identity(logging_queue):
    logger = elib_logging.logger.get_subprocess_logger(logging_queue, 'test_subprocess_logger_identity')
    assert logger is elib_logging.logger.get_subprocess_logger(logging_queue, 'test_subprocess_logger_identity')


def test_missing_queue():
    not_the_main_process = mock()
    not_the_main_process.name = 'not_the_main_process'
    when(multiprocessing).current_process().thenReturn(not_the_main_process)
    with pytest.raises(elib_logging.exc.MissingQueueError):
        elib_logging.get_logger()
    verifyStubbedInvocationsAreUsed()


def test_subprocess(logging_queue):
    assert logging_queue.empty()
    process = multiprocessing.Process(target=dummy, args=(logging_queue, 'test message'), name='test_subprocess')
    process.start()
    process.join()
    assert not logging_queue.empty()
    msg = logging_queue.get()
    assert isinstance(msg, base_logging.LogRecord)
    assert 'test message' == msg.msg
    assert f'{elib_logging.settings.logger_name()}.subprocess.test_subprocess' == msg.name
    assert 'DEBUG' == msg.levelname
    assert 'dummy' == msg.funcName
    log_dir = Path(elib_logging.settings.log_dir())
    assert log_dir.exists()
    assert 1 == len(list(log_dir.iterdir()))
    log_file = Path(log_dir.joinpath(f'{elib_logging.settings.logger_name()}.subprocess.test_subprocess.log'))
    assert log_file.exists()
    assert 'test message' in log_file.read_text()
