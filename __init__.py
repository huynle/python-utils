"""
Owner: Huy Le
Description: Custom package for the everyday use. Will try to minimize usage of other packages

"""
import os
from pathlib import Path

ROOT_DIR = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class Tools(object):
    @staticmethod
    def TEMP_DIR():
        temp_dir = ROOT_DIR.joinpath("temp")
        temp_dir.mkdir(parents=True, exist_ok=True)
        return temp_dir
