from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    user_address = models.CharField(max_length=100)
    registration = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.phone_number}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    price = models.DecimalField(default=1000.0, decimal_places=2, max_digits=10)
    count = models.IntegerField(default=1)
    adding_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.price}'

    def price_get(self):
        return self.price


class Order(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    sum_price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user_name} \
               Sum price: {self.sum_price} \
               Date: {self.order_date}'
