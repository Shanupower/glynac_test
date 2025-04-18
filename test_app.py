import unittest
from app import app

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()  # PUSH the app context

    def tearDown(self):
        self.app_context.pop()

    def test_health_check(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'status', response.data)

if __name__ == '__main__':
    unittest.main()
