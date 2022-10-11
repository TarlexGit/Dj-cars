from urllib import request
import requests  # for using API
import xml.etree.ElementTree as ET  # for parsing XML
import numpy as np  # for using pandas
import pandas as pd  # for using dataframes
from .save_objects import save_data_to_model


def get_data(request_url):
    r = requests.get(request_url)
    root = ET.fromstring(r.content)
    df_cols = ["price", "dealer", "model", "vin"]

    # rows = []
    for node in root.findall(root[0].tag):
        vin = node.find("vin").text
        id = node.find("id").text
        price = node.find("price").text
        model = node.find("model").text
        if not model:
            model = node.find("folder_id")
        dealer = node.find("dealer").text
        brand = node.find("brand").text
        # rows.append({"price": price, "dealer": dealer, "model": model, "vin": vin})
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
    # out_df = pd.DataFrame(rows, columns=df_cols)
    return 200
