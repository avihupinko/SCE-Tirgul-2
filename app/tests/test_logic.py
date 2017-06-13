import unittest

from app import app, db


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()
        self.check = app.test_client(self)

    def tearDown(self):
        del self.check
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_cant_access_without_login(self):
        # check if the url of accessing index page without logging in is the same of the login page
        index_page = self.app.get('/index', content_type='application/json')
        self.assertEqual(index_page.status_code, 302)

    def test_false_login(self):
        # check that you can't login without id
        invalid_login = self.app.post('/login', data=dict(first_name='avihu', last_name='pinko'),
                                      follow_redirects=True)
        self.assertIn('400 Bad Request', invalid_login.data.decode("utf-8"))

    def test_false_user_id(self):
        # check the error of user who's not in the database
        invalid_login = self.app.post('/login', data=dict(first_name='avihu', last_name='pinko', id='987'),
                                      follow_redirects=True)
        self.assertIn(u'המצביע אינו מופיע בבסיס הנתונים', invalid_login.data.decode("utf-8"))

    def test_false_user_name(self):
        # check the error of wrong name for valid id
        invalid_login = self.app.post('/login', data=dict(first_name='avihu', last_name='pinko', id='123'),
                                      follow_redirects=True)
        self.assertIn(u'פרטים שגויים, נסה שוב', invalid_login.data.decode("utf-8"))


# Run tests if script was executed directly from the shell
if (__name__ == '__main__'):
    unittest.main()
