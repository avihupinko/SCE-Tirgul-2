import unittest

import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        # Create Flask test client
        self.app = app.app.test_client()

    def tearDown(self):
        # Clear the data after each test
        app.data = {}
        app.free_id = 0

    def test_false_login(self):
        invalid_login = self.app.post('login', data={'first_name': 'avihu', 'last_name': 'pinko'},
                                      follow_redirects=True)
        assert 'Invalid credentials' in invalid_login.data


# Run tests if script was executed directly from the shell
if (__name__ == '__main__'):
    unittest.main()
