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
        response = self.app.get(self.get_server_url(), content_type='application/json')
        self.assertEqual(response.code, 200)

    def test_voting(self):
        self.browser.get(' http://127.0.0.1:5000/login')
        firstname = self.browser.find_element_by_name('first_name')
        firstname.send_keys('yulia')
        lastname = self.browser.find_element_by_name('last_name')
        lastname.send_keys('zorin')

        id = self.browser.find_element_by_name('id')
        id.send_keys('678')

        form = self.browser.find_element_by_id('loginForm')
        form.submit()


# Run tests if script was executed directly from the shell
if (__name__ == '__main__'):
    unittest.main()
