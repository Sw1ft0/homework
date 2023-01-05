class BinaryTreeNode:
    def __init__(self, product_code: int, price: float):
        self.product_code = product_code
        self.price = price
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, product_code: int, price: float):
        new_node = BinaryTreeNode(product_code, price)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if product_code < current.product_code:
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right

    def find_cost(self, product_code: int, quantity: int):
        current = self.root
        while current is not None:
            if current.product_code == product_code:
                return current.price * quantity
            elif product_code < current.product_code:
                current = current.left
            else:
                current = current.right
        return None

tree = BinaryTree()
tree.insert(234, 10)
tree.insert(543, 20)
tree.insert(567, 30)

cost = tree.find_cost(543, 2)
print(cost)  # prints 40
