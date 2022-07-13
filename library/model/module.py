import pickle
from pathlib import Path
from typing import Literal

from pydantic import BaseModel

from library.model.config import config


class Module(BaseModel):
    """
    Module.
    """

    name: str = "Unknown"
    pack: str
    version: str = "Unknown"
    author: list[str] = ["Unknown"]
    pypi: bool = False
    category: Literal[
        "utility", "entertainment", "dependency", "miscellaneous"
    ] = "miscellaneous"
    description: str = ""
    dependency: list[str] = None
    loaded: bool = True
    override_default: None | bool = None
    override_switch: None | bool = None

    def __hash__(self):
        return hash(self.name)


class Modules:
    __modules: list[Module] = []
    __pickle_path: Path = Path(config.data_path.generic, "modules.pickle")

    def __init__(self):
        self.load()

    def save(self):
        with self.__pickle_path.open("wb") as f:
            pickle.dump(self.__modules, f)

    def load(self):
        pass

    def load_from_directory(self):
        pass

    def load_from_pickle(self):
        if self.__pickle_path.exists():
            with self.__pickle_path.open("rb") as f:
                self.__modules = pickle.load(f)
            return
        self.__modules = []
        self.save()

    def get(self, name: str):
        return next((module for module in self.__modules if module.name == name), None)
