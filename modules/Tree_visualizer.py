import matplotlib.pyplot as plt
import networkx as nx

class TreeVisualizer:
    def __init__(self, tree):
        self.tree = tree
        self.G = nx.DiGraph()

    def build_graph(self, node):
        if node is None:
            return
        self.G.add_node(node.value)
        if node.left:
            self.G.add_edge(node.value, node.left.value)
            self.build_graph(node.left)
        if node.right:
            self.G.add_edge(node.value, node.right.value)
            self.build_graph(node.right)

    def plot(self):
        self.build_graph(self.tree.root)
        pos = nx.nx_agraph.graphviz_layout(self.G, prog="dot")
        nx.draw(self.G, pos, with_labels=True, arrows=False, node_size=2000,
                node_color='skyblue', font_size=10, font_weight='bold')
        plt.show()
