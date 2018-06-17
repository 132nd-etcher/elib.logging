# coding=utf-8
from pathlib import Path

import elib_logging.remove_old_logs
import elib_logging.settings


def test_remove_old_files():
    Path(f'{elib_logging.settings.log_file_name()}.log').touch()
    for i in range(20):
        Path(f'{elib_logging.settings.log_file_name()}.log-{str(i).zfill(3)}').touch()
    assert len(list(Path('.').iterdir())) == 21
    elib_logging.remove_old_logs.remove_old_log_files(f'{elib_logging.settings.log_file_name()}.log')
    assert len(list(Path('.').iterdir())) == 7


def test_remove_old_files_preserve_other_files():
    Path(f'{elib_logging.settings.log_file_name()}.log').touch()
    for i in range(20):
        Path(f'other file-{i}.log').touch()
    assert len(list(Path('.').iterdir())) == 21
    elib_logging.remove_old_logs.remove_old_log_files(f'{elib_logging.settings.log_file_name()}.log')
    assert len(list(Path('.').iterdir())) == 21
