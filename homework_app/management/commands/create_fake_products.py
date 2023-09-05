from random import uniform, randint

from django.core.management.base import BaseCommand
from homework_app.models import Product


class Command(BaseCommand):
    help = "Fake product creation."

    def handle(self, *args, **kwargs):
        for i in range(1, 21):
            product = Product(
                name=f'Товар {i}',
                content=f'Описание товара',
                price=uniform(500, 10000),
                count=randint(1, 20),
            )
            product.save()
        self.stdout.write('Products created')