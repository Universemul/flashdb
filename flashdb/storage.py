import json
import os.path
from abc import ABC
from typing import Dict, Any

from flashdb.file_helper import create_file


class Storage(ABC):

    def write(self, data: Dict[str, Dict[str, Any]]):
        raise NotImplementedError

    def read(self):
        raise NotImplementedError


class JsonStorage(Storage):

    def __init__(self, path: str, access_mode="r+", encoding="utf-8"):
        if not os.path.exists(path):
            create_file(path)
        self._path = path
        self._encoding = encoding
        self._file = open(path, mode=access_mode, encoding=encoding)

    def write(self, data: Dict[str, Dict[str, Any]]):
        self._file.seek(0)
        _data = json.dumps(data)
        try:
            self._file.write(_data)
        except Exception as e:
            raise IOError("Something went wrong when write in the database")
        self._file.flush()

    def read(self) -> Dict:
        if self._is_file_empty():
            return {}
        self._file.seek(0)
        return json.load(self._file)

    def _is_file_empty(self) -> bool:
        return os.stat(self._path).st_size == 0
