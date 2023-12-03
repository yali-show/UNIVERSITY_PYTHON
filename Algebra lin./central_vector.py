import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class GraphWorker:
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

    def tres_mas_centrados(self, graf):
        nodes = list(self.get_eigenvector_centrality(graf).items())
        return sorted(nodes, reverse=True, key=lambda x: x[1])[:3]

    def tres_menores_centrados(self, graf):
        nodes = list(self.get_eigenvector_centrality(graf).items())
        return sorted(nodes, key=lambda x: x[1])[:3]
    def trabajo(self):
        self.example_func(nx.karate_club_graph(), "\nLos resultador para el grafo karate_club_graph: \n")
        self.example_func(nx.florentine_families_graph(), "\nLos resultador para el grafo florentine_families_graph: \n")
        print("Mas centrados: {} de karate club".format(self.tres_mas_centrados(nx.karate_club_graph())))
        print("Mas centrados: {} de florentine families".format(self.tres_mas_centrados(nx.florentine_families_graph())))
        print("Menos centrados de karate club: {} ".format(self.tres_menores_centrados(nx.karate_club_graph())))
        print("Menos centrados de florentine families: {} ".format(self.tres_menores_centrados(nx.florentine_families_graph())))




if __name__ == "__main__":
    GraphWorker().trabajo()


