from random import randint

from django.core.management.base import BaseCommand
from homework_app.models import Product, Order, User


class Command(BaseCommand):
    help = "Fake order creation."

    def handle(self, *args, **kwargs):
        for user in User.objects.all():
            order = Order(user_name=user)
            order.save()
            sum_price = 0
            for _ in range(5):
                pid = randint(1, 20)
                prd = Product.objects.filter(pk=pid).first()
                order.products.add(prd)
                sum_price += prd.price_get()
            order.sum_price = sum_price
            order.save()
        self.stdout.write('Orders created')
