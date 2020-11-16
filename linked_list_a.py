class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append_val(self, x):
        '''add x to the end of the list'''
        if not isinstance(x, Node):
            x = Node(x)
        if self.head == None:
            self.head = x
        else:
            self.tail.next = x
        self.tail = x

    def __str__(self):
        # [5->4->10->1]
        to_print = ""
        curr = self.head
        while curr is not None:
            to_print += str(curr.data) + "->"
            curr = curr.next
        if to_print:
            return "[" + to_print[:-2] + "]"
        return "[]"

    def add_to_start(self, x):
        '''add x to the left of the list making it the head'''
        if not isinstance(x , Node):
            x = Node(x)
        old_head = self.head
        self.head = x
        self.head.next = old_head

    # Assume x is an int
    def search_val(self, x):
        index = 0
        current = self.head
        isNotFound = True
        while current.next != None and isNotFound:
            if current.data == x:
                isNotFound = False
            else:
                current = current.next 
                index += 1

        return index

    def remove_val_by_index(self, x):
        '''remove and return value at index x provided as parameter'''
        current = self.head
        index = 0
        # Check if head is index to be removed
        if index == x:
            self.head = current.next
            return current
        
        # Loop thru rest of list
        while current.next != None:
            if index == x:
                next = current.next
                previous.next = next
                return current
            else:
                index += 1
                previous = current
                current = current.next


    def length(self):
        '''return the length of the list, rep'd by number of nodes'''
        index = 1
        current = self.head
        while current.next != None:
            index += 1
            current = current.next

        return index

    def reverse_list_recur(self, current, previous):
        '''reverse the sequence of node pointers in the linked list'''
        # Given [1->2->3->4->5] reverse pointers [1<-2<-3<-4<-5]
        # Turning list to [5->4->3->2->1]

my_list = LinkedList()
# print(my_list)
my_list.append_val(1)
my_list.append_val(2)
my_list.append_val(3)
my_list.append_val(4)
my_list.append_val(5)
my_list.add_to_start(666)
print(my_list)
print(my_list.search_val(3))
print(my_list.length())
print(my_list.remove_val_by_index(0))
print(my_list)
