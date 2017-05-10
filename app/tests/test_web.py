import unittest

from flask import Flask
from flask_testing import LiveServerTestCase
from selenium import webdriver


class AppTestCase(LiveServerTestCase):
    @property
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        self.driver = webdriver.Firefox()
        self.driver.get(self.get_server_url())

    def tearDown(self):
        self.driver.quit()

    def test_server_is_up_and_running(self):
        response = self.app.get(self.get_server_url())
        self.assertEqual(response.code, 200)

    def test_getting_to_voting_page(self):
        firstname = self.driver.find_element_by_name('first_name')
        firstname.send_keys('yulia')
        lastname = self.driver.find_element_by_name('last_name')
        lastname.send_keys('zorin')
        id = self.driver.find_element_by_name('id')
        id.send_keys('678')
        self.driver.find_element_by_name("submit").click()
        # check if user where able to enter parties page
        self.assertIn(u'ברוכים הבאים , yulia zorin', self.driver.find_element_by_tag_name('h1'))

    def test_user_not_in_database(self):
        firstname = self.driver.find_element_by_name('first_name')
        firstname.send_keys('yulia')
        lastname = self.driver.find_element_by_name('last_name')
        lastname.send_keys('zorin')
        id = self.driver.find_element_by_name('id')
        id.send_keys('987')
        self.driver.find_element_by_name("submit").click()
        # check if user where able to enter parties page
        self.assertIn(u'המצביע אינו מופיע בבסיס הנתונים', self.driver.find_element_by_class_name("error"))

# Run tests if script was executed directly from the shell
if (__name__ == '__main__'):
    unittest.main()
