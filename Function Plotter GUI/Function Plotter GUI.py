# Hesham Mohamed Mohamed
# December 2021
from tkinter import *
from tkinter import ttk
from matplotlib import pyplot as plt
from matplotlib.pyplot import plot
from matplotlib.pyplot import figure

root = Tk()
root.title("Function Plotter GUI")
root.geometry("370x450")

photo=PhotoImage(file='image02.png')
resize_photo=photo.subsample(1,1)
# input part
top_label = ttk.Label(root, image=resize_photo, borderwidth=2, relief="groove").grid(row=0, column=0, columnspan=2, sticky='snew', pady=20, padx=20)
exp_label = ttk.Label(root, text='Exp.').grid(row=1, column=0, sticky='nw', pady=10, padx=20)
min_label = ttk.Label(root, text='mini').grid(row=3, column=0, sticky='nw', pady=10, padx=20)
max_label = ttk.Label(root, text='max').grid(row=5, column=0, sticky='nw', pady=10, padx=20)
step_label = ttk.Label(root, text='steps').grid(row=7, column=0, sticky='nw', pady=10, padx=20)
exp_entry = ttk.Entry(root)
min_entry = ttk.Entry(root)
max_entry = ttk.Entry(root)
step_entry = ttk.Entry(root)
exp_entry.grid(row=2, column=0, padx=20)
min_entry.grid(row=4, column=0, padx=20)
max_entry.grid(row=6, column=0, padx=20)
step_entry.grid(row=8, column=0, padx=20)
# Notes part
note_label = ttk.Label(root, text='notes', anchor='center').grid(row=1, column=1)
m= StringVar()
m_label = ttk.Label(root, textvariable=m, anchor='nw')
m_label.grid(row=2, rowspan=7, column=1, sticky='nw')
# button
buGo = Button(root, text='GO', bg = "#00FF00", fg='black', font='sans 12 bold')
buGo.grid(row=9, rowspan=2, column=0, sticky='snew', pady=10, padx=20)


class fplotte:
    def __init__(self, fun, maxX, minX, steps):
        self.fun = ''
        self.max = 0
        self.min = 0
        self.steps = 1
        self.rangeX = 0
        self.exp = 0.0
        self.x_axis = []  # values of x on axis
        self.values = []  # to store all y values

    def note_box(self, message):
        m.set(message)

    def clear_message(self):
        m.set('')

    def check_function(self):
        # first check
        if format(exp_entry.get()) == '' or format(max_entry.get()) == '' or \
                format(min_entry.get()) == '' or format(step_entry.get()) == '':
            message1 = "Please Enter all required inputs\n"
            self.note_box(message1)
            return False
        elif str(exp_entry.get()) is False or format(max_entry.get()).isdecimal() is False or \
                format(min_entry.get()).isdecimal() is False or format(step_entry.get()).isdecimal() is False:
            message2 = ("Please Enter valid inputs:\n"
                        "Exp ==> String\n"
                        "Mini ==> Integer\n"
                        "Max ==> Integer\n"
                        "Steps ==> Integer\n")
            self.note_box(message2)
            return False
        elif int(format(min_entry.get())) >= int(format(max_entry.get())):
            message3 = "Please Enter maximum bigger than the minimum\n"
            self.note_box(message3)
            return False

        # second check
        temp = str(format(exp_entry.get()))
        for i in temp:
            if (48 <= ord(i) <= 57) or (42 <= ord(i) <= 47) or (ord(i) == 120) or (ord(i) == 94):
                continue
            else:
                message4 = "expression is non-defined ,\nplease Enter only: \n\n-numbers\n-operators[+-/*^]" \
                           "\n-variable x) "
                self.note_box(message4)
                return False
        return True

    def put_values(self):
        self.fun = str(format(exp_entry.get()))
        self.max = int(format(max_entry.get()))
        self.min = int(format(min_entry.get()))
        self.steps = int(format(step_entry.get()))
        self.rangeX = ( self.max - self.min ) / self.steps

    def values_of_x(self):
        self.fun = self.fun.replace('^', '**')
        x = self.min
        while self.max >= x:
            self.x_axis.append(x)
            self.exp = eval(self.fun)
            self.values.append(self.exp)
            x += self.rangeX
        return True

    def plot_fun(self):
        # fig = Figure(figsize=(3.5, 3.5), dpi=100)
        # plot1 = fig.add_subplot(111)
        plt.plot(self.x_axis, self.values, c='r', marker='o')
        plt.show()


    def run_function(self):
        # Clearing notes box
        self.clear_message()
        # Checking function
        if self.check_function() is False:
            return False
        self.put_values()
        # Calculate the values
        self.values_of_x()
        self.plot_fun()

def activate():
    member = fplotte(format(str(exp_entry.get())), format(max_entry.get()), format(min_entry.get()),
                     format(step_entry.get()))
    member.run_function()

buGo.config(command=lambda: activate())

root.mainloop()
