# coding=utf-8


class ELIBLoggingError(Exception):
    """Base elib_logging exception"""


class MissingQueueError(ELIBLoggingError):
    """Raised when trying to instantiate a logger from a subprocess without a valid queue"""


class LoggerNotSetupError(ELIBLoggingError):
    """Raised when the logging system hasn't been set up yet"""
