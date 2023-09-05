from django.core.management.base import BaseCommand
from homework_app.models import User


class Command(BaseCommand):
    help = "Fake user creation."

    def handle(self, *args, **kwargs):
        for i in range(1, 6):
            user = User(
                name=f'Name_{i}',
                email=f'e{i}@mail.com',
                phone_number=f'+7 (123) 111-11-1{i}',
                user_address=f'Регион, Город, Улица, Дом, Кв.',
            )
            user.save()
        self.stdout.write('Users created')
