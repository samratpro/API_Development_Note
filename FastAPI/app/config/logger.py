# app_utils.py
import logging
import os
from logging.handlers import RotatingFileHandler

from app.config.config import Config


class LevelFilter(logging.Filter):
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def filter(self, record):
        return self.low <= record.levelno <= self.high


def setup_logger(name: str, info_log_file: str, error_log_file: str) -> None:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Set to DEBUG to capture all levels

    if not os.path.exists(os.path.dirname(info_log_file)):
        os.makedirs(os.path.dirname(info_log_file))

    # Create handlers
    info_handler = RotatingFileHandler(
        info_log_file, maxBytes=1 * 1024 * 1024, backupCount=5
    )
    error_handler = RotatingFileHandler(
        error_log_file, maxBytes=1 * 1024 * 1024, backupCount=5
    )

    # Set levels
    info_handler.setLevel(logging.DEBUG)
    error_handler.setLevel(logging.DEBUG)

    # Create formatters and add it to handlers
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    info_handler.setFormatter(formatter)
    error_handler.setFormatter(formatter)

    # Attach filters
    info_handler.addFilter(LevelFilter(logging.INFO, logging.WARNING))
    error_handler.addFilter(LevelFilter(logging.ERROR, logging.CRITICAL))

    # Add handlers to the logger
    logger.addHandler(info_handler)
    logger.addHandler(error_handler)

    return logger


log_files = Config.load_toml_config()["logfiles"]

celery_logger = setup_logger(
    "celery", log_files["celery_info_log"], log_files["celery_error_log"]
)

main_logger = setup_logger(
    "main", log_files["main_info_log"], log_files["main_error_log"]
)

utils_logger = setup_logger(
    "utils", log_files["utils_info_log"], log_files["utils_error_log"]
)

redis_logger = setup_logger(
    "redis", log_files["redis_info_log"], log_files["redis_error_log"]
)

chart_logger = setup_logger(
    "chart", log_files["chart_info_log"], log_files["chart_error_log"]
)

process_logger = setup_logger(
    "process", log_files["process_info_log"], log_files["process_error_log"]
)
