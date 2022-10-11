from urllib import request
import requests
import xml.etree.ElementTree as ET
from .save_objects import save_data_to_model


def find_data(node):
    vin = node.find("vin").text
    # try:
    id = node.find("id").text if node.find("id") else None
    # except:
    #     id = None
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

    return vin, id, price, model, dealer, brand


def get_data(request_url):
    r = requests.get(request_url)
    root = ET.fromstring(r.content)
    tag = "car" if root[0].tag == "cars" else "vehicle"
    nodes = list(root.iter(tag))
    # root.findall(root[0].tag)
    for node in nodes:
        vin, id, price, model, dealer, brand = find_data(node)
        car_data = {
            "name": vin,
            "instance_id": id,
            "price": price,
            "model": model,
            "dc": dealer,
            "brand": brand,
        }
        car_data["integration_url"] = request_url

        save_data_to_model(car_data)
    return 200
