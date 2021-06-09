import requests
import json
from config import keys

class ConvertionException(Exception):
    pass



class CryptoConvertor:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_tiket = keys[quote]
        except KeyError:
            raise ConvertionException(f'Неудалось обработать валюту {quote}')

        try:
            base_tiket = keys[base]
        except KeyError:
            raise ConvertionException(f'Неудалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Неудалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_tiket}&tsyms={base_tiket}')
        total_base = json.loads(r.content)[keys[base]]*amount

        return total_base
