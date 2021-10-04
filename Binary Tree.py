class Node:
    """Class to represent a node in Python3"""

    def __init__(self, data):
        self.data = data  # Node value
        self.left = None  # Left node
        self.right = None  # Right node


class BinaryTree:
    """Class to represent a binary tree in Python3"""

    def __init__(self):
        self._root = None  # The root of tree
        self._nodes = 0  # Number of nodes

    def returnNode(self, current):
        """Auxiliary method that return the node to be relocated"""
        if current.left == None:
            node2 = current.right
            return node2
        node1 = current
        node2 = current.left
        while node2.right != None:
            node1 = node2
            node2 = node2.right
        if node1 != current:
            node1.right = node2.left
            node2.left = current.left
        node2.right = current.right
        return node2

    def insert(self, value):
        """Inserts a node by your value"""
        if self._root is None:
            self._root = Node(value)
            self._nodes += 1
        else:
            pointer = self._root
            while True:
                if pointer.data > value:
                    if pointer.left is None:
                        break
                    pointer = pointer.left
                elif pointer.data < value:
                    if pointer.right is None:
                        break
                    pointer = pointer.right
                else:
                    raise Exception("The node already exists")
            node = pointer
            if node.data > value:
                node.left = Node(value)
                self._nodes += 1
            else:
                node.right = Node(value)
                self._nodes += 1

    def remove(self, value):
        """Removes a node and regroup the tree"""
        prev = None
        current = self._root
        while current != None:
            if value == current.data:
                if current == self._root:
                    self._root = self.returnNode(current)
                else:
                    if prev.right == current:
                        prev.right = self.returnNode(current)
                    else:
                        prev.left = self.returnNode(current)
            prev = current
            if value > current.data:
                current = current.right
            else:
                current = current.left
        self._nodes -= 1

    def preOrder(self, node):
        """Prints the tree: root -> left node -> right node"""
        if self._root is None:
            raise Exception("The tree is empty")
        if node != None:
            print(node.data)
            self.preOrder(node.left)
            self.preOrder(node.right)

    def order(self, node):
        """Prints the tree: left node -> root -> right node"""
        if self._root is None:
            raise Exception("The tree is empty")
        if node != None:
            self.order(node.left)
            print(node.data)
            self.order(node.right)

    def postOrder(self, node):
        """Prints the tree: left node -> right node -> root"""
        if self._root is None:
            raise Exception("The tree is empty")
        if node != None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.data)

    def search(self, value):
        """Returns true if the value is in the tree, otherwise, it returns false"""
        if self._root is None:
            raise Exception("The tree is empty")
        pointer = self._root
        while True:
            if pointer.data > value:
                if pointer.left is None:
                    return False
                pointer = pointer.left
            elif pointer.data < value:
                if pointer.right is None:
                    return False
                pointer = pointer.right
            else:
                return True

    def min(self, node=None):
        """Returns the lowest value in the tree or subtree"""
        if node is None:
            pointer = self._root
            if self._root is None:
                raise Exception("The tree is empty")
        while pointer.left:
            pointer = pointer.left
        print(pointer.data)

    def max(self, node=None):
        """Returns the lowest value in the tree or subtree"""
        if node is None:
            pointer = self._root
            if self._root is None:
                raise Exception("The tree is empty")
        while pointer.right:
            pointer = pointer.right
        print(pointer.data)

    def clear(self):
        """Restores the tree to its starting point (Empty)"""
        self._root = None
        self._nodes = 0

    def height(self, node):
        """Returns the tree's height"""
        if self._root is None:
            raise Exception("The tree is empty")
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            if (left_height > right_height):
                return left_height + 1
            else:
                return right_height + 1

    def nodes(self):
        """Returns the number of nodes in the tree"""
        return self._nodes

    def root(self):
        """Returns the tree's root node"""
        return self._root

    def empty(self):
        """Returns true if the tree is empty, otherwise, it returns false"""
        if self._root is None:
            return True
        return False
    
    def printTree(self, node=None):
        """Prints the Avl Tree"""
        if node is None:
            node = self._root
        lines, *_ = self._printTree(node)
        for line in lines:
            print(line)

    def _printTree(self, node):
        """Auxiliary function to print the Avl Tree"""
        if node.right is None and node.left is None:  # No child
            line = '%s' % node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if node.right is None:  # Only left child
            lines, n, p, x = self._printTree(node.left)
            s = '%s' % node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if node.left is None:  # Only right child
            lines, n, p, x = self._printTree(node.right)
            s = '%s' % node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._printTree(node.left)  # Two children
        right, m, q, y = self._printTree(node.right)
        s = '%s' % node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
