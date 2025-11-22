import logging
from pathlib import Path

LOG_DIR = Path("../logs")
LOG_DIR.mkdir(exist_ok=True)

def get_logger(name: str):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler(LOG_DIR / "provisioning.log")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger
