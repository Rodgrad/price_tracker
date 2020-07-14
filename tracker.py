#!/usr/bin/python3

import json
from lxml import html
import requests
import time
import os

class Tracker:
    
    def __init__(self, links,):
        self.link = links[0]
        self.target_price = links[1]


    def run(self):

        if not os.path.exists("/home/luka/price_tracker/price_tracker.html"):
            os.mknod("/home/luka/price_tracker/price_tracker.html")
            
        return self.resolve_data(self.check_price(self.get_price(self.link)))


    def get_price(self, url):

        get_data = requests.get(url)
        print(get_data)
        time.sleep(1)
        if get_data:
            data_get = html.fromstring(get_data.content)
            data_product = data_get.xpath('//div[@id="productright"]//h1/text()')
            data_price = data_get.xpath('//div[@class="productpageprice"]//span/text()')
            data_price_low = data_get.xpath('//span[@class="success"]/text()')

            if data_product and data_price and data_price_low:   
                 data = [data_product[0], data_price[0], data_price_low[0]]
                 return data
        return False


    def check_price(self, list):   #check new and old price difference
        
        if list:
            serial = list[2].split(",")
            serial = serial[0].replace(".", "")            
            if int(serial) <= int(self.target_price):
                return list
        return False


    def resolve_data(self, list):

        if list:
            file = open("/home/luka/price_tracker/price_tracker.html", "r+")
            read = file.read()
            data = str(read).split("<hr>")

            for i in range(len(data)) or range(1):
                if list[0] in data[i] and list[2] in data[i]:
                    return False
                
            data = str("""<div><br> <a href='{0}'>{1}</a> <br> CIJENA {2} 
            <br> CIJENA S POPUSTOM {3} <br></div><hr>""".format(self.link, list[0] or 
            "Product", list[1] or "Product", list[2] or "Product" ))
            file.write("".join(data))
            file.close()
            return data
        return False



products = [
    ["https://www.instar-informatika.hr/mobitel-apple-iphone-11-64gb-red/INS%2D53036/product/", 10000],
    ["https://www.instar-informatika.hr/mobitel-apple-iphone-se-2020-64gb-crni/INS%2D51630/product/", 10000],
    
    ]

for i in products:
  main = Tracker([i[0], i[1]])
  print(main.run())
