import unittest
from unittest.mock import MagicMock, patch

import git
from app import app
from flask import Flask

# Import the module containing the code to be tested


class GitUpdateTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch("git.Repo")
    def test_git_update(self, mock_repo):
        # Create mock objects
        mock_origin = MagicMock()
        mock_repo.return_value.remotes.origin = mock_origin
        mock_head = MagicMock()
        mock_repo.return_value.create_head.return_value = mock_head

        response = self.app.post("/git_update")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json(), {"message": "Git repository updated successfully."}
        )
        mock_repo.assert_called_once_with("./python-challenge")
        mock_repo.return_value.create_head.assert_called_once_with(
            "main", mock_repo.return_value.remotes.origin.refs.main
        )
        mock_head.set_tracking_branch.assert_called_once_with(
            mock_repo.return_value.remotes.origin.refs.main
        )
        mock_origin.pull.assert_called_once()
