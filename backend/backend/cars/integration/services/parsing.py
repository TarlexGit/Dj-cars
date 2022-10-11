from urllib import request
import requests
import xml.etree.ElementTree as ET

from gallery.models import CarImage
from .save_objects import save_data_to_model
from django.core.files import File
from django.conf import settings
import shutil
from django.core.files.temp import NamedTemporaryFile
from .check_image import check_and_resize


def find_data(node):
    vin = node.find("vin").text
    id = node.find("id").text if node.find("id") else None
    price = node.find("price").text
    model = node.find("model").text if node.find("model") else None
    if not model:
        model = node.find("folder_id").text if node.find("folder_id") else None
    dealer = node.find("dealer").text if node.find("dealer") else None
    if not dealer:
        dealer = "kan-ftp.kanavto.ru"

    brand = node.find("brand").text if node.find("brand") else None
    if not brand:
        brand = node.find("mark_id").text if node.find("mark_id") else None
    images = node.find("images").iter("image") if node.find("images") else None
    if not images:
        images = node.find("photos").iter("photo") if node.find("photos") else None

    img_objects = []
    path = settings.MEDIA_ROOT
    if images:
        for i in images:
            res = requests.get(i.text)
            f_name = i.text.split("/")[-1]
            # if res.status_code == 200:
            # with open(path / f_name, "wb") as f:
            #     shutil.copyfileobj(res.raw, f)
            # img_name = i.text.split("/")[-1]
            new_img, status = CarImage.objects.update_or_create(url=i.text)
            img_temp = NamedTemporaryFile(delete=True)

            fd = check_and_resize(res.content)

            img_temp.write(fd)
            img_temp.flush()

            new_img.photo.save(f_name.split("?")[0], File(img_temp), save=True)
            img_objects.append(new_img)
    # if not brand:
    #     brand = node.find("mark_id").text if node.find("mark_id") else None
    return vin, id, price, model, dealer, brand, img_objects


def get_data(request_url):
    r = requests.get(request_url)
    root = ET.fromstring(r.content)
    tag = "car" if root[0].tag == "cars" else "vehicle"
    nodes = list(root.iter(tag))
    # root.findall(root[0].tag)
    for node in nodes:
        vin, id, price, model, dealer, brand, img_objects = find_data(node)
        car_data = {
            "name": vin,
            "instance_id": id,
            "price": price,
            "model": model,
            "dc": dealer,
            "brand": brand,
            "photos": img_objects,
        }
        car_data["integration_url"] = request_url

        save_data_to_model(car_data)
    return 200
