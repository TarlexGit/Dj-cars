from PIL import Image
import io


def check_and_resize(img_file):
    image_bytes = io.BytesIO(img_file)
    img_file = Image.open(image_bytes)
    w, h = img_file.size
    if w > 2500 or h > 1500:
        max_size = (2500, 1500)

        with img_file as im:
            im.thumbnail(max_size)
            buf = io.BytesIO()
            im.save(buf, format="JPEG")
            byte_im = buf.getvalue()

            print("\n\nCHANGE IMAGE")
        return byte_im
    return image_bytes
