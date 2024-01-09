import unittest
from app import app, items

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_read_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")

    def test_add_item(self):
        response = self.app.post('/add', data=dict(item="Test Item"), follow_redirects=True)
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")

if __name__ == '__main__':
    unittest.main()