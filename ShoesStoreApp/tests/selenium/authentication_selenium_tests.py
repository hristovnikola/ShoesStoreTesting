import time

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AuthenticationPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        login_nav_button = self.driver.find_element(By.ID, 'login_button')
        login_nav_button.click()
        time.sleep(2)

        user_name = self.driver.find_element(By.NAME, 'username')
        user_password = self.driver.find_element(By.NAME, 'password')
        submit_button = self.driver.find_element(By.ID, 'log_in_button')
        time.sleep(2)

        user_name.send_keys(username)
        user_password.send_keys(password)
        time.sleep(2)

        submit_button.send_keys(Keys.RETURN)

    def fill_registration_form(self, username, email, password):
        username_register = self.driver.find_element(By.NAME, 'username')
        email_register = self.driver.find_element(By.NAME, 'email')
        password_register = self.driver.find_element(By.NAME, 'password1')
        repeat_password_register = self.driver.find_element(By.NAME, 'password2')
        time.sleep(2)

        username_register.send_keys(username)
        email_register.send_keys(email)
        password_register.send_keys(password)
        repeat_password_register.send_keys(password)


class AuthenticationTest(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.auth_page = AuthenticationPage(self.driver)

        driver.get('http://127.0.0.1:8000/index')
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_login_selenium(self):
        self.auth_page.login('admin', 'dnick201097homework')
        time.sleep(2)

        assert 'admin' in self.driver.page_source

    def test_register_selenium(self):
        self.auth_page.login('example.user', 'thisIsTestPassword')
        time.sleep(2)

        assert 'Bad credentials' in self.driver.page_source

        register_in_form_login_button = self.driver.find_element(By.ID, 'register_in_form_login')
        register_in_form_login_button.click()

        self.auth_page.fill_registration_form('example.user', 'hristov.nikola@yahoo.com', 'thisIsTestPassword')
        time.sleep(2)

        submit_register_button = self.driver.find_element(By.ID, 'register_button')
        submit_register_button.send_keys(Keys.RETURN)
        time.sleep(2)

        assert 'Account was created for example.user' in self.driver.page_source

        self.auth_page.login('example.user', 'thisIsTestPassword')
        time.sleep(2)

        assert 'example.user' in self.driver.page_source
