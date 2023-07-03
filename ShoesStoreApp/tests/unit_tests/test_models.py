
# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from ShoesStoreApp.models import Customer, Shoes, ShoesSize, Order, OrderItem, DeliveryInformation


class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='nikola', password='testpassword')
        self.customer = Customer.objects.create(user=self.user, first_name='Nikola', email='hristov.nikola@yahoo.com')
        self.shoes = Shoes.objects.create(name='Running Shoes', description='Very good shoes', brand='Nike',
                                          type='Running shoes', color='Black', price=99.99)
        self.shoes_size = ShoesSize.objects.create(size='42')
        self.order = Order.objects.create(customer=self.customer)
        self.order_item = OrderItem.objects.create(shoes=self.shoes, order=self.order, selected_size=42, quantity=2)
        self.delivery_info = DeliveryInformation.objects.create(
            customer=self.customer,
            order=self.order,
            name='Nikola',
            surname='Hristov',
            city='Bitola',
            address='Example street',
            email='hristov.nikola@yahoo.com',
            phone_number=1234567890,
            card_number='1234567812345678',
            name_on_card='Nikola Hristov',
            expiration_date=1225,
            cw=123
        )

    def test_customer_model(self):
        self.assertEqual(str(self.customer), 'Nikola')

    def test_shoes_model(self):
        self.assertEqual(str(self.shoes), 'Running Shoes - 99.99')

    def test_shoes_size_model(self):
        self.assertEqual(str(self.shoes_size), '42')

    def test_order_model(self):
        self.assertEqual(str(self.order), str(self.order.id))

    def test_order_item_model(self):
        self.assertEqual(str(self.order_item), 'Running Shoes - 2 pairs')

    def test_delivery_information_model(self):
        self.assertEqual(str(self.delivery_info), 'Nikola Hristov: ' + str(self.order.id))
