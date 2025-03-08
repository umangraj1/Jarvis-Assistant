# config/settings.py
from pathlib import Path

import yaml

CONFIG_PATH = Path(__file__).parent / "settings.yaml"

def load_settings():
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)

settings = load_settings()