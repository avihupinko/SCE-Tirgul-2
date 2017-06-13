import unittest

from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
        self.yulia = User('yulia', 'zorin', '678')
        self.yarok = Party(u'עלה ירוק', 'https://pbs.twimg.com/profile_images/553476099775016960/8Ha40Qym_400x400.jpeg')
        db.session.add(self.yarok)
        db.session.add(self.yulia)
        db.session.commit()

    def setUp(self):
        # create a new Firefox session
        self.browser = webdriver.PhantomJS()
        # nevigate to the application home page
        self.browser.get(self.get_server_url())
        self.str = '×”×ž×¦×‘×™×¢ ××™× ×• ×ž×•×¤×™×¢ ×‘×‘×¡×™×¡ ×”× ×ª×•× ×™× ××• ×©×›×‘×¨ ×”×¦×‘×™×¢'

    def tearDown(self):
        self.browser.quit()
        with app.app_context():
            db.drop_all()
            db.session.remove()

    def test_getting_to_voting_page(self):
        first_name = self.browser.find_element_by_name('first_name')
        first_name.send_keys('yulia')
        last_name = self.browser.find_element_by_name('last_name')
        last_name.send_keys('zorin')
        id = self.browser.find_element_by_name('id')
        id.send_keys('678')
        id.send_keys(Keys.ENTER)

        assert self.str not in self.browser.page_source

    def test_full_vote(self):
        first_name = self.browser.find_element_by_name('first_name')
        first_name.send_keys('yulia')
        last_name = self.browser.find_element_by_name('last_name')
        last_name.send_keys('zorin')
        id = self.browser.find_element_by_name('id')
        id.send_keys('678')
        id.send_keys(Keys.ENTER)
        assert u'לצורך הצבעה, בחר את המפלגה הרצויה' in self.browser.page_source
        # select party
        select_elements = self.browser.find_elements_by_name('partyId')
        select_elements[0].submit()
        self.browser.find_element_by_id('ok').click()
        assert u'האם ברצונך לאשר את הצבעתך' in self.browser.page_source

        # confirm selected party
        confirm = self.browser.find_element_by_class_name('submit')
        confirm.send_keys(u'אשר')
        confirm.submit()

        assert u'ברוכים הבאים למערכת הבחירות הממוחשבת' in self.browser.page_source

    def test_user_not_in_database(self):
        firstname = self.browser.find_element_by_name('first_name')
        firstname.send_keys('yulia')
        lastname = self.browser.find_element_by_name('last_name')
        lastname.send_keys('zorin')
        id = self.browser.find_element_by_name('id')
        id.send_keys('987')
        id.send_keys(Keys.ENTER)
        # self.browser.find_element_by_name("submit").click()
        # check if user where able to enter parties page
        assert self.str not in self.browser.page_source


# Run tests if script was executed directly from the shell
if (__name__ == '__main__'):
    unittest.main()
