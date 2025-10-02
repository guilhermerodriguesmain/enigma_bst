
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

#-----------------------------------------------------------------árvore binária
class Tree:
    def __init__(self):
        self.root = None
    
    #-----------------------------------------------------------------inserir mensagem em pós ordem na árvore
    def pos_order_insert(self, message: str):
        self.root = self._recursive_pos_inset(message)
        print("Arvore montada")

    def _recursive_pos_inset(self, partial_message: str):
        if not partial_message:
            return None
        
        tree_root = TreeNode(partial_message[-1])
        rest_message = partial_message[:-1]
        midpoint = len(rest_message) // 2

        tree_root.left = self._recursive_pos_inset(rest_message[:midpoint])
        tree_root.right = self._recursive_pos_inset(rest_message[midpoint:])

        return tree_root

    #----------------------------------------------percurso em pós ordem salvando em arquivo txt (descriptografia)
    def pos_order(self, file_name):
        if self.root is None:
            return "A árvore está vazia"

        with open(file_name, "w") as file:
            self._recursive_pos_order(self.root, file)

    def _recursive_pos_order(self, current_node, file):
        if current_node is None:
            return
        self._recursive_pos_order(current_node.left, file)
        self._recursive_pos_order(current_node.right, file)
        file.write(str(current_node.value) + ",")

    #---------------------------------------------------pos ordem salvando em lista e retornando uma string (descriptografia)
    def pos_order_to_string(self):
        if self.root is None:
            return "A árvore está vazia"
        list_result = []
        self._recursive_pos_order_to_string(self.root, list_result)
        return "".join(list_result)
    
    def _recursive_pos_order_to_string(self, current_node, list_result: list):
        if current_node is None:
            return
        self._recursive_pos_order_to_string(current_node.left, list_result)
        self._recursive_pos_order_to_string(current_node.right, list_result)
        list_result.append(current_node.value)
        
    #---------------------------------------------------pos ordem retornando uma lista (exportar para json)
        """
        percorre a árvore em pós ordem e salva os valores em uma lista
        """
        

    def post_order_crypto(self):
        if self.root is None:
            return "A árvore está vazia"
        list_result = []
        self._recursive_post_order_to_list(self.root, list_result)
        return list_result
    
    def _recursive_post_order_to_list(self, current_node, list_result: list):
        if current_node is None:
            return
        self._recursive_post_order_to_list(current_node.left, list_result)
        self._recursive_post_order_to_list(current_node.right, list_result)
        list_result.append(current_node.value)
        
    #---------------------------------------------------inserindo uma lista na árvore (criptografia)
    def Pos_order_insert(self, values: list):
        """
        Inserts multiple values into the tree in the order they appear in the given list.

        Args:
            values (list): A list of values to be inserted into the tree.

        Note:
            The insertion is performed in post-order fashion, meaning each value is inserted sequentially
            using the internal recursive insert method.
        """
        for value in values:
            self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if current_node is None:
            return TreeNode(value)
        if value < current_node.value:
            current_node.left = self._insert_recursive(current_node.left, value)
        else:
            current_node.right = self._insert_recursive(current_node.right, value)
        return current_node
    