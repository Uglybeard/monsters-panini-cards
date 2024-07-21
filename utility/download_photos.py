import requests

with open("cards.txt", 'r') as file:
    cards = file.read()
    cards = cards.split("\n")
    del cards[190]
    print(cards)
    

for url in cards:
    response = requests.get(url)
    name=url.split("/")
    name=name[6].lower()
    if response.status_code == 200:
        with open("../images/"+name, 'wb') as f:
            f.write(response.content)