from tkinter import filedialog, messagebox, Tk, Text, END
import numpy as np
import matplotlib.pyplot as plt


def get_text_result(slope, slope_err, intercept, intercept_err, corr_coef):
    window = Tk()
    window.title("Data result")
    text_answer = Text(window)

    text_answer.insert(END, "Resultados del ajuste lineal:\n"
                       "Pendiente: {} +/- {}\n"
                       "Ordenada en el origen: {} +/- {}\n"
                       "Coeficiente de correlación (R): {}"
                       .format(slope, slope_err, intercept,
                               intercept_err, corr_coef))
    text_answer.pack()


def calculate_data(x, y, el1, el2):
    x = np.array([float(x1) for x1 in x]) * (10 ** el1)
    y = np.array([float(y1) for y1 in y]) * (10 ** el2)
    # x = np.array([float(x1) for x1 in x])
    # y = np.array([float(y1) for y1 in y])

    slope, intercept = np.polyfit(x, y, 1)
    residuals = y - (slope * x + intercept)
    mse = np.sum(residuals ** 2) / (len(x) - 2)
    slope_err = np.sqrt(
        len(x) * mse / (len(x) * np.sum(x ** 2) - np.sum(x) ** 2))
    intercept_err = np.sqrt(mse * np.sum(x ** 2) / (
            len(x) * np.sum(x ** 2) - np.sum(x) ** 2))
    corr_coef = np.corrcoef(x, y)[0, 1]

    return slope, slope_err, intercept, intercept_err, corr_coef, x, y


def get_graph_and_data(x, y, figure, xlabel, ylabel, el1, el2):
    slope, slope_err, intercept, intercept_err, \
        corr_coef, x, y = calculate_data(x, y, el1, el2)

    get_text_result(slope, slope_err, intercept, intercept_err, corr_coef)

    plt.figure(figure)
    plt.scatter(x, y, color='blue', label='Datos')
    plt.plot(x, slope * x + intercept, color='red',
             label='Ajuste lineal')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    plt.legend()
    plt.show()


def browse_files(variable):
    # TODO select type csv and txt only
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",)
    variable.set(filename)


def check_button(event, x, y, explore):
    if event:
        explore.config(state="normal")
        x.delete(0, 'end')
        x.config(state='disabled')

        y.delete(0, 'end')
        y.config(state='disabled')

    else:
        explore.config(state="disabled")
        x.config(state='normal')
        y.config(state='normal')


def get_result_button(box, x, y, file, figure, xlabel, ylabel, el1, el2):
    if box:
        file = file.get()
        file_path = file
        if len(file) == 0:
            messagebox.showerror(title='Data error...',
                                 message='No files selected')
        else:

            file = open(file, 'r')
            x, y = file.readlines()
            x = x.split()
            y = y.split()

            if len(x) != len(y):
                messagebox.showerror(title='Data error...',
                                     message=f'Different amount of data in the'
                                             f' file for x and y in the:'
                                             f' {file_path}')
            else:
                get_graph_and_data(x, y, figure, xlabel, ylabel, el1, el2)

    else:
        x = x.get().split()
        y = y.get().split()

        if len(x) != len(y):
            messagebox.showerror(title='Data error...',
                                 message=f'Different amount of data were given.'
                                         f'\n Length of x -> {len(x)}'
                                         f' of y -> {len(y)}')

        else:
            if len(x) == 0:
                messagebox.showerror(title='Data error...',
                                     message='No data was inputed')
            else:
                get_graph_and_data(x, y, figure, xlabel, ylabel, el1, el2)


