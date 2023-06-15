from flask import Blueprint, jsonify, render_template
from flask_swagger import swagger

docs_blueprint = Blueprint("docs", __name__)


@docs_blueprint.route("/api/docs")
def swagger_ui():
    return render_template("swaggerui.html")
