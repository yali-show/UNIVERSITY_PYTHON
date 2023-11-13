import logic
from tkinter import *
# from tkinter import ttk
from ttkbootstrap import Style, ttk
import time
# import platform


class WidgetControlInputs:
    def __init__(self, root):
        self.root = root
        self.figure = 1
        self.file_path = StringVar()
        self.checkbox_var = IntVar()
        self.setup()

    def get_result_for_button_different_figures(self, box, x, y, file, labels, elevados):
        self.figure += 1
        logic.get_result_button(box, x, y, file, self.figure, *labels, *elevados)

    def setup(self):
        row_x = ttk.Entry(self.root)

        row_x_label = ttk.Entry(self.root)
        row_x_label.insert(0, "Title for eje X")

        row_x_spin = ttk.Spinbox(self.root, from_=-100, to=100, width=3)
        row_x_spin.delete(0, 'end')
        row_x_spin.insert(0, 0)

        row_y = ttk.Entry(self.root)

        row_y_label = ttk.Entry(self.root)
        row_y_label.insert(0, "Title for eje Y")

        row_y_spin = ttk.Spinbox(self.root, from_=-100, to=100, width=3)
        row_y_spin.delete(0, 'end')
        row_y_spin.insert(0, 0)

        button = ttk.Button(self.root, style='success.TButton', border_radius=10
                            text="Get result", width=50,
                        command=lambda:
                        self.get_result_for_button_different_figures(
                            self.checkbox_var.get(), row_x, row_y,
                            self.file_path,
                            labels=(row_x_label.get(), row_y_label.get()),
                            elevados=(int(row_x_spin.get()),
                                      int(row_y_spin.get()))
                             )
                        )

        button_explore = ttk.Button(self.root, width=20,
                                text="Browse Files",
                                command=lambda: logic.browse_files(self.file_path),
                                state="disabled")

        checkbox = ttk.Checkbutton(self.root,  text="From files",
                                   variable=self.checkbox_var,
                                   command=lambda var=self.checkbox_var:
                                   logic.check_button(var.get(),
                                                      row_x, row_y,
                                                      button_explore))



        row_x_label.grid(row=0, column=0)
        row_x_spin.grid(row=1, column=1)
        row_x.grid(row=1, column=0)

        row_y_label.grid(row=0, column=2)
        row_y_spin.grid(row=1, column=3)
        row_y.grid(row=1, column=2)

        checkbox.grid(row=2, column=2)

        button_explore.grid(row=2, column=0, columnspan=2)
        button.grid(row=3, columnspan=4)


class App:
    def __init__(self):
        self.root = Tk()

        self.style = Style(theme="minty")
        WidgetControlInputs(self.root)
        self.root.title("Calculadora fisica")
        self.root.geometry('500x120')
        self.root.mainloop()


App()
