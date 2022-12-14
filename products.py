# id | name | description | price | photo | memory | color |brand | call_back | url
from db import conn, cursor
import urllib.request
from PIL import Image
from telebot import types
import telebot

def create_table_product():
    query = """
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name VARCHAR,
            description TEXT,
            price INT,
            photo VARCHAR,
            memory VARCHAR,
            color VARCHAR,
            brand VARCHAR,
            call_back VARCHAR,
            url VARCHAR);"""
    cursor.execute(query=query)
    conn.commit()
    
def insert_product(name: str, 
                  description: str, 
                  price: int, 
                  photo: str, 
                  memory: str,
                  color: str, 
                  brand: str, 
                  call_back: str,
                  url: str):
    query = f"""
        INSERT INTO products (
            name, description, price, photo, memory, color, brand, call_back, url
        )VALUES (
            '{name}', '{description}', {price}, '{photo}', '{memory}', '{color}', '{brand}', '{call_back}', '{url}'
        );"""
    cursor.execute(query=query)
    conn.commit()


def get_brands():
    query = """
        SELECT count(brand), brand
        FROM products
        GROUP BY brand;"""
    cursor.execute(query=query)
    response = cursor.fetchall()
    return {i[1]: i[1].title() for i in response}


def get_phone_callbacks(brand: str = None):
    if brand is None:
        query = f"""
            SELECT call_back 
            FROM products;""" 
    else:
        query = f"""
            SELECT call_back 
            FROM products
            where brand = '{brand}';""" 
    
    cursor.execute(query=query)
    response = cursor.fetchall()
    return {i[0]: i[0].title().replace('_', ' ') for i in response}

def get_info_phone(call_back: str):
    query = f"""
        SELECT * 
        FROM products
        where call_back = '{call_back}';"""

    cursor.execute(query=query)
    response = cursor.fetchall()
    return response


def get_product_image(image_url):
    urllib.request.urlretrieve(image_url, "gfg.png")
    image = Image.open("gfg.png")
    return image

# id | name | description | price | photo | memory | color | brand | call_back | url

def send_phone(call,  bot: telebot.TeleBot, phone: tuple):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('???????????????? ?? ??????????????', callback_data=phone[0])
    item2 = types.InlineKeyboardButton('???????????? ????????????????????', url=phone[9])
    markup.add(item1,item2)
    image = get_product_image(phone[4])
    text = f"""
??????????????: {phone[1]}{phone[5]}
????????: {phone[6].title()}
????????: {phone[3]} ???
????????????????: {phone[2]}
"""
    bot.send_photo(
            chat_id=call.message.chat.id,
            photo=image,
            caption=text,
            reply_markup=markup)


# from pprint import pprint

# pprint(get_info_phone(call_back='apple_iphone_11'))