def available_currencies():
    return ["RWF", "USD", "EUR", "KSH", "UGSH"]

def currency_symbol(currency):
    symbols = {
        "RWF": "FRw",   # Rwandan Franc symbol
        "USD": "$",     # US Dollar
        "EUR": "€",     # Euro
        "KSH": "KSh",   # Kenyan Shilling
        "UGSH": "USh"   # Ugandan Shilling
    }
    return symbols.get(currency, "Unspecified Currency")
