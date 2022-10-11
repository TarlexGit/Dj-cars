import requests  # for using API
import xml.etree.ElementTree as ET  # for parsing XML
import numpy as np  # for using pandas
import pandas as pd  # for using dataframes


def get_data(request_url):
    r = requests.get(
        "http://export.maxposter.ru/legocar-used-all/3073-15554.xml"
    )  # call API
    root = ET.fromstring(r.content)
    desc_list = []
    df_cols = ["price", "dealer", "model", "vin"]

    for description in root.iter("description"):
        desc_list.append(description.text)

    properties_df = pd.DataFrame({"description": desc_list})

    properties_df.style.set_properties(
        subset=["description"], **{"width": "800px"}
    ).hide_index()
    rows = []

    for node in root.findall(root[0].tag):
        print("node =", node)
        vin = node.find("vin").text

        id = node.find("id").text
        print("vin =", vin)
        price = node.find("price").text
        model = node.find("modification_id")
        dealer = node.find("dealer").text
        rows.append({"price": price, "dealer": dealer, "model": model, "vin": vin})

    out_df = pd.DataFrame(rows, columns=df_cols)
    return out_df
