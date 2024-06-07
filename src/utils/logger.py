import sys
import os
from loguru import logger as log


"""
This module sets up a logger using the `loguru` library.

The logger is configured to log to `sys.stdout` with a custom format.
The log level is set to "INFO" by default.

The custom format includes the time, log level, and the log message.
The log level is displayed in different colors depending on its severity.

"""
log_level = os.getenv("LOG_LEVEL") or "INFO"
log.remove()
log.add(
    sys.stdout,
    format="[{time:HH:mm:ss}] {level} <lvl>{message}</lvl>",
    level=log_level,
    colorize=True)
