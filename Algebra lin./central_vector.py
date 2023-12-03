import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class GraphWorker:
    def __init__(self):
        ...

    @staticmethod
    def draw_graph(g):
        nx.draw(g, with_labels=True, node_size=500, node_color='skyblue')
        plt.show()

    @staticmethod
    def get_eigenvector_centrality(g):
        return nx.eigenvector_centrality(g)

    def example_func(self, graph, text=''):
        self.draw_graph(graph)
        print(text)
        print(self.get_eigenvector_centrality(graph))

    def trabajo(self):
        self.example_func(nx.karate_club_graph(), "\nLos resultador para el grafo karate_club_graph: \n")
        self.example_func(nx.florentine_families_graph(), "\nLos resultador para el grafo florentine_families_graph: \n")


if __name__ == "__main__":
    GraphWorker().trabajo()


