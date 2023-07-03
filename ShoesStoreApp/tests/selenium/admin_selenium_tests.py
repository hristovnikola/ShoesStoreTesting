import time
import os

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")


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

    def click_add_shoes_button(self):
        add_shoes_btn = self.driver.find_element(By.ID, 'add_shoes_btn')
        add_shoes_btn.click()
        time.sleep(2)

    def click_shoes_button(self):
        shoes_button = self.driver.find_element(By.ID, 'shoes_button')
        shoes_button.click()
        time.sleep(2)

    def add_new_shoes(self):
        name_field = self.driver.find_element(By.NAME, 'name')
        name_field.send_keys('ABCD shoes')
        time.sleep(1)
        price_field = self.driver.find_element(By.NAME, 'price')
        price_field.send_keys('55')
        time.sleep(1)

        description_field = self.driver.find_element(By.NAME, 'description')
        description_field.send_keys('This is a new pair of shoes.')
        time.sleep(1)

        size_field = self.driver.find_element(By.NAME, 'size')
        size_field.send_keys('39')
        time.sleep(1)

        brand_field = self.driver.find_element(By.NAME, 'brand')
        brand_field.send_keys('Nike')
        time.sleep(1)

        type_field = self.driver.find_element(By.NAME, 'type')
        type_field.send_keys('Running')
        time.sleep(1)

        color_field = self.driver.find_element(By.NAME, 'color')
        color_field.send_keys('Blue')
        time.sleep(1)

        image_field = self.driver.find_element(By.NAME, 'image')
        image_path = "C://Users/lenovo/Desktop/example.jpg"
        image_field.send_keys(image_path)
        time.sleep(1)

        submit_button = self.driver.find_element(By.ID, 'add_edit_shoes_submit')
        submit_button.click()
        time.sleep(1)

    def click_details_button(self, pair):
        shoes = self.driver.find_elements(By.CLASS_NAME, 'pair_of_shoe')
        if len(shoes) > 0:
            details_button = shoes[pair].find_element(By.CLASS_NAME, 'details_button')
            self.driver.execute_script("arguments[0].scrollIntoView();", details_button)
            time.sleep(2)
            details_button.click()

        time.sleep(2)

    def select_shoes_size_and_add_to_cart(self, pair, size):
        self.click_details_button(pair)
        available_sizes = self.driver.find_elements(By.NAME, "selected_size")
        if len(available_sizes) > 0:
            selected_size = available_sizes[size]
            selected_size.click()

        time.sleep(5)

        add_to_cart_button = self.driver.find_element(By.ID, "add_to_cart_button")
        add_to_cart_button.click()

        time.sleep(2)

    def click_edit_button_and_edit_shoes(self):
        edit_button = self.driver.find_element(By.ID, 'edit_button')
        edit_button.click()
        time.sleep(2)

        shoes_name = self.driver.find_element(By.ID, 'id_name')
        shoes_name.clear()
        time.sleep(2)
        shoes_name.send_keys('AAA shoes')
        time.sleep(2)
        shoes_name = self.driver.find_element(By.ID, 'id_price')
        shoes_name.clear()
        time.sleep(2)
        shoes_name.send_keys('100')
        time.sleep(2)

        edit_submit_btn = self.driver.find_element(By.ID, 'add_edit_shoes_submit')
        self.driver.execute_script("arguments[0].scrollIntoView();", edit_submit_btn)
        time.sleep(2)
        edit_submit_btn.click()

    def click_delete_shoes(self):
        delete_shoes_btn = self.driver.find_element(By.ID, 'delete_button')
        delete_shoes_btn.click()
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


class AdminTests(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8000/loginPage')
        time.sleep(2)
        self.login_page = LoginPage(self.driver)
        self.shoes_page = ShoesPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.login_as_admin()

    def login_as_admin(self):
        self.login_page.login("admin", "dnick201097homework")
        time.sleep(2)
        assert 'admin' and 'Logout' and 'Cart' in self.driver.page_source

    def test_admin_adding_shoes(self):
        self.shoes_page.click_shoes_button()
        self.shoes_page.click_add_shoes_button()
        self.shoes_page.add_new_shoes()

    def test_admin_editing_shoes(self):
        self.shoes_page.click_shoes_button()
        self.shoes_page.click_details_button(0)
        self.shoes_page.click_edit_button_and_edit_shoes()

        time.sleep(2)

        assert "AAA shoes" in self.driver.page_source

    def test_admin_deleting_shoes(self):
        self.shoes_page.click_shoes_button()
        assert 'AAA shoes' in self.driver.page_source
        self.shoes_page.click_details_button(0)
        self.shoes_page.click_delete_shoes()
        time.sleep(2)
        assert 'AAA shoes' not in self.driver.page_source
