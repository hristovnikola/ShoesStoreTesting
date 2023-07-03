import time

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class IndexPageTest(LiveServerTestCase):

    def test_index_page(self):
        driver = webdriver.Chrome()
        time.sleep(2)
        driver.get('http://127.0.0.1:8000/index')
        time.sleep(2)
        assert "Online Shoes Store" in driver.title
