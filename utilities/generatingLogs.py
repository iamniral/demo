import logging

import logging
import os

# Ensure the 'Logs' directory exists relative to the script location
# Note: The relative path in the image (..\Logs\\logfile.log) suggests
# the log file is one directory up, then in a 'Logs' folder.
LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'Logs', 'logfile.log')
# You may need to create the directory structure before calling basicConfig
os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)


def log():
    """Configures the root logger and returns the logger instance."""

    # logging.basicConfig automatically configures the root logger based on the parameters
    logging.basicConfig(
        filename=LOG_FILE_PATH,
        format='%(asctime)s: %(levelname)s: %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',  # Note: The image uses a non-standard date format
        level=logging.INFO
    )

    # logging.getLogger() without an argument returns the root logger
    logger = logging.getLogger()
    return logger


# --- Execution ---

logger = log()
logger.info("This is a new log")
logger.error("This is an error message")