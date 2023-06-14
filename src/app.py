import git
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello test flask home page CI pull request"


@app.route("/git_update", methods=["POST"])
def git_update():
    repo = git.Repo("./python-challenge")
    origin = repo.remotes.origin
    repo.create_head("main", origin.refs.main).set_tracking_branch(
        origin.refs.main
    ).checkout()
    origin.pull()
    return "", 200


@app.route("/vowel_count", methods=["POST"])
def count_vowels():
    if request.content_type != "application/json":
        return jsonify({"error": "Content type must be application/json"}), 400

    data = request.get_json()
    if "words" not in data or not isinstance(data["words"], list):
        return jsonify({"error": "Invalid request data"}), 400

    result = {}
    for word in data["words"]:
        vowel_count = sum(1 for char in word.lower() if char in "aeiou")
        result[word] = vowel_count

    return jsonify(result)


@app.route("/sort", methods=["POST"])
def sort_words():
    if request.content_type != "application/json":
        return jsonify({"error": "Content type must be application/json"}), 400

    data = request.get_json()
    if "words" not in data or not isinstance(data["words"], list):
        return jsonify({"error": "Invalid request data"}), 400

    order = data.get("order", "asc")
    if order not in ["asc", "desc"]:
        return jsonify({"error": "Invalid sort order"}), 400

    sorted_words = sorted(data["words"], reverse=(order == "desc"))
    return jsonify(sorted_words)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
