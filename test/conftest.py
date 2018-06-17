# coding=utf-8
"""
Pytest config file
"""
import multiprocessing
import os
import random
import sys

import pytest
from mockito import unstub

import elib_logging
from elib_logging import configure


def pytest_configure(config):
    print('pytest args: ', config.args)
    setattr(sys, '_called_from_test', True)


def pytest_unconfigure(config):
    print('pytest args: ', config.args)
    delattr(sys, '_called_from_test')


@pytest.fixture(autouse=True)
def cleandir(request, tmpdir):
    if 'nocleandir' in request.keywords:
        yield
    else:
        current_dir = os.getcwd()
        os.chdir(str(tmpdir))
        yield os.getcwd()
        os.chdir(current_dir)


@pytest.fixture(autouse=True)
def unstub_mockito():
    unstub()
    yield
    unstub()


def pytest_addoption(parser):
    parser.addoption("--long", action="store_true",
                     help="run long tests")


def pytest_runtest_setup(item):
    # Skip tests that are marked with the "long" marker
    long_marker = item.get_marker("long")
    if long_marker is not None and not item.config.getoption('long'):
        pytest.skip('skipping long tests')


@pytest.fixture(name='logging_queue')
def _get_logging_queue():
    logging_queue = multiprocessing.Queue()
    yield logging_queue


@pytest.fixture(autouse=True)
def random_logger():
    # environ = os.environ
    # noinspection SpellCheckingInspection
    rand = ''.join(random.sample('abcdefghijkl', 6))
    elib_logging.setup_logging(rand)
    configure.check_settings()

    print(os.environ)
    yield
    # os.environ = environ
