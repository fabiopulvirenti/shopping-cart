from shopping_cart_objects import Cart_Item

price_fr1 = 3.11
price_sr1 = 5.00
price_cf1 = 11.23
price_sr1_discount = 4.50


def checkout(items_list):
    total = 0

    for item in items_list:

        if "FR1" == item.code:
            # Discount no. 1
            quantity_free = int(item.quantity / 2)
            quantity_to_pay = (item.quantity - quantity_free)
            cost_item = quantity_to_pay * price_fr1

        elif "SR1" == item.code:
            if item.quantity >= 3:
                # Discount no. 2
                cost_item = item.quantity * price_sr1_discount
            else:
                cost_item = item.quantity * price_sr1

        elif "CF1" == item.code:
            # No discounts
            cost_item = item.quantity * price_cf1

        total = total + cost_item

    rounded_total = round(total, 2)
    return rounded_total


item1 = Cart_Item("FR1", 7)
item2 = Cart_Item("SR1", 1)
list = [item1, item2]
cost = checkout(list)
print("Total cost:", cost)
