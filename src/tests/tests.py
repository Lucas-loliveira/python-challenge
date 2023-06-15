import json
import unittest

from app import app
from flask import Flask


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_vowel_count(self):
        data = {"words": ["batman", "robin", "coringa"]}
        response = self.app.post(
            "/api/vowel_count", data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertEqual(result, {"batman": 2, "robin": 2, "coringa": 3})

    def test_vowel_count_invalid_request(self):
        data = {"invalid_key": ["batman", "robin", "coringa"]}
        response = self.app.post(
            "/api/vowel_count", data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertIn("error", result)

    def test_sort_asc(self):
        data = {"words": ["batman", "robin", "coringa"], "order": "asc"}
        response = self.app.post(
            "/api/sort", data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertEqual(result, ["batman", "coringa", "robin"])

    def test_sort_desc(self):
        data = {"words": ["batman", "robin", "coringa"], "order": "desc"}
        response = self.app.post(
            "/api/sort", data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertEqual(result, ["robin", "coringa", "batman"])

    def test_sort_invalid_order(self):
        data = {"words": ["batman", "robin", "coringa"], "order": "invalid"}
        response = self.app.post(
            "/api/sort", data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertIn("error", result)
