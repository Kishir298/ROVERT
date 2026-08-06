"""
ROVERT Logger
=============
Central logging system for the laptop software.
"""

import logging
import os
from datetime import datetime


# Create logs folder if it does not exist
LOG_FOLDER = "logs"

os.makedirs(LOG_FOLDER, exist_ok=True)


# Log filename
log_file = os.path.join(
    LOG_FOLDER,
    f"rovert_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
)


# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)


logger = logging.getLogger("ROVERT")