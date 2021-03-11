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
        print(" ")      # after call to _in_order(), print new line

    def _in_order(self, curr):
        # go all the way to left most node recursively (print left, root, right)
        if curr:
            self._in_order(curr.left_child)     # recursively print left
            print(curr.data, end=" ")           # root // middle
            self._in_order(curr.right_child)    # recursively print right


    def pre_order(self):
        '''root, left, right'''
        self._pre_order(self.root)
        print(" ")

    def _pre_order(self, curr):
        if curr:
            print(curr.data, end=" ")           # root
            self._pre_order(curr.left_child)     # print left
            self._pre_order(curr.right_child)    # right

    def post_order(self):
        '''left, right, root'''
        self._post_order(self.root)
        print(" ")

    def _post_order(self, curr):
        if curr:
            self._post_order(curr.left_child)
            self._post_order(curr.right_child)
            print(curr.data, end=" ")

    # O(h) - average, O(log n) - in balanced BST
    def find_val(self, key):
        return self._find_val(self.root, key)

    def _find_val(self, curr, key):
        if curr:
            # base case
            if key == curr.data:
                return "Value found in tree"
            # traverse left
            elif key < curr.data:
                return self._find_val(curr.left_child, key)
            else:
                return self._find_val(curr.right_child, key)
        return "Value not found in tree"

    # 3 Cases:
    #     - deleting a leaf Node
    #     - deleting node with only 1 child
    #     - delete node with 2 children
    def delete_val(self, key):
        self._delete_val(self.root, None, None, key)

    def _delete_val(self, curr, prev, is_left, key):
        if curr:
            # ************* Delete leaf node *************
            if key == curr.data:
                if is_left:
                    prev.left_child = None
                else:
                    prev.right_child = None
            # if key is less than current, search left 
            elif key < curr.data:
                self._delete_val(curr.left_child, curr, True, key)
            # else search for key in right subtree
            elif key > curr.data:
                self._delete_val(curr.right_child, curr, False, key)
            # ************* Delete leaf node *************
        else:
            print(f"{key} not found in Tree")

tree = BSTDemo()
tree.insert("F")
tree.insert("C")
tree.insert("G")
tree.insert("A")
tree.insert("B")
tree.insert("K")
tree.insert("H")

# print(tree.find_val("A"))
# tree.delete_val("K")
tree.in_order()
tree.post_order()
tree.pre_order()