from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.first_name


class Shoes(models.Model):
    BRAND = [
        ('Adidas', 'Adidas'),
        ('Nike', 'Nike'),
        ('Brooks', 'Brooks'),
        ('Puma', 'Puma'),
    ]
    TYPE = [
        ('Running shoes', 'Running shoes'),
        ('Basketball shoes', 'Basketball shoes'),
        ('Tennis shoes', 'Tennis shoes'),
        ('Football shoes', 'Football shoes'),
        ('Sneakers', 'Sneakers'),
        ('Sandals', 'Sandals'),
    ]
    SIZES = [
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    brand = models.CharField(max_length=255, choices=BRAND)
    type = models.CharField(max_length=255, choices=TYPE)
    color = models.CharField(max_length=255)
    size = models.ManyToManyField('ShoesSize', related_name="shoes")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"{self.name} - {self.price}"

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class ShoesSize(models.Model):
    size = models.CharField(max_length=255, choices=Shoes.SIZES)

    def __str__(self):
        return self.size


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.get_total for item in order_items])
        return total

    @property
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total


class OrderItem(models.Model):
    shoes = models.ForeignKey(Shoes, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    selected_size = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.shoes.name} - {self.quantity} pairs"

    @property
    def get_total(self):
        total = self.shoes.price * self.quantity
        return total


class DeliveryInformation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    phone_number = models.IntegerField(null=True)
    card_number = models.IntegerField(null=True, blank=True)
    name_on_card = models.CharField(max_length=255, null=True, blank=True)
    expiration_date = models.IntegerField(null=True, blank=True)
    cw = models.IntegerField(null=True, blank=True)
    pay_in_cash = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.surname}: {self.order.id}"