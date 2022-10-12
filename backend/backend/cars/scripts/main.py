from integration.models import Task, DataHub
from pprint import pprint
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError


def run():
    try:
        User = get_user_model()
        new_super = User.objects.create_superuser("admin", "admin@example.com", "admin")
        print(new_super, "user created")

    except IntegrityError:
        print("superuser already exists")
    # Fetch all questions

    urls = {
        1: "http://export.maxposter.ru/legocar-used-all/3073-15554.xml",
        2: "http://export.maxposter.ru/legocar-used-all/3413-78456.xml",
        3: "http://kan-ftp.kanavto.ru/newavto/Avtoru_kae_renaultoren.xml",
    }

    for u in urls:
        dh, status = DataHub.objects.get_or_create(title=u, url=urls[u])
        Task.objects.get_or_create(title=u, execute=False, result=None, dh=dh)

    print(f"\nCREATED:\n{pprint(urls)}\n{Task.objects.all()}")
