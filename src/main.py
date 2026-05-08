def main():
    print("Hello, world from GitHub Codespaces + Dev Container!")

def add_numbers(a, b):
    return a + b

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None

# ─── INSERT ───────────────────────────────────────────
    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if node is None:
            return TreeNode(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # Duplicates ignored

        return node

    # ─── SEARCH ───────────────────────────────────────────
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    # ─── DELETE ───────────────────────────────────────────
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Case 1: Leaf node
            if node.left is None and node.right is None:
                return None

            # Case 2: One child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Case 3: Two children — replace with in-order successor
            min_val = self._find_min_node(node.right).value
            node.value = min_val
            node.right = self._delete_recursive(node.right, min_val)

        return node

    # ─── MIN / MAX ─────────────────────────────────────────
    def find_min(self):
        if self.root is None:
            raise ValueError("Tree is empty.")
        return self._find_min_node(self.root).value

    def find_max(self):
        if self.root is None:
            raise ValueError("Tree is empty.")
        node = self.root
        while node.right:
            node = node.right
        return node.value

    def _find_min_node(self, node):
        while node.left:
            node = node.left
        return node

    # ─── HEIGHT ───────────────────────────────────────────
    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return 0
        return 1 + max(
            self._height_recursive(node.left),
            self._height_recursive(node.right)
        )

    # ─── COUNT ────────────────────────────────────────────
    def count(self):
        return self._count_recursive(self.root)

    def _count_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._count_recursive(node.left) + self._count_recursive(node.right)

if __name__ == "__main__":
    main()
