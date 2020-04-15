from datetime import datetime
from freezegun import freeze_time
from app.shopping_cart import to_usd, tax, find_product

def test_to_usd():
    result = to_usd(3.47)
    assert result == f"${3.47:,.2f}"

def test_tax():
    result= tax(40)
    assert result == 3.5

#taken from https://pypi.org/project/freezegun/
@freeze_time("2012-01-14")
def test_time():
    result = datetime.now()
    assert result == datetime(2012, 1, 14)

def test_find_product():
    
    products = [
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    ]
    selected_ids = []
    selected_id = 3  
    selected_ids.append(selected_id)
    total_price = 0
    for i in selected_ids:
        result = find_product(i, total_price, products,selected_id)
    
    assert result == 2.49


