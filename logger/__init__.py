import logging
import os
import yaml

from logging.config import dictConfig
from pathlib import Path

BASE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "configs")


def get_config(config_name):
    return os.path.join(BASE_DIR, config_name)


def start(name=None, log_dir=None, config=None):
    if not name:
        name = "oscil"

    if log_dir and not isinstance(log_dir, str):
        try:
            log_dir = log_dir._str
        except AttributeError:
            log_dir = str(log_dir)

    config_path = os.path.join(BASE_DIR, "default.yml")
    if config:
        config_path = config

    try:
        with open(config_path, "r") as f2:
            default_config = yaml.safe_load(f2)
    except FileNotFoundError:
        raise

    for handler, configs in default_config["handlers"].items():
        file_name = configs.get("filename")
        if not file_name:
            continue

        if "{name}" in file_name and name:
            log_file = file_name.format(**locals())
            if log_dir:
                log_file = os.path.join(log_dir, log_file)
                make_dir(log_file)
            configs.update({"filename": log_file})
        elif file_name:
            log_file = file_name
            if log_dir:
                log_file = os.path.join(log_dir, log_file)
                make_dir(log_file)
            configs.update({"filename": log_file})
        else:
            raise NotImplementedError

    dictConfig(default_config)
    _tool = logging.getLogger("tool")
    _verbose = logging.getLogger("verbose")
    _scope = logging.getLogger("scope")

    _tool.info("************* Tool Logging Started *************")
    _scope.info("************* Scope Logging Started *************")
    _verbose.info("************* Command Logging Started *************")


def make_dir(filepath):
    path = Path(filepath)
    try:
        path.parent.mkdir(parents=True)
    except FileExistsError as err:
        pass
