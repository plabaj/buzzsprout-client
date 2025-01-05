import unittest
from buzzsprout_client import BuzzsproutClient

class TestBuzzsproutClient(unittest.TestCase):
    def test_client_initialization(self):
        client = BuzzsproutClient(api_key="test_key")
        self.assertEqual(client.api_key, "test_key")
        self.assertEqual(client.base_url, "https://www.buzzsprout.com/api")
