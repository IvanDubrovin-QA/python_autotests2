import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '18dbc78ad378758a5fbb96edbcd4a6ba'
HEADER = {'Content-Type' : 'application/json','trainer_token' : TOKEN}
body = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_change_name = {
    "pokemon_id": "43345",
    "name": "New Name",
    "photo_id": 1
}

body_add_pokeball = {
    "pokemon_id": "43345"
}

'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body)
print(response.text)'''

'''response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response.text)'''

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response.text)