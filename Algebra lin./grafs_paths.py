import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class GetAmountObject:
    def __init__(self):
        self.run_work()

    @staticmethod
    def get_paths_amount(matrix_graf, start, following, arcos):
        """
        Elevamos matriz a 3 y en primer fila [0]  y columna de 'following' node
        node buscado
        :param matrix_graf:
        :param start:
        :param following:
        :return:
        """
        paths = np.linalg.matrix_power(matrix_graf, arcos)
        print(f"Cantidad de rutas desde el nodo {start} a {following} ({arcos} arcs): "
              f"{paths[start, following]}")
        return matrix_graf

    @staticmethod
    def get_graf_visual(matrix):
        """
        Pintamos grafo
        :param matrix:
        :return:
        """
        Graph = nx.Graph()
        num_nodes = len(matrix)
        Graph.add_nodes_from(range(num_nodes))

        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                if matrix[i][j] == 1:
                    Graph.add_edge(i, j)

        nx.draw(Graph, with_labels=True, node_size=1000, node_color='skyblue')

        plt.show()

    def run_work(self):

        arcs = int(input("Arcos: "))
        matriz = input("Escriba matriz de ayudencia como en ejemplo:\n "
                       "0 1 1|0 0 1|1 1 0 : ")
        try:
            matriz = np.array([[int(i) for i in x.split()]
                               for x in matriz.split("|")])

        except Exception:
            print('Mal datos: error')

        start = int(input('Start node: '))
        end = int(input('End node: '))
        self.get_paths_amount(matriz, start, end, arcs)
        self.get_graf_visual(matriz)

# Matriz para ejemplo
#     [0, 1, 1, 0, 0],
#     [1, 0, 1, 1, 0],
#     [1, 1, 0, 1, 1],
#     [0, 1, 1, 0, 1],
#     [0, 0, 1, 1, 0]


GetAmountObject()
