
from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)
    return converted_amount

amount = float(input("Enter the amount: "))
from_currency = input("Enter the currency to convert from: ")
to_currency = input("Enter the currency to convert to: ")

converted_amount = convert_currency(amount, from_currency, to_currency)
print(f"The converted amount is: {converted_amount}")