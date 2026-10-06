def create_invoice(amount):
    tax = amount * 0.18
    return {"amount": amount, "tax": tax}