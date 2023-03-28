from shopping_cart_objects import Cart_Item

list_of_products = {
    "FR1": 3.11,   # Fruit tea
    "SR1": 5.00,   # Strawberries
    "CF1": 11.23,  # Coffee
    "DT1": 7.50,   # Detergent
    "ST1": 4.30,   # Stilton
    "FB2": 1000.00
}

price_sr1_discount = 4.50


def checkout(items_list):
    total = 0

    for item in items_list:
        # Retrieve the price from the dictionary
        price_item = list_of_products.get(item.code)

        if "FR1" == item.code:
            # Discount no. 1
            quantity_free = int(item.quantity / 2)
            quantity_to_pay = (item.quantity - quantity_free)
            cost_item = quantity_to_pay * price_item

        elif "SR1" == item.code:
            if item.quantity >= 3:
                # Discount no. 2
                cost_item = item.quantity * price_sr1_discount
            else:
                cost_item = item.quantity * price_item

        else:
            # No discounts
            cost_item = item.quantity * price_item

        total = total + cost_item

    rounded_total = round(total, 2)
    return rounded_total

item1=Cart_Item("FR1", 7)
item2=Cart_Item("SR1", 4)
item3=Cart_Item("ST1", 1)
item4=Cart_Item("CF1", 1)
item5=Cart_Item("FB2", 1)
list = [item1, item2,item3,item4,item5]
cost = checkout(list)
print("Total cost:", cost)
