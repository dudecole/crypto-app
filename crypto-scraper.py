import requests
import time
from bs4 import BeautifulSoup as bs
import lxml

#a = 1
#while a != 0:
my_list = ["hello","what","is","your","name"]
print("here is my list: {}".format(my_list))
    
r = requests.get('https://www.coinbase.com/price/ripple')
print(r.status_code)
#print(r.text)
ugly_soup = bs(r.text, 'html.parser')
print(ugly_soup.prettify())

file = open("ugly-soup.html", "w")
file.write(str(ugly_soup))
file.close()



#    time.sleep(100)
