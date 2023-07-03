import time

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class UserRestrictions(LiveServerTestCase):

    def test_unauthenticated_user_permission(self):
        driver = webdriver.Chrome()
        time.sleep(2)
        driver.get('http://127.0.0.1:8000/index')

        time.sleep(2)

        shoes_button = driver.find_element(By.ID, 'shoes_button')
        shoes_button.click()

        time.sleep(2)

        assert "Add new shoes" not in driver.page_source

        shoes = driver.find_elements(By.CLASS_NAME, 'pair_of_shoe')

        time.sleep(2)

        if len(shoes) > 0:
            details_button = shoes[0].find_element(By.CLASS_NAME, 'details_button')
            details_button.click()
            print(shoes)

        time.sleep(2)

        assert "Edit" and "Delete" and "Add to Cart" not in driver.page_source
        assert "Back to Shoes" in driver.page_source

    def test_unauthenticated_user_denied_access_to_certain_pages(self):
        driver = webdriver.Chrome()
        time.sleep(2)

        urls = ['http://127.0.0.1:8000/cart', 'http://127.0.0.1:8000/add_shoes']
        for url in urls:
            driver.get(url)
            time.sleep(2)
            assert "Log in" in driver.page_source
