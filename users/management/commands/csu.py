from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Создает супер-пользователя при вызове комманды
    """

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@mail.ru',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        user.set_password('admin')
        user.save()