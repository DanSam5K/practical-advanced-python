class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(data, node.right)

    def search(self, data):
        return self._search_recursive(data, self.root)
    
    def _search_recursive(self, data, node):
        if node is None or node.data == data:
            return node
        
        if data < node.data:
            return self._search_recursive(data, node.left)
        else:
            return self._search_recursive(data, node.right)
        
    def delete(self, data):
        self.root = self._delete_recursive(data, self.root)

    def _delete_recursive(self, data, node):
        if node is None:
            return node
        
        if data < node.data:
            node.left = self._delete_recursive(data, node.left)
        elif data > node.data:
            node.right = self. _delete_recursive(data, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            min_node = self._find_min(node.right)
            node.data = min_node.data
            node.right = self._delete_recursive(min_node.data, node.right)

        return node
    
    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node
    
    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node is not None:
            self._inorder_recursive(node.left)
            print(node.data, end=" ")
            self._inorder_recursive(node.right)


# Create a new binary tree
my_tree = BinaryTree()

# Insert elements into the binary tree
my_tree.insert(50)
my_tree.insert(30)
my_tree.insert(70)
my_tree.insert(20)
my_tree.insert(40)
my_tree.insert(60)
my_tree.insert(80)

# Search for an element in the binary tree
print(my_tree.search(40))  # Output: <__main__.TreeNode object at 0x...>

# Delete an element from the binary tree
my_tree.delete(30)

# Perform inorder traversal of the binary tree
my_tree.inorder_traversal()  # Output: 20 40 50 60 70 80