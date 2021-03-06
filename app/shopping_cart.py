import datetime as dt
def tax(total):
    new= total * 0.0875
    return new


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

def to_usd(price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${price:,.2f}" #> $12,000.71

if __name__ == "__main__":

    #print(products)
    # pprint(products)

    #info capture based on: https://www.youtube.com/watch?v=3BaGb-1cIr0
    total_price = 0
    selected_ids= []
    active_ids= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    while True:
        selected_id= input("please input product identifier:")
        if selected_id== "DONE":
            break
        elif int(selected_id) in active_ids:
            selected_ids.append(selected_id)
            #print(selected_ids)
        else:
            print("indentifier not found. Please update and rescan.")
            #taken from https://thispointer.com/python-how-to-add-append-key-value-pairs-in-dictionary-using-dict-update/
            new_id= input("Input new id: ")
            new_name= input("input new name: ")
            new_department= input("input new department: ")
            new_aisle= input("input new aisle: ")
            new_price= float(input("input new price value: "))
            products.append({"id": int(new_id), "name": new_name, "department": new_department, "aisle": new_aisle, "price": new_price})
            active_ids.append(int(new_id))


    #print("Selected Product: " + matching_product["name"] + " " + str(matching_product["price"]))


    #info display/output
    #print(selected_ids)
    print("------------------------")
    print("Simple Joes Simple Shop")
    print("-----------------------")
    print("Checkout time:" ,dt.datetime.now())
    print("-----------------------")

    for selected_id in selected_ids:
        matching_products= [p for p in products if str(p["id"]) == str(selected_id)]
        matching_product= matching_products[0]
        total_price= total_price + float(matching_product["price"])
        #total_price+= float(matching_product["price"]) #Eric Hyson Code
        print(">>> " , matching_product["name"] , " " , to_usd(matching_product["price"]))

    tax_total= tax(total_price)
    Big_total= total_price + tax_total
    print("------------------------")
    print("SUBTOTAL:" + to_usd(total_price))
    print("Taxes:" + to_usd(tax_total))
    print("Total:" + to_usd(Big_total))
    print("-----------------------")
    print("Thanks for stopping into Simple Joe's")




