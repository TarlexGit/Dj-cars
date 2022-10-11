from core.settings import DEBUG
from users.models import User
from django.core.management import CommandError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "create superuser for development"

    def handle(self, *args, **options):
        if DEBUG:
            name_pass = "tarlex"

            user = User._default_manager.create(
                username=name_pass,
                is_superuser=True,
                is_staff=True,
                email="tarlex.py@ya.ru",
            )
            user.set_password(name_pass)
            user.save()
        else:
            raise CommandError(
                "супер не был создан, команда доступна только для разработки"
            )
