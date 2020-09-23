from bottle import get, post, run, template
from core import State

@get("/")
def get():
    return template("index")

@post("/")
def post():
    s = State()

    return template("index", state=s)

run(reloader=True, debug=True, host="localhost", port="8081")