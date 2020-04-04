import requests
import time
from bs4 import BeautifulSoup as bs
# import lxml
import pprint as p
import json

# use this url for getting all the crypto names, and acronyms
# in order to build a url for the single crypto stats function
COINBASE_URL_ALL_CRYPTO = "https://www.coinbase.com/price/"

# use this for the single crypto statistics function
COINBASE_URL_SINGLE_CRYPTO = "https://www.coinbase.com/price/ripple"

# this wile loop was for helping the python container
# continue running like a deamon.. not a good
# production idea.
#a = 1
#while a != 0:

my_list = ["hello","what","is","your","name"]
print("here is my list: {}".format(my_list))
    
r = requests.get('https://www.coinbase.com/price/ripple')
print(r.status_code)
#print(r.text)

# creating beautiful soup object using html parsing
ugly_soup = bs(r.text, 'html.parser')

# find single instance of an html tag like:
# <script id=server-app-state type=applicatoin/json>
script_tag = ugly_soup.find("script", {"id":"server-app-state",
                                       "type":"application/json"})

# assigning the contents of the previous tag
# to json_tag as contents are in json structure type
json_tag = script_tag.contents[0]

# converting json_tag string contents
# into a dictionary
json_dict = json.loads(json_tag)

# p.pprint(json_dict["initialData"]["data"]["stats"], indent=4) #["asset"], indent=4)



# setting the crypto acronym
crypto_acronym = json_dict["initialData"]["data"]["asset"]["symbol"]
print("crypto_acronym: {}".format(crypto_acronym))


# setting activity - buying percentage
trading_activity = json_dict["initialData"]["data"]["stats"] \
                            ["signals"]["tradingActivity"]["value"]
print("Trading_activity:  {}".format(trading_activity))


# setting latest_price
latest_price = json_dict["initialData"]["data"]["asset"]["latest"]
print("latest_price: {}".format(latest_price))


# setting slug - end of the web address www.blah.bha/<slug>
slug = json_dict["initialData"]["data"] \
                ["asset"]["slug"]
print("slug: {}".format(slug))


# setting uri_scheme
uri_scheme = json_dict["initialData"]["data"] \
                      ["asset"]["uriScheme"]
print("uri_scheme: {}".format(uri_scheme))


# setting market_cap
market_cap = json_dict["initialData"]["data"] \
                      ["stats"]["marketCap"]
print("market_cap: {}".format(json_dict["initialData"]["data"] \
                                      ["stats"]["marketCap"]))


# setting unique id
id = json_dict["initialData"]["data"] \
              ["asset"]["id"]
print("id: {}".format(id))


# setting circulating_supply
circulating_supply = json_dict["initialData"]["data"] \
                              ["stats"]["circulatingSupply"]
print("circulating_supply: {}:".format(circulating_supply))


# setting total_supply
total_supply = json_dict["initialData"]["data"]["stats"] \
                        ["totalSupply"]
print("total_supply: {}:".format(total_supply))



# setting max_supply
max_supply = json_dict["initialData"]["data"]["stats"] \
                      ["maxSupply"]
print("max_supply: {}:".format(max_supply))


# setting volume
daily_volume = json_dict["initialData"]["data"]["stats"]["volume24H"]
print("daily_volume: {}".format(daily_volume))


#    time.sleep(100)
