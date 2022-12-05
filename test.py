import urllib.request
from PIL import Image
import ssl

# This restores the same behavior as before.
context = ssl._create_unverified_context()


def get_product_image(image_url):
    urllib.request.urlretrieve(image_url, "gfg.png")
    image = Image.open("gfg.png")
    return image

image_url = 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h62/he1/52289124302878/xiaomi-redmi-10a-3-gb-64-gb-seryi-grafit-105711712-1.jpg'

get_product_image(image_url)