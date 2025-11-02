import requests
from bs4 import BeautifulSoup
import json

product_Site=requests.get('https://www.entekhabcenter.com/product-category/product/audio-video/television')
page_Soup=BeautifulSoup(product_Site.content,'html.parser')
product_Names=page_Soup.select('a>h5')
product_Prices= page_Soup.select("div>ins")

def getNames(soup):

    namesList=[]
    for name in soup:
        namesList.append(name.text)
    return namesList

def getPrices(soup):

    pricesList=[]
    for price in soup:
        pricesList.append(price.text)
    return pricesList


def getProducts():

    productsList=list(zip(getNames(product_Names),getPrices(product_Prices)))
    products=[]
    for product in productsList:
        products.append({'Product_Name':product[0],'Product_Price':product[1]})
    
    with open("products.json", "w", encoding='utf8') as json_file:
        json.dump(products, json_file, indent=4, ensure_ascii=False)


getProducts()