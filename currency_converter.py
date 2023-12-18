from forex_python.converter import CurrencyRates

def currency_converter(amount, from_currency, to_currency):
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)
    return converted_amount

# Example usage:
amount_to_convert = 100  # Change this to the amount you want to convert
from_currency_code = 'USD'  # Change this to the currency you have
to_currency_code = 'ZAR'  # Change this to the currency you want to convert to

result = currency_converter(amount_to_convert, from_currency_code, to_currency_code)
print(f"{amount_to_convert} {from_currency_code} is equal to {result} {to_currency_code}")
