import requests


def Get(coin1 , coin2 , API) -> dict:
    response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={coin1}&tsyms={coin2}&api_key={API}').json()
    return response
