from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.test import TestCase
from django.contrib.auth.models import User, Group
from django.urls import reverse

from ShoesStoreApp.models import Customer, Shoes, ShoesSize, Order, OrderItem, DeliveryInformation


class IndexViewTestCase(TestCase):
    def test_index_view(self):
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class ShoesViewTest(TestCase):
    def test_shoes_list(self):
        self.shoes = Shoes.objects.create(name='PUMA Патики Rs-X', description='Comfortable running shoes',
                                          brand='PUMA',
                                          type='Running shoes', color='Black', price=99.99)
        response = self.client.get('/shoes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shoes.html')
        self.assertContains(response, f"{self.shoes.type}")
        self.assertContains(response, f"{self.shoes.name}")
        self.assertContains(response, f"{self.shoes.price}")
        self.assertContains(response, f"{self.shoes.brand}")

    def test_filter_by_shoe_type(self):
        Shoes.objects.create(name='Running Shoes', description='Comfortable running shoes', brand='Nike',
                             type='Running shoes', color='Black', price=99.99)
        Shoes.objects.create(name='Basketball Shoes', description='High-performance basketball shoes', brand='Nike',
                             type='Basketball shoes', color='Red', price=129.99)
        Shoes.objects.create(name='Tennis Shoes', description='Durable tennis shoes', brand='Adidas',
                             type='Tennis shoes', color='White', price=89.99)

        response = self.client.get('/shoes/?type=Running shoes')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shoes.html')

        self.assertContains(response, "Running Shoes")

        self.assertNotContains(response, 'Basketball Shoes')
        self.assertNotContains(response, 'Tennis Shoes')

    def test_filter_by_shoe_brand(self):
        Shoes.objects.create(name='Nike Jordan 312', description='Comfortable running shoes', brand='Nike',
                             type='Running shoes', color='Black', price=99.99)
        Shoes.objects.create(name='Basketball Shoes', description='High-performance basketball shoes', brand='Nike',
                             type='Basketball shoes', color='Red', price=129.99)
        Shoes.objects.create(name='Brooks Shoes', description='Comfortable running shoes', brand='Brooks',
                             type='Running shoes', color='Black', price=99.99)

        response = self.client.get('/shoes/?brand=Nike')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shoes.html')

        self.assertContains(response, "Nike Jordan 312")
        self.assertContains(response, "Running shoes")
        self.assertContains(response, "Nike")
        self.assertContains(response, "99.99")

        self.assertContains(response, "Basketball Shoes")
        self.assertContains(response, "Running shoes")
        self.assertContains(response, "Nike")
        self.assertContains(response, "129.99")

        self.assertNotContains(response, "Brooks Shoes")

    def test_pagination(self):
        for i in range(1, 9):
            Shoes.objects.create(name=f'Running Shoes {i}', description='Comfortable running shoes', brand='Nike',
                                 type='Running shoes', color='Black', price=99.99)

        response = self.client.get('/shoes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shoes.html')

        all_shoes = Shoes.objects.all()

        paginator = Paginator(all_shoes, 6)
        self.assertEqual(paginator.num_pages, 2)

        response = self.client.get("/shoes/?page=1")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shoes.html')
        self.assertContains(response, 'Running Shoes', count=6)

        response = self.client.get("/shoes/?page=2")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shoes.html')
        self.assertContains(response, 'Running Shoes', count=2)


class Authentication(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser123',
            password='12test12',
            email='test@example.com'
        )

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        response = self.client.post('/loginPage/', {'username': 'testuser123', 'password': '12test12'})
        print(response)
        second_response = self.client.get(response.url)
        print(second_response)
        content = second_response.content.decode('utf-8')
        print(content)
        self.assertTrue('testuser123' in content)

    def test_wrong_username(self):
        response = self.client.post('/loginPage/', {'username': 'wrong', 'password': '12test12'})
        content = response.content.decode('utf-8')
        # print(content)
        self.assertFalse('testuser123' in content)

    def test_wrong_password(self):
        response = self.client.post('/loginPage/', {'username': 'testuser123', 'password': 'wrong'})
        content = response.content.decode('utf-8')

        self.assertFalse('testuser123' in content)
