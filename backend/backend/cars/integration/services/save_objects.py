from main.models import Car, DealerCenter, Brand, CarModel

# from .check_image import


def save_data_to_model(data):
    try:
        dc = DealerCenter.objects.filter(name=data["dc"])
        if len(dc) > 0:
            del data["dc"]
            data["dc"] = dc[0]
        else:
            data["dc"] = DealerCenter.objects.create(name=data["dc"])

        if data["model"]:
            models = CarModel.objects.filter(name=data["model"])
            if len(models) > 0:
                data["model"] = models[0]
            else:
                data["model"] = CarModel.objects.create(name=data["model"])
        if "brand" in data and data["brand"]:
            brands = Brand.objects.filter(name=data["brand"])
            if len(brands) > 0:
                data["brand"] = brands[0]
            else:
                data["brand"] = Brand.objects.create(name=data["brand"])

        imgs = data["photos"]
        del data["photos"]

        new_car, status = Car.objects.update_or_create(**data)
        if status and imgs:
            for img in imgs:
                new_car.photos.add(img)

    except Exception as err:
        # TODO add logging
        print(str(err))
