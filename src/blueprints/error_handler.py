from flask import Blueprint, jsonify, make_response
from jsonschema import ValidationError

error_handler_blueprint = Blueprint("error_handler", __name__)


@error_handler_blueprint.app_errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        original_error = error.description
        return make_response(jsonify({"error": original_error.message}), 400)
    return error
