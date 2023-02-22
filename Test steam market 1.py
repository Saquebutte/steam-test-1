import time
import requests

item_id = 'AK-Thodik vie de neon vert'
appid=1575870
market_hash_name='Green%20neon%20life%20AK-Thodik'
asktime=int(input("How many sec do you awnt between each attempts : "))

url = f'https://steamcommunity.com/market/pricehistory/?appid={appid}&market_hash_name={market_hash_name}'
print(url)
previous_price = None
response = requests.get(url)
print(response)

if item_id in response.text:
    print(f"The item {item_id} was found on the market !")
else:
    print(f"The item {item_id} wasn't found on the market !")
    exit()

while True:
    response = requests.get(url)

    if response.status_code == 200:
        item_data = response.json()
        current_price = item_data['prices'][0][1]
        print(f"The actual price of {item_id} is : {current_price}")

        if previous_price is not None and current_price < previous_price:
            print(f'{item_id} price is lower ! The new price is : {current_price}')
        previous_price = current_price

    time.sleep(asktime)
