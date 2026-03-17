import logging
import os
import uuid

from datetime import datetime

logger = logging.getLogger(__name__)

def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def generate_uuid():
    return str(uuid.uuid4())

def get_current_timestamp():
    return int(datetime.now().timestamp())

def get_config_value(config, key):
    try:
        return config[key]
    except KeyError:
        logger.error(f"Config key '{key}' not found")
        return None

def get_project_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_project_name():
    return os.path.basename(get_project_root())

def get_current_branch():
    try:
        return os.environ['GITHUB_BRANCH']
    except KeyError:
        logger.error("GITHUB_BRANCH environment variable not found")
        return None