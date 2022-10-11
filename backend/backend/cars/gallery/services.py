import requests
from django.core.files import File
import os


def save_picture(image_url):
    # http://kan-ftp.kanavto.ru/newavto/1(3)XUFPE6DC2D3018700.jpg
    filename = image_url.split("/")[-1]
    img_data = requests.get(image_url).content
    with open(filename, "wb") as handler:
        handler.write(img_data)
