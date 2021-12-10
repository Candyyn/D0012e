

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data): #O(n)
    if root is None:
        root = node(data)
    else:
        if data <= root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root


def displayAll(root):
    if root:
        displayAll(root.left)
        print(root.data)
        displayAll(root.right)



if __name__ == '__main__':
    print('Binary Search Tree')

    test = node(10)
    test = insert(test, 3)
    test = insert(test, 11)
    test = insert(test, 2)
    test = insert(test, 15)
    test = insert(test, 1)

    displayAll(test)