from uuid import uuid4
from data.file import Filestore
from state import State

store = Filestore("data-games.json")

class Game:

    def __init__(self, id: str, user: str, state: dict):
        self.id = id
        self.user = user
        if isinstance(state, State):
            self.state = state
        else:
            self.state = State()
            self.state.matrix = state["matrix"]
            self.state.locked = state["locked"]

    def find_by_id(id: str):
        """Najde igro po IDju. Vrne None, če igra ne obstaja."""
        data = store.read()
        if id in data:
            return Game(id=id, **data[id])
        else:
            return None

    def find_by_user(user: str):
        """Najde vse igre, ki pripadajo uporabniku."""
        data = store.read().items()
        return [Game(id=id, **value) for id,value in data if value["user"] == user]

    def find_all():
        """Vrne seznam vseh iger."""
        data = store.read().items()
        return [Game(id=id, **value) for id,value in data]

    def create(user: str, state: dict):
        """Ustvari novo igro."""
        id = uuid4().hex
        store.update({
            id: { "user": user, "state": vars(state) }
        })
        return Game(id, user, state)

    def update(self, state: dict):
        """Posodobi stanje igre."""
        store.update({
            self.id: { "state": vars(state) }
        })
        if isinstance(state, State):
            self.state = state
        else:
            self.state = State()
            self.state.matrix = state["matrix"]
            self.state.locked = state["locked"]

    def delete(self, id: str):
        store.update({
            self.id: None
        })

