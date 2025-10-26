from flashdb.index import Index
from flashdb.storage import Storage, JsonStorage


class FlashDB:

    _default_storage = JsonStorage
    _index_name = dict()
    _default_table_name = "_default"

    def __init__(self, path: str, storage: Storage = None, *args, **kwargs):
        self._storage = (storage or self._default_storage)(path, *args, **kwargs)

    def index(self, name: str) -> Index:
        if name in self._index_name:
            return self._index_name[name]
        self._index_name[name] = Index(name, self._storage)
        return self._index_name[name]


