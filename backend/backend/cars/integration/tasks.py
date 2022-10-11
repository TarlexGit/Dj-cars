from celery import shared_task
from integration.services.parsing import get_data


@shared_task
def take_date_from_integration(url):
    # url = "http://export.maxposter.ru/legocar-used-all/3073-15554.xml"
    data = get_data(url)
    # print(data)
    if data == 200:
        print("DONE")
    else:
        print("ERROR")
