import requests,json
from config import keys

class ConvertionExeption(Exception):
    pass

class ConvertCurrency:
    @staticmethod
    def convert(quote:str, amount:str, base: str):
        if quote == base:
            raise ConvertionExeption('Введена одинаковая валюта для обмена, введите запрос в правильном формате')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Введено неверное число {amount}')

        r = requests.get(f'https://v6.exchangerate-api.com/v6/e2c4c225412b745e174037ed/pair/{quote_ticker}/{base_ticker}/{amount}')
        total = json.loads(r.content)['conversion_result']
        rate = json.loads(r.content)['conversion_rate']
        date = json.loads(r.content)["time_last_update_utc"]
        return [total,rate,date]