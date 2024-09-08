import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'СЕКРЕТ, У ВАС СВОЙ ДОЛЖЕН БЫТЬ'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_create = {
    "name": "generate",
    "photo_id": -1
}
response_create = requests.post(url =f'{URL}/pokemons', headers = HEADER, json = body_create)
print (response_create.json)

Pokemon_ID = response_create.json()["id"]

body_namechange = {
    "pokemon_id": Pokemon_ID,
    "name": "generate",
    "photo_id": -1
}

response_namechange = requests.put(url =f'{URL}/pokemons', headers = HEADER, json = body_namechange)
print (response_namechange.json)

body_pokeball = {
    "pokemon_id": Pokemon_ID
}
response_pokeball = requests.post(url =f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print (response_pokeball.json) 