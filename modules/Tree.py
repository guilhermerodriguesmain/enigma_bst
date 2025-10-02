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
    # Funcionando e montando a arvore corretamente (recebe mensagem de arquivo txt abero e salvo em uma variável)
    def pos_order_insert(self, message: str):
        if type(message) is not str:
            if type(message) is list:
                new_message = ""
                for bin in message:
                    new_message = new_message + bin + " "
                message = new_message
            else:
                return "Erro: tipo de dado inválido. Use string ou lista de strings."
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

    #---------------------------------------------------pos ordem retornando uma lista (exportar para json)
    def pos_order_to_list(self):
        if self.root is None:
            return "A árvore está vazia"
        list_result = []
        self._recursive_pos_order_to_list(self.root, list_result)
        return list_result
    
    def _recursive_pos_order_to_list(self, current_node, list_result: list):
        if current_node is None:
            return
        self._recursive_pos_order_to_list(current_node.left, list_result)
        self._recursive_pos_order_to_list(current_node.right, list_result)
        list_result.append(current_node.value)

    #---------------------------------------------------pos ordem retornando uma string (descriptografia)
    # String pode ser salva em arquivo externo através de outro módulo/método ou exibida no terminal com print
    def pos_order_to_string(self):
        list_tree = self.pos_order_to_list()
        return "".join(list_tree)
           
    #-------------------------------------------------------------------------------pre ordem 
    # Funcionando - retorna lista de valores em pre ordem
    def pre_order_to_list(self):
        if self.root is None:
            return "A árvore está vazia"
        list_result = []
        self._recursive_pre_order(self.root, list_result)
        return list_result
    
    def _recursive_pre_order(self, current_node, list_result: list):
        if current_node is None:
            return
        list_result.append(current_node.value)
        self._recursive_pre_order(current_node.left, list_result)
        self._recursive_pre_order(current_node.right, list_result)

    #-------------------------------------------------------------------------------pre ordem retornando string (criptografia)
    # String pode ser salva em arquivo externo através de outro módulo/método ou exibida no terminal com print
    def pre_order_to_string(self):
        list_tree = self.pre_order_to_list()
        return "".join(list_tree)
    
    #-----------------------------------------------------------------inserir mensagem em pré ordem na árvore
    
    def pre_order_insert(self, message: str):
        if type(message) is not str:
            if type(message) is list:
                new_message = ""
                for bin in message:
                    new_message = new_message + bin + " "
                message = new_message
            else:
                return "Erro: tipo de dado inválido. Use string ou lista de strings."
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