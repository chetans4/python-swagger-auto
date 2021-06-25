from flask import jsonify
from pyms.flask.app import Microservice


ms = Microservice(path=__file__)
app = ms.create_app()


@app.route("/")
def example():
    return jsonify({"main": "hello world"})


@app.route("/one")
def one():
    return jsonify({"main": "one world"})


if __name__ == "__main__":
    app.run()
