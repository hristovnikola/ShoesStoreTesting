import time

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")
        submit_button = self.driver.find_element(By.ID, "log_in_button")

        username_field.send_keys(username)
        password_field.send_keys(password)
        submit_button.click()


class ShoesPage:
    def __init__(self, driver):
        self.driver = driver

    def click_shoes_button(self):
        shoes_button = self.driver.find_element(By.ID, 'shoes_button')
        shoes_button.click()
        time.sleep(2)

    def select_shoes_size_and_add_to_cart(self, pair, size):
        shoes = self.driver.find_elements(By.CLASS_NAME, 'pair_of_shoe')
        if len(shoes) > 0:
            details_button = shoes[pair].find_element(By.CLASS_NAME, 'details_button')
            details_button.click()

        time.sleep(2)

        available_sizes = self.driver.find_elements(By.NAME, "selected_size")
        if len(available_sizes) > 0:
            selected_size = available_sizes[size]
            selected_size.click()

        time.sleep(2)

        add_to_cart_button = self.driver.find_element(By.ID, "add_to_cart_button")
        add_to_cart_button.click()

        time.sleep(2)


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_cart_item_count(self):
        delete_buttons = self.driver.find_elements(By.CLASS_NAME, "delete_cart_item")
        return len(delete_buttons)

    def get_item_quantity(self, index):
        item_quantities = self.driver.find_elements(By.CLASS_NAME, "item_quantity")
        return int(item_quantities[index].text)

    def increase_item_quantity(self, index):
        inc_quantity_buttons = self.driver.find_elements(By.CLASS_NAME, "inc_button")
        inc_quantity_buttons[index].click()
        time.sleep(2)

    def decrease_item_quantity(self, index):
        dec_quantity_buttons = self.driver.find_elements(By.CLASS_NAME, "dec_button")
        dec_quantity_buttons[index].click()
        time.sleep(2)

    def delete_cart_item(self, index):
        delete_buttons = self.driver.find_elements(By.CLASS_NAME, "delete_cart_item")
        delete_buttons[index].click()
        time.sleep(2)


class CustomerTests(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8000/loginPage')
        time.sleep(2)
        self.login_page = LoginPage(self.driver)
        self.shoes_page = ShoesPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.login_as_customer()

    def login_as_customer(self):
        self.login_page.login("hristov.nikola", "customerpass")
        time.sleep(2)
        assert ('hristov.nikola' and 'Logout' and 'Cart') in self.driver.page_source

    def test_customer_access(self):
        self.shoes_page.click_shoes_button()
        self.shoes_page.select_shoes_size_and_add_to_cart(0, 0)

        assert self.cart_page.get_cart_item_count() == 1
        assert self.cart_page.get_item_quantity(0) == 1

        self.shoes_page.click_shoes_button()
        self.shoes_page.select_shoes_size_and_add_to_cart(1, 0)

        assert self.cart_page.get_cart_item_count() == 2

        self.shoes_page.click_shoes_button()
        self.shoes_page.select_shoes_size_and_add_to_cart(0, 0)

        assert self.cart_page.get_cart_item_count() == 2
        assert self.cart_page.get_item_quantity(0) == 2

        self.cart_page.increase_item_quantity(0)
        time.sleep(2)
        self.cart_page.increase_item_quantity(0)
        time.sleep(2)

        assert self.cart_page.get_item_quantity(0) == 4

        self.cart_page.decrease_item_quantity(0)

        time.sleep(2)

        assert self.cart_page.get_item_quantity(0) == 3

        self.cart_page.delete_cart_item(0)

        time.sleep(2)

        assert self.cart_page.get_cart_item_count() == 1
