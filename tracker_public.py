#!/usr/bin/python3
import smtplib
import json
from lxml import html
import requests
import time
import os



class TrackerEmailAlert:

    """
        Send mail using MailGun SMTP protocol. 
    """


    def __init__(self, message):

        print(200)
        smtp = smtplib.SMTP("smtp.mailgun.org", 587)
        smtp.login("your SMTP credentials",  # They can be found and created under Domain settings on your Mailgun.com account
                   "SMPT password")          # SMTP credentials password
        smtp.sendmail("price.tracker.alert2021@example.com", "recipient@gmail.com",  message) # smtp.sendmail( from, to, text)

        # !Note: for sandbox domain recipient must be added and verified on domain page of MailGun.com




class Tracker:

    """ 
        Scrape data from site, extract key parts, compare their validity by price and then save tem to file and email them to recipient.
        If data is not valid only email with null match will be sent to recipient.
    """


    def __init__(self, links,):

        self.link = links[0]
        self.target_price = links[1]


    def run(self):

        return self.resolve_data(self.check_price(self.get_price(self.link)))


    def get_price(self, url):   #scrape price and title

        get_data = requests.get(url)
        print(get_data)
        time.sleep(1)
        if get_data:
            data_get = html.fromstring(get_data.content)
            data_product = data_get.xpath('//div[@id="productright"]//h1/text()')
            data_price = data_get.xpath('//div[@class="productpageprice"]//span/text()')
            data_price = data_price[0].replace("\xa0", ' ') # Clear non ascii for mailgun
            data_price_low = data_get.xpath('//span[@class="success"]/text()')
            data_price_low = data_price_low[0].replace("\xa0", '') # Clear non ascii for mailgun
            if data_product and data_price and data_price_low:   
                 data = [data_product[0], data_price, data_price_low]
                 return data
        return False


    def check_price(self, list):   #check target and current price difference
        
        if list:
            serial = list[2].split(",")
            serial = serial[0].replace(".", "")            
            if int(serial) <= int(self.target_price):
                return list
        return False


    def resolve_data(self, list):  # If match were made create file, if new data in match is same as data in file, do nothing, else update.

        if not os.path.exists("/home/user/price_tracker/price_tracker.html"):
            os.mknod("/home/user/price_tracker/price_tracker.html")

        if list:
            file = open("/home/user/price_tracker/price_tracker.html", "r+")
            read = file.read()
            data = str(read).split("<hr>")

            for i in range(len(data)) or range(1):
                if list[0] in data[i] and list[2] in data[i]:
                    return False
            # "Cijena" is just Croatian word for Price
            data =  "{0} \n CIJENA {1} \n CIJENA S POPUSTOM {2} \n {3} \n ".format(list[0], list[1], list[2], self.link)
            file.write("".join(data))
            file.close()
            return data
        return False




# Target items to check [url, price]
products = [
    ["https://www.instar-informatika.hr/mobitel-apple-iphone-11-64gb-red/INS%2D53036/product/", 10000],
    ["https://www.instar-informatika.hr/mobitel-apple-iphone-se-2020-64gb-crni/INS%2D51630/product/", 10000],
    
    ]
# Holder for data to be mailed    
results = ["Price Tracker ALERT \n\n"]

# Traverse products and check them with Tracker
match = False
for i in products:
    main = Tracker([i[0], i[1]])
    status = main.run()
    if status:
        results[0] = results[0] + "\n\n" + status
        match = True

if match:
    mail = TrackerEmailAlert(results[0])
else:
    mail = TrackerEmailAlert("Price Tracker NULL \n\n Tracker found no matches, but is still ACTIVE and running.")

print("All Done.")
    
    



  
