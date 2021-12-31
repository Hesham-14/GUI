from tkinter import *
from tkinter import ttk
from matplotlib.pyplot import plot
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

root = Tk()
root.title("Function Plotter GUI")
root.geometry("650x550")


# f1.place(in_ =root, anchor='c', relx=.5)

# function plotter class

class fplotte:
    def __init__(self, fun, maxX, minX, steps):
        self.fun = fun.lower()
        self.max = int(maxX)
        self.min = minX
        self.steps = int(steps)
        self.rangeX = (maxX - minX) / steps
        self.exp = 0.0
        self.x_axis = []  # values of x on axis
        self.values = []  # to store all y values

    def check_function(self):
        for i in self.fun:
            if (48 <= ord(i) <= 57) or (42 <= ord(i) <= 47) or (ord(i) == 120) or (ord(i) == 94):
                continue
            else:
                return False
        self.fun = self.fun.replace('^', '**')
        return True

    def values_of_x(self):

        x = self.min
        while self.max >= x:
            self.x_axis.append(x)
            self.exp = eval(self.fun)
            self.values.append(self.exp)
            x += self.rangeX
        return self.values


f1 = ttk.Frame(root, width=650, height=100, relief=RIDGE)  # Heading frame
f2 = ttk.Frame(root, width=250, height=400, relief=RIDGE)  # Input frame
f3 = ttk.Frame(root, width=400, height=300, relief=RIDGE)  # Plot frame
f4 = ttk.Frame(root, width=400, height=100, relief=RIDGE)  # message frame
f1.grid(row=0, column=0, columnspan=2)
f2.grid(row=1, rowspan=2, column=0)
f3.grid(row=1, column=1)
f4.grid(row=2, column=1)

# Frame 1 labels
exp_label = ttk.Label(f2, text='Exp.')
min_label = ttk.Label(f2, text='mini')
max_label = ttk.Label(f2, text='max')
step_label = ttk.Label(f2, text='steps')
exp_label.grid(row=0, column=1, sticky='nw')
min_label.grid(row=2, column=1, sticky='nw')
max_label.grid(row=4, column=1, sticky='nw')
step_label.grid(row=6, column=1, sticky='nw')

# Frame 1 Entries
exp_entry = ttk.Entry(f2)
min_entry = ttk.Entry(f2)
max_entry = ttk.Entry(f2)
step_entry = ttk.Entry(f2)
exp_entry.grid(row=1, column=1, columnspan=4)
min_entry.grid(row=3, column=1, columnspan=4)
max_entry.grid(row=5, column=1, columnspan=4)
step_entry.grid(row=7, column=1, columnspan=4)
buGo = ttk.Button(f2, text='GO')
buGo.grid(row=8, rowspan=2, column=1, columnspan=5, sticky='snew')

# frame 4 for error notes
note_label = ttk.Label(f4, text='notes', anchor='nw')
note_label.grid(row=0)
m= StringVar()
m_label = ttk.Label(f4, textvariable=m, anchor='nw')
m_label.grid(row=1)


# Required functions
def plot_fun(values, x_axis):
    fig = Figure(figsize=(3.5, 3.5), dpi=100)
    plot1 = fig.add_subplot(111)
    plot1.plot(x_axis, values, c='r', marker='o')
    plot1.show()
    # canvas = FigureCanvasTkAgg(fig, master=f3)
    # canvas.draw()
    # canvas.get_tk_widget().pack()

def clear_plot():
    del plot_fun

def note_box(message):
    m.set(message)


def clear_message():
    m.set('')

def run_function():
    clear_message()
    # Checking inputs
    if format(str(exp_entry.get())) == NONE or format(max_entry.get()) == NONE or \
            format(min_entry.get()) == NONE or format(step_entry.get()) == NONE:
        message1 = "Please Enter all required inputs\n"
        note_box(message1)
        return False
    # elif str(exp_entry.get()) != str or max_entry.get() != int or \
    #         min_entry.get() != int or step_entry.get() != int:
    #     message2 = ("Please Enter valid inputs:\n"
    #                 "Exp ==> String\n"
    #                 "Mini ==> Integer\n"
    #                 "Max ==> Integer\n"
    #                 "Steps ==> Integer\n")
    #     note_box(message2)
    #     return False

    # checking Max > min
    # if format(min_entry.get()) >= format(max_entry.get()):
    #     message3 = "Please Enter maximum bigger than the minimum\n"
    #     note_box(message3)
    #     return False

    # creating class object
    member = fplotte(format(str(exp_entry.get())), int(format(max_entry.get())), int(format(min_entry.get())),
                     int(format(step_entry.get())))

    # Checking function
    ck = member.check_function()
    if ck is False:
        message4 = "The expression has non-defined element, please Enter only: \n (numbers, operators[+-/*^], " \
                   "and variable x) "
        note_box(message4)
        return False
    print(member.values_of_x())

    plot_fun(member.values, member.x_axis)

def pressed():
    print('pressed')

# root.bind("<Return>", self.update_values)
# plot_fun(member.values, member.x_axis)
buGo.config(command=lambda: run_function())

root.mainloop()
