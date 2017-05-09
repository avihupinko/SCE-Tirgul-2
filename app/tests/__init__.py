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

    def test_cant_enter_without_login(self):
        # Check if login link is visible
        index_page = self.app.get('/index')
        assert 'Log in' not in index_page

        # def test_login(self):
        #     # Check if login link is visible
        #     index_page = self.app.get('/')
        #     assert 'Log in' in index_page.data
        #
        #     # Check if form visible
        #     login_page = self.app.get('/login')
        #     assert 'login' in login_page.data
        #     assert 'password' in login_page.data
        #
        #     # Check invalid data
        #     invalid_login = self.app.post('login', data=dict(login='invalid', password='invalid'), follow_redirects=True)
        #     assert 'Invalid credentials' in invalid_login.data
        #
        #     # Check valid credentials
        #     valid_login = self.app.post('login', data=dict(login='admin', password='demo'), follow_redirects=True)
        #     assert 'You were logged in' in valid_login.data
        #
        #     # Test logging out
        #     logout = self.app.get('logout', follow_redirects=True)
        #     assert 'You were logged out' in logout.data


# Run tests if script was executed directly from the shell
if (__name__ == '__main__'):
    unittest.main()
