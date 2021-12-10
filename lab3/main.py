import random


class node:
    def __init__(self, data, c):
        self.data = data
        self.left = None
        self.right = None
        self.size = 0
        self.leftCount = 0
        self.rightCount = 0

    def getSize(self):
        return self.size

    def updateSize(self):  # sums the size of the nodes below it
        temp = 1
        if self.left is not None:
            temp += self.left.getSize()

        if self.right is not None:
            temp += self.right.getSize()

        self.size = temp

    def addleft(self):
        self.leftCount += 1
        self.updateSize()

    def addright(self):
        self.rightCount += 1
        self.updateSize()

    # Display code from: https://stackoverflow.com/a/54074933
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data + ' (' + str(self.size) + ')'
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data + ' (' + str(self.size) + ')'
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data + ' (' + str(self.size) + ')'
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data + ' (' + str(self.size) + ')'
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


def isPerfectRec(root, d, level=0):
    # An empty tree is perfect
    if (root == None):
        return True

    # If leaf node, then its depth must
    # be same as depth of all other leaves.
    if root.left == None and root.right == None:
        return (d == level + 1)

    # If internal node and one child is empty
    if (root.left == None or root.right == None):
        return False

    # Left and right subtrees must be perfect.
    return (isPerfectRec(root.left, d, level + 1) and
            isPerfectRec(root.right, d, level + 1))


# Wrapper over isPerfectRec()
def isPerfect(root):
    d = findADepth(root)
    return isPerfectRec(root, d)


def findADepth(node):
    d = 0
    while (node != None):
        d += 1
        node = node.left
    return d


def height(root):
    # Check if the binary tree is empty
    if root is None:
        # If TRUE return 0
        return 0
        # Recursively call height of each node
    leftAns = height(root.left)
    rightAns = height(root.right)

    # Return max(leftHeight, rightHeight) at each iteration
    return max(leftAns, rightAns) + 1


def insert(root, data, c):  # O(n)
    if root is None:
        root = node(data, c)
    else:
        if data <= root.data:
            if True:
            #if root.leftCount <= (root.rightCount + root.leftCount) * c:
                root.left = insert(root.left, data, c)
                root.addleft()
        else:
            if True:
            #if root.rightCount <= (root.rightCount + root.leftCount) * c:
                root.right = insert(root.right, data, c)
                root.addright()
    return root


def inordertraversal(root):
    datatraversed = []
    if root:
        datatraversed = inordertraversal(root.left)
        datatraversed.append(root.data)
        datatraversed = datatraversed + inordertraversal(root.right)
    return datatraversed


if __name__ == '__main__':
    print('Binary Search Tree')

    c = 0.5
    maxheight = 2
    elements = (2 ** maxheight) - 1
    print(elements)
    test = node(5, c)
    for i in range(elements - 1):
        root = insert(test, random.randint(0, 10), c)

    print('#' * 60)
    print('Variables: \t')
    print('c:                       \t', c)
    print('Max Subtree height:      \t', (test.rightCount + test.leftCount) * c)
    print('Height of the tree:      \t', height(test))
    print('Size:                    \t', test.size)
    print('Is perfectly balanced?   \t', isPerfect(test))
    print('#' * 60)
    test.display()
