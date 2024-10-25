# Sample exchange rates to USD (base currency)
exchange_rates = {
    "RWF": 0.00084,  # 1 RWF = 0.00084 USD
    "USD": 1.0,      # 1 USD = 1.0 USD
    "EUR": 1.06,     # 1 EUR = 1.06 USD
    "KSH": 0.0068,   # 1 KSH = 0.0068 USD
    "UGSH": 0.00027  # 1 UGSH = 0.00027 USD
}

def convert(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        raise ValueError(f"Invalid currency: {from_currency} or {to_currency}")

    # Convert from `from_currency` to USD, then from USD to `to_currency`
    usd_value = amount / exchange_rates[from_currency]
    converted_value = usd_value * exchange_rates[to_currency]
    return round(converted_value, 2)
