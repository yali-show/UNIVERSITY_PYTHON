import matplotlib.pyplot as plt
import numpy as np


def get_data_por_tax(x):
    if x <= 12450:
        return x * 0.19

    elif x <= 19999:
        return 12450 * 0.19 + (x - 12450) * 0.24

    elif x <= 35199:
        return 12450 * 0.19 + (19999 - 12450) * 0.24 + (x - 19999) * 0.30

    elif x <= 59999:
        return 12450 * 0.19 + (19999 - 12450) * 0.24 + (
                    35199 - 19999) * 0.30 + (x - 35199) * 0.37

    elif x <= 299999:
        return 12450 * 0.19 + (19999 - 12450) * 0.24 + (
                    35199 - 19999) * 0.30 + (59999 - 35199) * 0.37 + (
                    x - 59999) * 0.45

    else:
        return 12450 * 0.19 + (19999 - 12450) * 0.24 + (
                    35199 - 19999) * 0.30 + (59999 - 35199) * 0.37 + (
                    299999 - 59999) * 0.45 + (x - 299999) * 0.47


def draw(salario):
    x = np.linspace(0, salario, 1000)

    taxes = np.vectorize(get_data_por_tax)(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, taxes, label='TAX')

    plt.title('IRPF ')
    plt.xlabel('Salario, euro')
    plt.ylabel('TAX, euro')
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    in_progress = True

    while in_progress:

        try:
            data = int(input("Tu salario: "))
            draw(data)

        except Exception as ex:
            print(ex)
            in_progress = False






