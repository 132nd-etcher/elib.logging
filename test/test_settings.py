# coding=utf-8

import os
import sys

import pytest

import elib_logging.configure
import elib_logging.exc
import elib_logging.settings


def test_get_value_raise():
    with pytest.raises(elib_logging.exc.LoggerNotSetupError):
        elib_logging.settings._get_value('test')


def test_get_value():
    val_name = 'test_val_name'
    val_name_sys = f'{sys.executable}{val_name}'
    val_value = 'test_val_value'
    os.environ[val_name_sys] = val_value
    assert val_value == elib_logging.settings._get_value(val_name)


def test_check_settings_ok():
    elib_logging.configure.check_settings()


@pytest.mark.parametrize(
    'value',
    [
        f'{sys.executable}ELIB_LOGGING_LOGGER_NAME',
        f'{sys.executable}ELIB_LOGGING_LOG_FILE_NAME',
        f'{sys.executable}ELIB_LOGGING_LOG_DIR',
        f'{sys.executable}ELIB_LOGGING_LOG_FORMAT_CONSOLE',
        f'{sys.executable}ELIB_LOGGING_LOG_FORMAT_FILE',
        f'{sys.executable}ELIB_LOGGING_BACKUP_COUNT',
    ])
def test_check_settings_nok(value):
    del os.environ[value]
    with pytest.raises(elib_logging.exc.LoggerNotSetupError):
        elib_logging.configure.check_settings()
