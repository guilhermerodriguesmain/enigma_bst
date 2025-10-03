"""
melhoria -> nova feature 
arvore precisa iterar sobre uma lista de valores colocar na ordem certa e retornar em forma de lista
"""""
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
        
        for value in values:
            self.root = self._insert_recursive(self.root, value)

    def _recursive_pre_insert(self, partial_message: str):
        if not partial_message:
            return None
        
        tree_root = TreeNode(partial_message[0])
        rest_message = partial_message[1:]
        midpoint = len(rest_message) // 2

        tree_root.left = self._recursive_pre_insert(rest_message[:midpoint])
        tree_root.right = self._recursive_pre_insert(rest_message[midpoint:])

        return tree_root

    #-------------------------------------------------------representação da árvore
    def print_tree(self):
        if self.root is None:
            print("A árvore está vazia")
            return
        self._recursive_print(self.root, 0)  
    
    def _recursive_print(self, node, level):
        if node is not None:
            space = 4
            self._recursive_print(node.right, level + 1)
            print(" " * (space * level), end="")
            print(node.value)
            self._recursive_print(node.left, level + 1)

    #-------------------------------------------------------representação em níveis/identação
    #-----------------nós esquerdos abaixo e direitos acima

    def __str__(self):
        if self.root is None:
            return "A árvore está vazia"
        
        return self._str_helper(self.root, "", True)

    def _str_helper(self, node, prefix, is_last):
        if node is None:
            return ""

        current_line = prefix + ("`-- " if is_last else "|-- ") + str(node.value) + "\n"
        prefix_child = prefix + ("    " if is_last else "|   ")
        
        children = []
        if node.right:
            children.append(node.right)
        if node.left:
            children.append(node.left)
    
        child_lines = ""
        for i, child in enumerate(children):
            is_child_last = (i == len(children) - 1)
            child_lines += self._str_helper(child, prefix_child, is_child_last)
            
        return current_line + child_lines
        