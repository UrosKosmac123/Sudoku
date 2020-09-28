from json import loads, dumps
from os import path

def deepUpdateDict(data: dict, update: dict):
    for k, v in update.items():
        d = data.get(k, {})
        if isinstance(d, dict) and isinstance(v, dict):
            data[k] = deepUpdateDict(d, v)
        else:
            data[k] = v
    return data

class Filestore:
    """Razred za shranjevanje podatkov v JSON datoteko."""

    def __init__(self, filename: str, default: dict = {}):
        """Ustvari datoteko, če ne obstaja."""
        self.filename = filename
        if not path.exists(self.filename):
            serialized = dumps(default)
            with open(self.filename, "w") as file:
                file.write(serialized)

    def read(self) -> dict:
        """Prebere datoteko."""
        with open(self.filename, "r") as file:
            raw = file.read()
            json = loads(raw)
            file.close()
            return json

    def update(self, update: dict) -> dict:
        """Posodobi datoteko in vrne posodobljeno vrednost."""
        with open(self.filename, "r+") as file:
            raw = file.read()
            json = loads(raw)

            updated = deepUpdateDict(json, update)
            serialized = dumps(updated)

            file.seek(0)
            file.write(serialized)
            file.truncate()

            return updated