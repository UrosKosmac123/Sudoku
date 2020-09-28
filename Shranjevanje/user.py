from uuid import uuid4
from Shranjevanje.file import Filestore

store = Filestore("data-users.json")


class User:

    def __init__(self, id: str, name: str = None):
        self.id = id
        self.name = name

    def ensure(id: str = None, name: str = None):
        """Zagotovi, da uporabnik obstaja v datoteki."""
        id = id or uuid4().hex
        updated = {}
        if name is None:
            updated = store.update({id: {}})
        else:
            updated = store.update({id: {"name": name}})
        return User(id, **updated[id])

    def find_by_id(id: str):
        """Najde uporabnika po ID-ju. Vrne None, če uporabnik ne obstaja."""
        data = store.read()
        if username in data:
            return User(**data[username])
        else:
            return None

    def find_all():
        """Vrne seznam vseh uporabnikov."""
        data = store.read().items()
        return [User(id=id, **value) for id, value in data]
