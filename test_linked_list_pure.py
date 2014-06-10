from linked_list_pure import LinkedList


def test_add_first():
    ll = LinkedList()
    ll.add_first(5)
    assert ll.contains(5) == True
    assert ll.at_index(5) == 0
    ll.add_first(6)
    assert ll.contains(6) == True
    assert ll.at_index(6) == 0

def test_add_at():
    ll = LinkedList()
    ll.add_at(5,0)
    assert ll.contains(5) == True
    assert ll.at_index(5) == 0
    ll_two = LinkedList([1,23,4,5,6,78])
    ll_two.add_at(12,0)
    assert ll_two.contains(12) == True
    assert ll_two.at_index(12) == 0
    ll_two.add_at(21,3)
    assert ll_two.contains(21) == True
    assert ll_two.at_index(21) == 3

def test_add_last():
    ll = LinkedList()
    ll.add_last(3)
    assert ll.contains(3) == True
    assert ll.at_index(3) == 0
    ll.add_last(4)
    assert ll.contains(4) == True
    assert ll.at_index(4) == 1
    ll.add_last(5)
    assert ll.contains(5)  == True
    assert ll.at_index(5) == 2
