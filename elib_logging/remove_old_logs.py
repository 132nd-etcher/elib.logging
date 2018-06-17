# coding=utf-8
from pathlib import Path

from elib_logging import settings


def remove_old_log_files(log_file_path: str):
    log_file = Path(log_file_path).absolute()
    folder = log_file.parent

    old_logs = sorted(
        [
            x for x in folder.iterdir()
            if x.name.startswith(f'{log_file.stem}.log-')
        ]
    )[:-(int(settings.back_count()) - 1)]

    for path in old_logs:
        path.unlink()
