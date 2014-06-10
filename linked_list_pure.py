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
            self.head = None
        elif len(collection) == 1:
            self.length = 1
            self.head = Node(collection[0])
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
            self.head = Node(item=collection[0])
            self.head.next = None
            curr = Node(item=collection[1])
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
            self.head.item = new_node.item
            self.head.next = None
            self.head.prev = None
        else:    
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None
        self.length += 1
        

    def add_last(self,item):
        if self.length == 0:
            self.add_first(item)
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            new_node = Node(item)
            new_node.prev = curr
            curr.next = new_node
            new_node.next = None
            self.length += 1
        
    def add_at(self,item,location):
        if location == 0:
            self.add_first(item)
        else:    
            curr = self.head
            count = 0
            if location < self.length:
                while (curr != None) and (count < location):
                    curr = curr.next
                    count += 1
                new_node = Node(item)
                curr.prev.next = new_node
                new_node.next = curr
                self.length += 1
            else:
                raise Exception("location out of range")

    def contains(self,val):
        curr = self.head
        while curr != None:
            if curr.item == val:
                return True
            curr = curr.next
        return False

    def at_index(self,val):
        curr = self.head
        ind = 0
        while curr != None:
            if curr.item == val:
                return ind
            ind += 1
            curr = curr.next
            
        return False


