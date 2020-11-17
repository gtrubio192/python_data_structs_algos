class Node:
    def __init__(self, key):
        self.data = key
        self.left_child = None
        self.right_child = None

class BSTDemo:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        # if Empty tree
        if self.root == None:
            self.root = key
        # else, use private method
        else:
            self._insert(self.root, key)

    # "_xyz() " functions are said to be private functions 
    def _insert(self, curr, key):
        # deal with inserting on right
        if key.data > curr.data:
            if curr.right_child == None:
                curr.right_child = key
            else:
                self._insert(curr.right_child, key)
        # deal with inserting on left
        elif key.data < curr.data:
            if curr.left_child == None:
                curr.left_child = key
            else:
                self._insert(curr.left_child, key)

    # print left, root, then right node
    def in_order(self):
        self._in_order(self.root)
        print(" ")

    def _in_order(self, curr):
        # go all the way to left most node recursively (print left, root, right)
        if curr:
            self._in_order(curr.left_child)
            print(curr.data, end=" ")
            self._in_order(curr.right_child)


    def pre_order(self):
        '''root, left, right'''
        pass

    def _pre_order(self, curr):
        pass

    def post_order(self):
        '''left, right, root'''
        pass

    def _post_order(self, curr):
        pass

    def find_val(self, key):
        pass

    def _find_val(self, curr, key):
        pass

    def delete_val(self, key):
        pass

    def _delete_val(self, curr, prev, is_left, key):
        pass

tree = BSTDemo()
tree.insert("F")
tree.insert("C")
tree.insert("G")
tree.insert("A")
tree.insert("B")
tree.insert("K")
tree.insert("H")
tree.in_order()
