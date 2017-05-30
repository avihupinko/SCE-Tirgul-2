import unittest

from flask_testing import LiveServerTestCase
from selenium import webdriver

from app import app, db
from app.models import User, Party


class AppTestCase(LiveServerTestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8943
        app.config['LIVESERVER_TIMEOUT'] = 10
        db.init_app(app)
        with app.app_context():
            db.create_all()
            self.insert_data_to_db()
        return app

    def insert_data_to_db(self):
        db.session.commit()
        yulia = User('yulia', 'zorin', '678')
        yarok = Party(u'עלה ירוק', 'https://pbs.twimg.com/profile_images/553476099775016960/8Ha40Qym_400x400.jpeg')
        db.session.add(yarok)
        db.session.add(yulia)
        db.session.commit()

    def setUp(self):
        # create a new Firefox session
        self.browser = webdriver.PhantomJS()
        # nevigate to the application home page
        self.browser.get(self.get_server_url())

    def tearDown(self):
        self.browser.quit()
        with app.app_context():
            db.session.remove()
            db.drop_all()

    # def test_server_is_up_and_running(self):
    #     response = self.app.get(self.get_server_url())
    #     self.assertEqual(response.code, 200)

    def test_getting_to_voting_page(self):
        firstname = self.browser.find_element_by_name('first_name')
        firstname.send_keys('yulia')
        lastname = self.browser.find_element_by_name('last_name')
        lastname.send_keys('zorin')
        id = self.browser.find_element_by_name('id')
        id.send_keys('678')
        self.browser.find_element_by_name("submit").click()
        # check if user where able to enter parties page
        self.assertIn(u'ברוכים הבאים , yulia zorin', self.browser.find_element_by_tag_name('h1'))

    def test_user_not_in_database(self):
        firstname = self.browser.find_element_by_name('first_name')
        firstname.send_keys('yulia')
        lastname = self.browser.find_element_by_name('last_name')
        lastname.send_keys('zorin')
        id = self.browser.find_element_by_name('id')
        id.send_keys('987')
        self.browser.find_element_by_name("submit").click()
        # check if user where able to enter parties page
        self.assertIn(u'המצביע אינו מופיע בבסיס הנתונים', self.browser.find_element_by_class_name("error"))


# Run tests if script was executed directly from the shell
if (__name__ == '__main__'):
    unittest.main()
