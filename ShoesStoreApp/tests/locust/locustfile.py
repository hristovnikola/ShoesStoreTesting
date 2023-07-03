import time

from locust import HttpUser, task, between, TaskSet
from requests.auth import HTTPBasicAuth
import requests
from bs4 import BeautifulSoup


class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def index_page(self):
        self.client.get(url="/index")

    @task
    def shoes_page(self):
        self.client.get(url="/shoes")

    @task
    def login_page(self):
        self.client.get(url="/loginPage")

    @task
    def register_page(self):
        self.client.get(url="/register")

    @task
    def cart_page(self):
        self.client.get(url="/cart")

    @task
    def login_post(self):
        data = {
            "username": "hristov.nikola",
            "password": "customerpass"
        }
        self.client.post("/loginPage/", data=data)

    @task
    def register_post(self):
        data = {
            "username": "testuser",
            "email": "test@test.com",
            "password1": "passwordfortestuser123",
            "password2": "passwordfortestuser123"
        }
        response = self.client.post("/register/", data=data)
        print(response.request.headers)
        print(response.headers)
