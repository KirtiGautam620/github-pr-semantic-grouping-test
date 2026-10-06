from billing.invoice import create_invoice

def test_create_invoice():
    invoice = create_invoice(100)
    assert invoice["amount"] == 100