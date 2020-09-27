from bottle import route, request, response, run, template, redirect
from argparse import ArgumentParser
from data.user import User
from data.game import Game
from model import State
import json

def get_user_from_cookie(req, res) -> User:
    id = req.get_cookie("SESSION")
    user = User.ensure(id)
    response.set_cookie("SESSION", user.id)
    return user

@route("/", method="GET")
def index_get():
    """Vstopna stran."""
    user = get_user_from_cookie(request, response)
    games = [g for g in Game.find_by_user(user.id) if not g.state.solved()] if user else []
    return template("index.tpl", user=user, games=games)

@route("/", method="POST")
def index_post():
    """Obrazec na vstopni strani, ki določi ime."""
    user = get_user_from_cookie(request, response)
    name = request.forms.get("name")
    User.ensure(user.id, name)
    return redirect("/")

@route("/igre", method="POST")
def games_post():
    """Ustvari novo igro."""
    user = get_user_from_cookie(request, response)
    if user.name is None:
        return redirect("/")
    state = State(True)
    game = Game.create(user.id, state)
    return redirect("/igre/{}".format(game.id))

@route("/igre/<id>", method="GET")
def game_get(id: str):
    """Posamezna igra."""
    user = get_user_from_cookie(request, response)
    if user.name is None:
        return redirect("/")
    game = Game.find_by_id(id)
    return template("game.tpl", user=user, game=game)

@route("/igre/<id>", method="POST")
def game_get(id: str):
    """Posodobi stanje igre."""
    user = get_user_from_cookie(request, response)
    if user.name is None:
        return redirect("/")

    def parse_coordinates(coor: str):
        x, y = (int(c) for c in coor.split(","))
        return (x, y)

    game = Game.find_by_id(id)
    state = game.state
    
    values = [(*parse_coordinates(coor), int(value)) for coor, value in request.forms.items() if value]
    errors = [[None for y in range(9)] for x in range(9)]
    for x, y, value in values:
        if value == state.matrix[x][y]:
            continue
        try:
            state = state.mutate(x, y, value)
        except Exception as error:
            errors[x][y] = (value, error)
    game.update(state)

    return template("game.tpl", user=user, game=game, errors=errors)

if __name__ == "__main__":
    parser = ArgumentParser(description="Sudoku spletni vmesnik.")
    parser.add_argument("--host", type=str, help="IP, na katerem posluša vmesnik.", default="localhost")
    parser.add_argument("--port", type=int, help="TCP port, na katerem posluša vmesnik.", default=8080)
    parser.add_argument("--debug", type=bool, help="Razvojni način.", default=False)

    args = parser.parse_args()

    run(
        host=args.host,
        port=args.port,
        debug=args.debug,
        reloader=args.debug
    )