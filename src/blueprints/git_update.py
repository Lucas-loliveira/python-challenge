import git
from flask import Blueprint, jsonify

git_update_blueprint = Blueprint("git_update", __name__)


@git_update_blueprint.route("/git_update", methods=["POST"])
def git_update():
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
    return jsonify({"message": "Git repository updated successfully."})
