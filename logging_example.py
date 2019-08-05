#!/usr/bin/env python3
"""Using syslog functionality in Python scripts"""

####---- Logging Configuration ----####
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s"
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "logfile": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "/tmp/test.log",
            "maxBytes": 500000000,  # 500 MB
            "backupCount": 10,
            "formatter": "verbose",
        },
        "console": {
            "level": "CRITICAL",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "__main__": {
            "handlers": ["logfile", "console"],
            "level": "DEBUG",
            "propagate": True,
        }
    },
}
####---- End of Logging Config ----####

# Logging Module with config capabilities
import logging.config

# Create logging instance
logger = logging.getLogger(__name__)

# Load logging configuration
logging.config.dictConfig(LOGGING_CONFIG)

# Send log messages
logger.info("Testing info level message.")
logger.critical("Urgent message! Display in log AND console.")
