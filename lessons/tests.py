from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchWindowException, WebDriverException, ErrorInResponseException

class SimpleTest(TestCase):
    def test_basic_views(self):
        response = client.get('/')
        response.status_code
        
    def create_lesson(nam, tut, des):
        Lesson.object.create(name = nam, tutorial = tut, description = des)

        
class MySeleniumTests(LiveServerTestCase):
    fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(MySeleniumTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('TestUser')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('BlaTestUserBla123')
        self.selenium.find_element_by_xpath('//input[@value="login"]').click()
        
    def test_register(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/register/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('TestUser')
        password_1_input = self.selenium.find_element_by_name("password1")
        password_1_input.send_keys('BlaTestUserBla123')
        password_2_input = self.selenium.find_element_by_name("password2")
        password_2_input.send_keys('BlaTestUserBla123')
        self.selenium.find_element_by_xpath('//input[@value="Create the account"]').click()
        
    def test_views(self):
        f = open('D:/Users/Alexander Wendland/Documents/GitHub/mimir/lessons/Test_pages_1.txt', 'r')
        urls = list(f)
        
        print 'Checking pages as unregistered user ...'
        
        for url in urls:
            print 'Trying to open ' + url + ' ...'
            try:
                self.selenium.get('%s%s' % (self.live_server_url, url))
                print 'SUCCESS: Loaded ' + url + ' as unregistered user'
            except Exception:
                print 'ERROR: Could not load ' + url + ' page as unregistered user'
        
        f.close()
        
        print 'Done' 
        print 'Registering user ...'
        
        self.selenium.get('%s%s' % (self.live_server_url, '/register/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('TestUser')
        password_1_input = self.selenium.find_element_by_name("password1")
        password_1_input.send_keys('BlaTestUserBla123')
        password_2_input = self.selenium.find_element_by_name("password2")
        password_2_input.send_keys('BlaTestUserBla123')
        self.selenium.find_element_by_xpath('//input[@value="Create the account"]').click()
        
        f = open('D:/Users/Alexander Wendland/Documents/GitHub/mimir/lessons/Test_pages_2.txt', 'r')
        
        urls = list(f)
        
        print 'Checking pages as registered user ...'
        
        for url in urls:
            print 'Trying to open ' + url + ' ...'
            try:
                self.selenium.get('%s%s' % (self.live_server_url, url))
                print 'SUCCESS: Loaded ' + url + ' as registered user'
            except Exception:
                print 'ERROR: Could not load ' + url + ' page as registered user'
        
        f.close()
    
    def test_lessons(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/register/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('TestUser')
        password_1_input = self.selenium.find_element_by_name("password1")
        password_1_input.send_keys('BlaTestUserBla123')
        password_2_input = self.selenium.find_element_by_name("password2")
        password_2_input.send_keys('BlaTestUserBla123')
        self.selenium.find_element_by_xpath('//input[@value="Create the account"]').click()
        self.selenium.get('%s%s' % (self.live_server_url, '/logout/'))
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('TestUser')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('BlaTestUserBla123')
        self.selenium.find_element_by_xpath('//input[@value="login"]').click()
        create_lesson('bla','bla','bla')
        