import git
from flask import Flask, jsonify, make_response, render_template, request
from flask_expects_json import expects_json
from flask_restful import Api, Resource
from flask_swagger import swagger
from jsonschema import ValidationError

from src.schema import SORT_SCHEMA, VOWEL_COUNT_SCHEMA

app = Flask(__name__)
api = Api(app)


@app.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        original_error = error.description
        return make_response(jsonify({"error": original_error.message}), 400)
    return error


@api.resource("/git_update")
class GitUpdateResource(Resource):
    def post(self):
        """
        Update Git Repository

        Update the local Git repository by pulling changes from the remote origin.

        ---
        responses:
            200:
                description: Success
        """
        repo = git.Repo("./python-challenge")
        origin = repo.remotes.origin
        repo.create_head("main", origin.refs.main).set_tracking_branch(
            origin.refs.main
        ).checkout()
        origin.pull()
        return "", 200


@api.resource("/api/vowel_count")
class VowelCountResource(Resource):
    @expects_json(VOWEL_COUNT_SCHEMA)
    def post(self):
        """
        Count Vowels

        Count the number of vowels in the provided list of words.

        ---
        consumes:
          - application/json
        parameters:
          - in: body
            name: data
            required: true
            schema:
              type: object
              properties:
                words:
                  type: array
                  items:
                    type: string
        responses:
          200:
            description: Success
          400:
            description: Bad Request
        """
        data = request.get_json()
        result = {}
        for word in data["words"]:
            vowel_count = sum(1 for char in word.lower() if char in "aeiou")
            result[word] = vowel_count

        return jsonify(result)


@api.resource("/api/sort")
class SortResource(Resource):
    @expects_json(SORT_SCHEMA)
    def post(self):
        """
        Sort Words

        Sort the provided list of words in ascending or descending order.

        ---
        consumes:
          - application/json
        parameters:
          - in: body
            name: data
            required: true
            schema:
              type: object
              properties:
                words:
                  type: array
                  items:
                    type: string
                order:
                  type: string
                  enum: [asc, desc]
                  default: asc
        responses:
          200:
            description: Success
          400:
            description: Bad Request
        """
        data = request.get_json()
        order = data.get("order", "asc")

        sorted_words = sorted(data["words"], reverse=(order == "desc"))
        return jsonify(sorted_words)


@app.route("/api/docs")
def swagger_ui():
    return render_template("swaggerui.html")


@app.route("/api/spec")
def spec():
    swag = swagger(app)
    swag["info"]["version"] = "1.0"
    swag["info"]["title"] = "My API"
    return jsonify(swag)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
