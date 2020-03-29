import requests
import time
from bs4 import BeautifulSoup as bs
# import lxml
import pprint as p
import json

#a = 1
#while a != 0:
my_list = ["hello","what","is","your","name"]
print("here is my list: {}".format(my_list))
    
r = requests.get('https://www.coinbase.com/price/ripple')
print(r.status_code)
#print(r.text)
ugly_soup = bs(r.text, 'html.parser')

script_tag = ugly_soup.find("script", {"id":"server-app-state", "type":"application/json"})
# print(script_tag)
json_tag = script_tag.contents[0]
# p.pprint(json_tag, indent=5)
json_dict = json.loads(json_tag)

print(json.dumps(json_dict["initialData"]["data"]["asset"], sort_keys=True, indent=4))
# json_dict = json.loads(json_tag)

# latest price - as a json string
print(json.dumps(json_dict["initialData"]["data"]["asset"]["latest"]))

# acronym of the asset - as a json string
print(json.dumps(json_dict["initialData"]["data"]["asset"]["symbol"]))


file = open("ugly-soup.html", "w")
file.write(str(ugly_soup.prettify()))
file.close()

# "tradingActivity":{"value":0.651166

#    time.sleep(100)
