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

    def test_cant_access_without_login(self):
        # check if the url of accessing index page without logging in is the same of the login page
        index_page = self.app.get('/index', follow_redirects=True)
        return index_page.location == self.app.get('/login', follow_redirects=True)

    def test_false_login(self):
        # check that you can't login without id
        invalid_login = self.app.post('/login', data={'first_name': 'avihu', 'last_name': 'pinko'},
                                      follow_redirects=True)
        return b'Invalid credentials' in invalid_login.data

    def test_false_user_id(self):
        # check the error of user who's not in the database
        invalid_login = self.app.post('/login', data={'first_name': 'avihu', 'last_name': 'pinko', 'id': '987'},
                                      follow_redirects=True)
        return u'המצביע אינו מופיע בבסיס הנתונים' in invalid_login.data.decode("utf-8")

    def test_false_user_name(self):
        # check the error of wrong name for valid id
        invalid_login = self.app.post('/login', data={'first_name': 'avihu', 'last_name': 'pinko', 'id': '123'},
                                      follow_redirects=True)
        return u'המצביע אינו מופיע בבסיס הנתונים' in invalid_login.data.decode("utf-8")


# Run tests if script was executed directly from the shell
if (__name__ == '__main__'):
    unittest.main()
