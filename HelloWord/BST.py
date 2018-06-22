class BST:
    root = None

    def __init__(self):
        pass

    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def add(self, val):
        self.root = self.add_node(self.root, val)

    def add_node(self, root, val):
        if root is None:
            root = self.Node(val)
        else:
            if val < root.val:
                root.left = self.add_node(root.left, val)
            else:
                root.right = self.add_node(root.right, val)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)


def test_bst():
    bst = BST()
    bst.add(10)
    bst.add(20)
    bst.inorder(bst.root)

test_bst()
