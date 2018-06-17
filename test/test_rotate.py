# coding=utf-8
from pathlib import Path

import elib_logging.logger
import elib_logging.rotate_logs


def test_rotate_log_file():
    assert not list(Path('.').iterdir())
    log_file = Path('{elib_logging.settings.SETTINGS.log_file_name}.log').absolute()
    log_file.touch()
    elib_logging.rotate_logs.rotate_logs(str(log_file))
    logger = elib_logging.logger.get_main_logger()
    logger.debug('test')
    assert 2 == len(list(Path('.').iterdir()))
