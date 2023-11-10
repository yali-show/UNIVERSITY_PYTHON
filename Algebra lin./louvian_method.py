import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import community  # python-louvain

class LouvianTrabajo:
    def __init__(self):
        self.ejemplo_karate_club_graph()
        self.result_con_graph_dado()
    @staticmethod
    def obtener_el_graf():
        matriz = input("Escriba matriz de ayudencia como en ejemplo:\n "
                       "0 1 1|0 0 1|1 1 0 : ")
        try:
            matriz = np.array([[int(i) for i in x.split()]
                               for x in matriz.split("|")])

        except Exception:
            print('Mal datos: error')

        return matriz

    def result_con_graph_dado(self):
        grafo = self.obtener_el_graf()
        graph = nx.Graph()
        num_nodes = len(grafo)
        graph.add_nodes_from(range(num_nodes))

        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                if grafo[i][j] == 1:
                    graph.add_edge(i, j)

        nx.draw(graph, with_labels=True, node_size=500, node_color='skyblue')
        plt.show()

        partition = community.best_partition(graph)
        print("Comunidades encontrados entre tu grafo: ")
        print(partition)


    @staticmethod
    def ejemplo_karate_club_graph():
        g = nx.karate_club_graph()
        nx.draw(g, with_labels=True, node_size=500, node_color='skyblue')
        plt.show()
        partition = community.best_partition(g)
        print("Un ejemplo de metodo louvian para un grafo karate_club_graph"
              " con 34 nodes and 78 edges:")
        print(partition)

LouvianTrabajo()
