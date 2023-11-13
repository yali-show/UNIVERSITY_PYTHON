import matplotlib.pyplot as plt
import numpy as np


class MaxMinTrabajo:
    def __init__(self):
        self.obtener_graficos()

    def obtener_graficos(self) -> None:
        self.example1()
        self.example2()
        self.example3()
        self.example4()
        self.example5()

    @staticmethod
    def example1() -> None:
        x = np.linspace(-2, 2)
        y = x ** 3 - 3 * x

        plt.title("x³ - 3x")
        plt.plot(x, y)
        plt.scatter(-1, 2, facecolors='red')
        plt.scatter(1, -2, facecolors='blue')
        plt.scatter(2, 2, facecolors='red')
        plt.scatter(-2, -2, edgecolors='blue', facecolors='none')
        plt.grid()
        plt.show()

    @staticmethod
    def example2() -> None:
        x = np.linspace(-2, 3)
        y = x ** 3 - (6*x ** 2) + 9*x
        plt.title("x³ - 6x² + 9x")
        plt.plot(x, y)
        plt.scatter(1, 4, facecolors='red')
        plt.scatter(3, 0, facecolors='blue')
        # plt.scatter(4, 4, facecolors='red')
        plt.scatter(-2, -50, edgecolors='blue', facecolors='none')
        # plt.scatter(1, -2, facecolors='blue')
        # plt.scatter(2, 2, facecolors='red')
        plt.grid()
        plt.show()

    @staticmethod
    def example3() -> None:
        x = np.linspace(-2, 4)
        y = x ** 3 - (6 * x ** 2) + 9 * x
        plt.title("x³ - 6x² + 9x")
        plt.plot(x, y)
        # plt.scatter(1, 4, facecolors='red')
        plt.scatter(1, 4, facecolors='red')
        plt.scatter(3, 0, facecolors='blue')
        plt.scatter(-2, -50, edgecolors='red', facecolors='none')
        plt.scatter(4, 4, facecolors='red')

        plt.grid()
        plt.show()

    @staticmethod
    def example4() -> None:
        x = np.linspace(-2, 4)
        y = -x ** 3 + (6*x ** 2) - 9*x
        plt.title("-x³ + 6x² - 9x")
        plt.plot(x, y)
        # plt.scatter(1, 4, facecolors='red')
        plt.scatter(3, 0, facecolors='red')
        plt.scatter(1, -4, facecolors='blue')
        plt.scatter(-2, 50, edgecolors='red', facecolors='none')
        plt.scatter(4, -4, facecolors='blue')

        plt.grid()
        plt.show()

    @staticmethod
    def example5() -> None:
        x = np.linspace(-2, 3)
        y = -x ** 3 + (6*x ** 2) - 9*x
        plt.title("-x³ + 6x² - 9x")
        plt.plot(x, y)
        # plt.scatter(1, 4, facecolors='red')
        plt.scatter(3, 0, facecolors='red')
        plt.scatter(1, -4, facecolors='blue')
        plt.scatter(-2, 50, edgecolors='red', facecolors='none')
        # plt.scatter(4, -4, facecolors='blue')

        plt.grid()
        plt.show()

MaxMinTrabajo()
