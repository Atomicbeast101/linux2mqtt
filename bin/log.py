# Imports
import logging.handlers
import logging
import config
import sys
import os

# Attributes
logger = logging.getLogger(config.APP_NAME)
logger.setLevel(config.LOG_LEVEL)
console_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.handlers.TimedRotatingFileHandler(
    filename=os.path.join(config.LOG_PATH, 'app.log'),
    when='midnight',
    interval=1,
    backupCount=config.LOG_RETENTION_DAYS,
    encoding='utf-8',
    utc=False,
)
formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.addHandler(file_handler)
