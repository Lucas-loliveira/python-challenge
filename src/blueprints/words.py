from flask import Blueprint, jsonify, request
from flask_expects_json import expects_json
from jsonschema import ValidationError

from src.blueprints.schemas.schema import SORT_SCHEMA, VOWEL_COUNT_SCHEMA

words_blueprint = Blueprint("words", __name__)


@words_blueprint.route("/api/vowel_count", methods=["POST"])
@expects_json(VOWEL_COUNT_SCHEMA)
def count_vowels():
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
        vowel_count = sum(
            1 for char in word.lower() if char in "aeiouáéíóúãõâêîôûàèìòùäëïöü"
        )
        result[word] = vowel_count

    return jsonify(result)


@words_blueprint.route("/api/sort", methods=["POST"])
@expects_json(SORT_SCHEMA)
def sort_words():
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
