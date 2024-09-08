import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'

def test_status_code():
    response = requests.get(f'{URL}/trainers')
    assert response.status_code == 200

def test_itsme():
    response_itsme = requests.get(f'{URL}/trainers', params={'trainer_id': '5848'})
    assert response_itsme.json()['data'][0]['trainer_name'] == "МАШИНИСТ"