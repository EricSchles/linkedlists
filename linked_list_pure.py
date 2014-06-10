class Node:
    def __init__(self,item=None,prev=None):
        self.item = item
        self.next = next
        self.prev = prev
    def __str__(self):
        return str(self.item)

class CollectionTypeError(Exception):
    def __init__(self,msg=''):
        self.msg = "Wrong type for passed in collection, please use list"
    def __str__(self):
        return repr(self.msg)
        
        
class LinkedList:
    """
    Optionally takes in a list.
    """
    def __init__(self,collection=[]):
        try:
            if type(collection) != type(list()):
                raise CollectionTypeError
            else:
                pass
        except CollectionTypeError as col:
            print col

        if collection == []:
            self.length = 0
            self.head = Node()
            self.head.next = None
            self.head.prev = None
        elif len(collection) < 3:
            self.length = len(collection)
            self.head = Node(collection[0])
            curr = Node(collection[1])
            curr.prev = self.head
            curr.next = None
            self.head.next = curr
        else:
            self.length = len(collection)
            self.head = Node(collection[0])
            self.head.next = None
            curr = Node(collection[1])
            curr.prev = self.head
            curr.next = None
            self.head.next = curr
            prev = curr
            for item in collection[2:]:
                curr = Node(item)
                curr.prev = prev
                prev.next = curr
                curr.next = None
                prev = curr
                
    def print_backwards(self):
        curr = self.head
        while curr.next:
            curr = curr.next
        while curr:
            print curr,
            curr = curr.prev
        print
        
    def pretty_print(self):
        curr = self.head
        while curr:
            print curr,
            curr = curr.next
        print
    def add_first(self,item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
        new_node.next = self.head
        self.head = new_node
        new_node.prev = None
        self.length += 1

    def add_last(self,item):
        curr = self.head
        while curr.next != None:
            curr = curr.next
        new_node = Node(item)
        curr.next = new_node
        new_node.prev = curr
        new_node.next = None
        self.length += 1
        
    def add_at(self,item,location):
        curr = self.head
        prev = None
        count = 0
        if location < self.length:
            while (curr != None) and (count < location):
                curr.next = curr
                count += 1
            new_item = Node(item)
            next_node = curr
            curr = curr.prev
            #curr.next = new_item
            new_item.next = next_node
            self.length += 1
        else:
            raise Exception("location out of range")
