from app.shopping_cart import to_usd, tax

def test_to_usd():
    result = to_usd(3.47)
    assert result == f"${3.47:,.2f}"

def test_tax():
    result= tax(40)
    assert result == 3.5
    
