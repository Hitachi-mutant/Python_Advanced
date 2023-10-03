'''Home work for the lesson 27'''

'''Task 1 - Розширити структуру, яку побудували на уроці, 
можливістю вставки дерева в наявне дерево та видалення піддерева з дерева, що існує.'''

# structure was created during the lesson and expanded as a homework

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, current_node, key):
        if current_node is None:
            return TreeNode(key)
        else:
            if key < current_node.value:
                current_node.left = self.insert(current_node.left, key)
            else:
                current_node.right = self.insert(current_node.right, key)
        return current_node

    def search(self, current_node, key):
        if current_node is None or current_node.value == key:
            return current_node
        if current_node.value < key:
            return self.search(current_node.right, key)
        return self.search(current_node.left, key)
    
    def find_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value

    def delete(self, current_node, key):
        if current_node is None:
            return current_node
        if key < current_node.value:
            current_node.left = self.delete(current_node.left, key)
        elif key > current_node.value:
            current_node.right = self.delete(current_node.right, key)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            current_node.value = self.find_min_value_node(current_node.right)
            current_node.right = self.delete(current_node.right, current_node.value)
        return current_node

    def inorder_traversal(self, current_node):
        if current_node:
            self.inorder_traversal(current_node.left)
            print(current_node.value, end=' ')
            self.inorder_traversal(current_node.right)


if __name__ == "__main__":
    
    bst = BinarySearchTree()
    root = None
    root = bst.insert(root, 53)
    bst.insert(root, 42)
    bst.insert(root, 18)
    bst.insert(root, 38)
    bst.insert(root, 89)
    bst.insert(root, 54)
    bst.insert(root, 7)

    print("Inorder traversal of the BST:")
    bst.inorder_traversal(root)
    print()

    print("Search for 54:", bst.search(root, 54) is not None)
    print("Search for 7:", bst.search(root, 7) is not None)

    root = bst.delete(root, 89)
    print("Inorder traversal after deleting 89:")
    bst.inorder_traversal(root)
    print()

    print("Search for 89 after deletion:", bst.search(root, 89) is not None)