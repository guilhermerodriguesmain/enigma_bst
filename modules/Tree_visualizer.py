import matplotlib.pyplot as plt
import networkx as nx

class TreeVisualizer:
    def __init__(self, tree):
        self.tree = tree
        self.G = nx.DiGraph()
        self.pos = {}

    def build_graph(self, node, x=0, y=0, dx=1.0):
        """Cria nós e calcula posições manualmente."""
        if node is None:
            return
        self.G.add_node(node.value)
        self.pos[node.value] = (x, y)
        if node.left:
            self.G.add_edge(node.value, node.left.value)
            self.build_graph(node.left, x - dx, y - 1, dx / 2)
        if node.right:
            self.G.add_edge(node.value, node.right.value)
            self.build_graph(node.right, x + dx, y - 1, dx / 2)

    def plot(self):
        self.build_graph(self.tree.root)
        plt.figure(figsize=(12, 6))
        nx.draw(self.G, self.pos, with_labels=True, arrows=False,
                node_size=2000, node_color='skyblue',
                font_size=8, font_weight='bold')
        plt.gca().invert_yaxis()  # inverte o eixo y para parecer com uma árvore
        plt.show()
