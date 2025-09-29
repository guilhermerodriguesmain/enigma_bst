
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

#-----------------------------------------------------------------árvore binária
class Tree:
    def __init__(self):
        self.root = None

    def insert (self, element):
        if self.root is None:
            self.root = TreeNode(element)
        else:
            self._recursive_insert(self.root, element)

    def _recursive_insert(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = TreeNode(value)
            else:
                self._recursive_insert(current.left, value)
        else:
            if current.right is None:
                current.right = TreeNode(value)
            else:
                self._recursive_insert(current.right, value)

    #---------------------------------percurso em pós ordem
    def post_order (self, file_name):
        with open(file_name, "w") as file:
            self._save_leaves(self.root, file)
    
    def _save_leaves(self, node, file):
        if node is None:
            return
        
        self._save_leaves(node.left, file)
        self._save_leaves(node.right, file)

        if node.left and node.right is None:
            file.write(str(node.value)+",")