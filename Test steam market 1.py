import time
import requests

item_id = 'AK-Thodik vie de neon vert'
appid=1575870
market_hash_name='Green%20neon%20life%20AK-Thodik'
asktime=int(input("Indiquez le nombre de secondes entre chaque tentatives : "))

url = f'https://steamcommunity.com/market/pricehistory/?appid={appid}&market_hash_name={market_hash_name}'
print(url)
previous_price = None
response = requests.get(url)
print(response)

if item_id in response.text:
    print(f"L'objet {item_id} est trouvé sur le marché !")
else:
    print(f"L'objet {item_id} n'est pas trouvé sur le marché !")
    exit()

while True:
    response = requests.get(url)

    if response.status_code == 200:
        item_data = response.json()
        current_price = item_data['prices'][0][1]
        print(f"Prix actuel de {item_id} : {current_price}")

        if previous_price is not None and current_price < previous_price:
            print(f'Le prix de {item_id} a baissé ! Le nouveau prix est {current_price}')
        previous_price = current_price

    time.sleep(asktime)
