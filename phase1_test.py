from phase1 import checkout
from shopping_cart_objects import Cart_Item

def test_simple_1():

    item1=Cart_Item("FR1", 6)
    item2=Cart_Item("SR1", 1)
    list = [item1, item2]

    assert checkout(list) == 14.33

def test_simple_2():
    item1=Cart_Item("FR1", 7)
    item2=Cart_Item("SR1", 4)
    list = [item1, item2]

    assert checkout(list)== 30.44