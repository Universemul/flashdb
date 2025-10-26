from typing import Dict

from flashdb.storage import Storage


class Index:

    _id = 0

    def __init__(self, name: str, storage: Storage, *args, **kwargs):
        self._name = name
        self._storage = storage

    def insert(self, data: Dict):
        new_id = self._id
        indexes = self._storage.read()
        if self._name not in indexes:
            indexes[self._name] = {}
        indexes[self._name][new_id] = data
        self._storage.write(indexes)
        self._id += 1 #get the latest id always
        return new_id

    def get_all(self):
        return self._storage.read()

    def find(self):
        pass
