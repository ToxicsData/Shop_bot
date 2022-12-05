from bs4 import BeautifulSoup
import requests 
from config import HEADERS, URL, DOMEN, LIST_BRANDS
from products import insert_product

# id | name | description | price | photo | memory | color | brand | call_back | url


def get_html(URL, headers=HEADERS, params=' '):
    html = requests.get(URL, headers=headers, params=params)
    soup = BeautifulSoup(html.text, 'html.parser')
    return soup


def get_data(soup, brand):
    items = soup.find_all('div', class_='item-card')
    data = []
    for item in items:
        try:
            name = item.find('div', class_='item-card__info')\
                .find('a').get_text(strip=True).split()
            right_name = ''
            memory = ''
            color = name[-1]
            call_back = '_'.join(name[:3]).lower()
            for i in name[:-1]:
                if 'gb' in i.lower() or 'гб' in i.lower():
                    memory += i
                else:
                    right_name += i+' '
        except:
            right_name = None
            memory = None
            color = None
            call_back = None
        try:
            url = DOMEN + item.find('a', class_='item-card__image-wrapper').get('href')
        except:
            url = None

        try:
            price = item.find('span', class_='item-card__prices-price').get_text(strip=True).replace('₸', '').replace(' ','')
        except:
            price = 0
        local_data = get_html(url)
        img = local_data.find_all('meta')[12].get('content')
        description = local_data.find('div', class_='item__description-text').get_text(strip=True)
        
        if right_name is not None:
            data.append({
                'name': right_name,
                'description': description,
                'price': int(price),
                'photo': img,
                'memory': memory,
                'color': color,
                'brand': brand,
                'call_back': call_back,
                'url': url
            })
    
    return data  
        

def parse(LIST_BRANDS, page):
    contents = []
    for brand in LIST_BRANDS:
        for page in range(1 , page+1):
            html = get_html(URL + brand, params={'page': page})
            content = get_data(html, brand)
            contents.extend(content)
            print(f"Страница Бренд {brand} {page} готово!")
    return contents

def add_products_db(items: list[dict]):
    for item in items:
        insert_product(
            name=item['name'],
            description=item['description'],
            price=item['price'],
            photo=item['photo'],
            memory=item['memory'],
            color=item['color'],
            brand=item['brand'],
            call_back=item['call_back'],
            url=item['url'])
        print(f"{item['name']} добавлен в базу данных!")




items = parse(LIST_BRANDS, page=2)
add_products_db(items=items)
