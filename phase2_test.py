from phase2 import checkout
from shopping_cart_objects import Cart_Item


def test_shoppincart_1():
    item1 = Cart_Item("FR1", 7)
    item2 = Cart_Item("SR1", 4)
    item3 = Cart_Item("ST1", 1)
    item4 = Cart_Item("CF1", 1)
    item5 = Cart_Item("DT1", 1)
    list = [item1, item2, item3, item4, item5]
    cost = checkout(list)

    assert cost == 53.47



def test_shoppincart_2_no_discount():
    itemA = Cart_Item("CF1", 1)
    itemB = Cart_Item("DT1", 2)
    list = [itemA, itemB]
    cost = checkout(list)

    assert cost == 26.23

def test_shoppincart_3_with_discount():
    item1=Cart_Item("FR1", 7)
    item2=Cart_Item("SR1", 4)
    list = [item1, item2]
    cost = checkout(list)

    assert cost == 30.44

def test_shoppincart_4_only_FR1_discount():
    x=Cart_Item("FR1", 6)

    list = [x]
    cost = checkout(list)

    assert cost == 30.44

def test_shoppincart__only_SR1_discount():
    item=Cart_Item("SR1", 4)
    list = [item]
    cost = checkout(list)

    assert cost == 30.44

def test_anything():
    item = Cart_Item("FR1", 6)

    list = [item]

    assert checkout(list) == 9.33
