import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time


class node:
    def __init__(self, c):
        self.value = None
        self.left = None
        self.right = None
        self.size = 1
        self.c = c

    def display(self):
        if self.left:
            self.left.display()
        if self.right:
            self.right.display()

    def insert(self, value):
        if self.value is None:
            self.value = value
            self.size += 1
            return True
        else:
            if value < self.value:

                if self.left is None:
                    self.left = node(self.c)
                    placed = self.left.insert(value)
                    if placed:
                        self.size += 1
                        return True

                elif self.left.size > self.c * self.size:
                    placed = self.left.insert(value)
                    if placed:
                        self.size += 1
                        return True

                else:
                    traversed = self.inordertraversal()
                    originLen = len(traversed)
                    for i in range(0, len(traversed)):
                        if value == traversed[i]:
                            return False
                        if value < traversed[i]:
                            traversed = traversed[:i] + [value] + traversed[i:]
                            break
                    if originLen == len(traversed):
                        traversed = traversed + [value]
                    self.left = None
                    self.right = None
                    self.balance(traversed)

            elif value > self.value:

                if self.right == None:
                    self.right = node(self.c)
                    placed = self.right.insert(value)
                    if placed:
                        self.size += 1
                        return True

                elif self.right.size > self.c * self.size:
                    placed = self.right.insert(value)
                    if placed:
                        self.size += 1
                        return True

                else:
                    traversed = self.inordertraversal()
                    originLen = len(traversed)
                    for i in range(0, len(traversed)):
                        if value == traversed[i]:
                            return False
                        if value < traversed[i]:
                            traversed = traversed[:i] + [value] + traversed[i:]
                            break
                    if originLen == len(traversed):
                        traversed = traversed + [value]
                    self.left = None
                    self.right = None

                    self.balance(traversed)
            else:  # if the insertion value is the same as a value already found we do not insert
                return False

    def inordertraversal(self):
        datatraversed = []
        if self.left:
            datatraversed = self.left.inordertraversal()
        datatraversed.append(self.value)
        if self.right:
            datatraversed = datatraversed + self.right.inordertraversal()
        return datatraversed

    def balance(self, values):
        self.value = values[len(values) // 2]
        self.size = len(values)
        left = values[:len(values) // 2]
        right = values[len(values) // 2 + 1:]
        if len(left) > 0:
            self.left = node(self.c)
            self.left.balance(left)
        if len(right) > 0:
            self.right = node(self.c)
            self.right.balance(right)

    # Display code from: https://stackoverflow.com/a/54074933
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value + ' (' + str(self.size) + ')'
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value + ' (' + str(self.size) + ')'
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value + ' (' + str(self.size) + ')'
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value + ' (' + str(self.size) + ')'
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


def height(root):
    # if root is None return 0
    if root == None:
        return 0
    # find height of left subtree
    hleft = height(root.left)
    # find the height of right subtree
    hright = height(root.right)
    # find max of hleft and hright, add 1 to it and return the value
    if hleft > hright:
        return hleft + 1
    else:
        return hright + 1


def CheckBalancedBinaryTree(root):
    # if tree is empty,return True
    if root is None:
        return True
    # check height of left subtree
    lheight = height(root.left)
    rheight = height(root.right)
    # if difference in height is greater than 1, return False
    if (abs(lheight - rheight) > 1):
        return False
    # check if left subtree is balanced
    lcheck = CheckBalancedBinaryTree(root.left)
    # check if right subtree is balanced
    rcheck = CheckBalancedBinaryTree(root.right)
    # if both subtree are balanced, return True
    if lcheck == True and rcheck == True:
        return True


if __name__ == '__main__':
    print('Binary Search Tree')

    c = 0.5
    maxheight = 7
    elements = (2 ** maxheight) - 1
    print(elements)
    test = node(c)
    for i in range(elements):
        test.insert(random.randint(0, elements * 2))

    print('#' * 60)
    print('Variables: \t')
    print('c:                       \t', c)
    print('Size:                    \t', test.size)
    print('height:                    \t', height(test))
    print('balanced:                \t', CheckBalancedBinaryTree(test))
    print('#' * 60)
    test.display()

    test1 = []
    test2 = []
    test3 = []
    test4 = []
    for i in range(0):
        if i == 0:
            for j in range(1000):
                c = 0.55
                maxheight = 10
                elements = (2 ** maxheight) - 1
                testing = node(c)
                for z in range(elements):
                    testing.insert(random.randint(0, 100))

                if not CheckBalancedBinaryTree(testing):
                    test1.append('not balanced')
        if i == 1:
            for j in range(10000):
                c = 0.6
                maxheight = 5
                elements = (2 ** maxheight) - 1
                testing = node(c)
                for z in range(elements):
                    testing.insert(random.randint(0, 100))

                if not CheckBalancedBinaryTree(testing):
                    test2.append('not balanced')
        if i == 2:
            for j in range(10000):
                c = 0.8
                maxheight = 5
                elements = (2 ** maxheight) - 1
                testing = node(c)
                for z in range(elements):
                    testing.insert(random.randint(0, 100))

                if not CheckBalancedBinaryTree(testing):
                    test3.append('not balanced')
        if i == 3:
            for j in range(10000):
                c = 1
                maxheight = 5
                elements = (2 ** maxheight) - 1
                testing = node(c)
                for z in range(elements):
                    testing.insert(random.randint(0, 100))

                if not CheckBalancedBinaryTree(testing):
                    test4.append('not balanced')

    _c = []
    _corr = []
    correct = []
    for i in range(0, 100):
        c = 0.5 + (0.005 * i)
        _c.append(c)
        _corr = []
        for j in range(100):
            maxheight = 7
            elements = (2 ** maxheight) - 1
            plot = node(c)
            sample = random.sample(range(0, 50000), elements)
            for z in range(elements):
                plot.insert(sample[z])

            if CheckBalancedBinaryTree(plot):
                _corr.append(1)
        correct.append((len(_corr) / 100) * 100)

    plt.plot(_c, correct)
    plt.ylabel('in %')
    plt.xlabel('c variable')
    plt.title('c variable vs. correct ( unique sample ) with 100 trials')
    plt.show()

    _c2 = []
    _time = []
    for i in range(90, 0, -1):
        c = 0.50 + (0.005*i)
        _c2.append(c)
        for j in range(1):
            maxheight = 7 * (j)
            elements = (2 ** maxheight) - 1
            sample = random.sample(range(0, 50000), elements)
            start = time.time()
            plot = node(c)
            for z in range(elements):
                plot.insert(sample[z])
            end = time.time()
            _time.append(end - start)

    plt.plot(_c2, _time)
    plt.ylabel('time')
    plt.xlabel('c variable')
    plt.title('c variable vs. time ( unique sample of 2^7-1  ) with 90 trials')
    plt.show()

    _time2 = []
    _elemens2 = []
    for i in range(0, 90):
        c = 0.6
        for j in range(4):

            maxheight = 3 + (1 * j)
            elements = (2 ** maxheight) - 1

            sample = random.sample(range(0, 50000), elements)
            start = time.time()
            plot = node(c)
            for z in range(elements):
                plot.insert(sample[z])
            end = time.time()
            _elemens2.append(elements)
            _time2.append(end - start)

    plt.scatter(_elemens2, _time2)
    plt.ylabel('time')
    plt.xlabel('elements')
    plt.title('elements vs. time ( unique sample c = 0.6) with 90 trials')
    plt.show()
