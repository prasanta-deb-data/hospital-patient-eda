import logging
import os
from src.config_loader import load_config

config = load_config()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, config["paths"]["logs"])
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, config["logging"]["file_name"])

logging.basicConfig(
    filename=LOG_FILE,
    level=config["logging"]["level"],
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)
