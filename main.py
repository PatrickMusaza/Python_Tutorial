from Finance.Currency import available_currencies, currency_symbol
from Finance.Conversion import convert

# List available currencies
print("Available Currencies:", available_currencies())

# Perform a currency conversion
amount = float(input("Enter the amount to be converted to usd: "))  # Example amount
from_currency = "USD"
to_currency = input("Enter the currency to be converted to usd:")
converted_amount = convert(amount, from_currency, to_currency)
print(f"{amount} {to_currency} is equal to {converted_amount} {from_currency}.")
