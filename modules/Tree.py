class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    #----------------------------- Inserir mensagem em pós-ordem
    def pos_order_insert(self, message: str):
        self.root = self._build_tree_post_order(list(message))
        print("Árvore montada em pós-ordem")

    #----------------------------- Inserir lista de valores (pré-ordem)
    def crypto_insert(self, values: list):
        self.root = self._build_tree_pre_order(values)
        print("Árvore montada a partir da lista")

    #----------------------------- Construção recursiva pré-ordem
    def _build_tree_pre_order(self, values: list):
        if not values:
            return None
        node = TreeNode(values[0])
        rest = values[1:]
        mid = len(rest) // 2
        node.left = self._build_tree_pre_order(rest[:mid])
        node.right = self._build_tree_pre_order(rest[mid:])
        return node

    #----------------------------- Construção recursiva pós-ordem
    def _build_tree_post_order(self, values: list):
        if not values:
            return None
        node = TreeNode(values[-1])
        rest = values[:-1]
        mid = len(rest) // 2
        node.left = self._build_tree_post_order(rest[:mid])
        node.right = self._build_tree_post_order(rest[mid:])
        return node

    #----------------------------- Pós-ordem retornando lista
    def post_order_list(self):
        result = []
        self._post_order(self.root, result)
        return result

    def _post_order(self, node, result: list):
        if node is None:
            return
        self._post_order(node.left, result)
        self._post_order(node.right, result)
        result.append(node.value)

    #----------------------------- Impressão gráfica da árvore
    def print_tree(self):
        if not self.root:
            print("Árvore vazia")
            return
        self._print(self.root, 0)

    def _print(self, node, level):
        if node is not None:
            self._print(node.right, level + 1)
            print("    " * level + str(node.value))
            self._print(node.left, level + 1)
