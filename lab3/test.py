# Data Structure D
# —Dis a binary search tree.
# —For every node vin the tree D,
# ∗ the size of v ́s left subtree is at most c×(the size of the subtree rooted at v),
# and
# ∗ the size of v ́s right subtree is at most c×(the size of the subtree rooted at v),
# where c, 1
# 2 <c<1, is a constant.
# —An insert operation on Dis performed just as in a standard binary search tree. For
# all the nodes xon the search path, if
# ∗ either the size of x ́s left subtree >c×(the size of the subtree rooted at x)
# ∗ or the size of x ́s right subtree >c×(the size of the subtree rooted at x)
# then the subtree rooted at xis replaced by a perfect balanced binary search tree
# containing the same keys.
# •Implementation and experiment
# —Implement such a data structure and an insert operation on it.
# —Conduct simulation experiments with a series of insertions on the data structure and
# the standard binary search tree (considering different types of inputs and different
# values of c).
import random


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self.key)

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key


class BST:
    def __init__(self):
        self.root = None

    def display(self):
        if self.root is not None:
            self.root.display()

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(key, self.root)

    def _insert(self, key, node):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(key, node.left)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(key, node.right)

    def search(self, key):
        if self.root is None:
            return None
        else:
            return self._search(key, self.root)

    def _search(self, key, node):
        if key == node.key:
            return node
        elif key < node.key and node.left is not None:
            return self._search(key, node.left)
        elif key > node.key and node.right is not None:
            return self._search(key, node.right)
        else:
            return None

    def delete(self, key):
        if self.root is None:
            return
        else:
            self._delete(key, self.root)

    def _delete(self, key, node):
        if key < node.key:
            if node.left is not None:
                self._delete(key, node.left)
        elif key > node.key:
            if node.right is not None:
                self._delete(key, node.right)
        else:
            if node.left is None and node.right is None:
                if node == self.root:
                    self.root = None
                else:
                    if node.parent.left == node:
                        node.parent.left = None
                    else:
                        node.parent.right = None
            elif node.left is None:
                if node == self.root:
                    self.root = node.right
                else:
                    if node.parent.left == node:
                        node.parent.left = node.right
                    else:
                        node.parent.right = node.right
            elif node.right is None:
                if node == self.root:
                    self.root = node.left
                else:
                    if node.parent.left == node:
                        node.parent.left = node.left
                    else:
                        node.parent.right = node.left
            else:
                successor = self.get_successor(node)
                node.key = successor.key
                self._delete(successor.key, successor)

    def get_successor(self, node):
        successor = node.right
        while successor.left is not None:
            successor = successor.left
        return successor

    def inorder(self):
        if self.root is None:
            return []
        else:
            return self._inorder(self.root)

    def _inorder(self, node):
        if node is None:
            return []
        else:
            return self._inorder(node.left) + [node.key] + self._inorder(node.right)

    def preorder(self):
        if self.root is None:
            return []
        else:
            return self._preorder(self.root)

    def _preorder(self, node):
        if node is None:
            return []
        else:
            return [node.key] + self._preorder(node.left) + self._preorder(node.right)

    def postorder(self):
        if self.root is None:
            return []
        else:
            return self._postorder(self.root)

    def _postorder(self, node):
        if node is None:
            return []
        else:
            return self._postorder(node.left) + self._postorder(node.right) + [node.key]

    def levelorder(self):
        if self.root is None:
            return []
        else:
            return self._levelorder(self.root)

    def _levelorder(self, node):
        if node is None:
            return []
        else:
            queue = [node]
            result = []
            while len(queue) > 0:
                node = queue.pop(0)
                result.append(node.key)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            return result


if __name__ == '__main__':
    print('Binary Search Tree')
    bst = BST()
    bst.insert(10)
    for _ in range(11):
        bst.insert(random.randint(0, 20))
    bst.display()
