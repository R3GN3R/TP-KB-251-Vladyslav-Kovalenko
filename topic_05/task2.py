import requests

def convert():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException:
        print("Помилка з'єднання з API НБУ.")
        return

    rates = {}
    for item in data:
        if item ['cc'] in ['USD', 'EUR', 'PNL']:
            rates[item['cc']] = item['rate']

    currency = input("Введіть тип валюти (USD, EUR, PLN): ").upper()
    if currency not in rates:
        print("Помилка: валюта не підтримується. Виберіть USD, EUR або PLN.")
        return
    try:
        amount = float(input(f"Введіть кількість {currency}:"))
    except ValueError:
        print("Помилка: введено не числове значення.")
        return
    result = amount * rates[currency]
    print(f"{amount} {currency} = {result:.2f} UAH за курсом НБУ")

convert()