import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = 'logs'
LOG_FILE = 'app.log'

logger = logging.getLogger('my_app_logger')
logger.setLevel(logging.DEBUG)

log_path = os.path.join(LOG_DIR, LOG_FILE)

handler = RotatingFileHandler(log_path, maxBytes=1024*1024, backupCount=1)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
