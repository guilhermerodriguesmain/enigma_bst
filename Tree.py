
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
    def pos_order(self, file_name: str):
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

    #--------------------------------------------------------------------------pre ordem (criptografia)
    def pre_order(self):
        if self.root is None:
            return "A árvore está vazia"
        list_result = []
        self._recursive_pre_order(self.root, list_result)
        return "".join(list_result)
    
    def _recursive_pre_order(self, current_node, list_result: list):
        if current_node is None:
            return
        list_result.append(current_node.value)
        self._recursive_pre_order(current_node.left, list_result)
        self._recursive_pre_order(current_node.right, list_result)
    
    def pre_order_insert(self, message: str):
        self.root = self._recursive_pre_insert(message)
        print("Arvore montada")

    def _recursive_pre_insert(self, partial_message: str):
        if not partial_message:
            return None
        
        tree_root = TreeNode(partial_message[0])
        rest_message = partial_message[1:]
        midpoint = len(rest_message) // 2

        tree_root.left = self._recursive_pre_insert(rest_message[:midpoint])
        tree_root.right = self._recursive_pre_insert(rest_message[midpoint:])

        return tree_root