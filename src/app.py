from blueprints.docs import docs_blueprint
from blueprints.error_handler import error_handler_blueprint
from blueprints.git_update import git_update_blueprint
from blueprints.words import words_blueprint
from flask import Flask, jsonify
from flask_restful import Api
from flask_swagger import swagger

app = Flask(__name__)
api = Api(app)

app.register_blueprint(git_update_blueprint)
app.register_blueprint(words_blueprint)
app.register_blueprint(docs_blueprint)
app.register_blueprint(error_handler_blueprint)


@app.route("/api/spec")
def spec():
    swag = swagger(app)
    swag["info"]["version"] = "1.0"
    swag["info"]["title"] = "words API "
    return jsonify(swag)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
