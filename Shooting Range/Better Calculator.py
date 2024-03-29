#Holy shit i bin so a pro

from tkinter import *


def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + float(second_number))

    if math == "subtraction":
        e.insert(0, f_num - float(second_number))

    if math == "multiplication":
        e.insert(0, f_num * float(second_number))

    if math == "division":
        e.insert(0, f_num / float(second_number))

def button_dot():
    e.insert(END, ".")

# Creating Lable
root = Tk()
root.title("Better Calculator by @RonaldMcDonald14")
root.geometry("302x432")

#Autoresize
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)


# Creating Entry
e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


#Define buttons
button1 = Button(root, text="1", padx=42, pady=20, bg="#202020", fg="white",  command=lambda: button_click(1))
button2 = Button(root, text="2", padx=42, pady=20, bg="#202020", fg="white", command=lambda: button_click(2))
button3 = Button(root, text="3", padx=42, pady=20, bg="#202020", fg="white", command=lambda: button_click(3))
button4 = Button(root, text="4", padx=42, pady=20, bg="#202020", fg="white", command=lambda: button_click(4))
button5 = Button(root, text="5", padx=42, pady=20, bg="#202020", fg="white", command=lambda: button_click(5))
button6 = Button(root, text="6", padx=42, pady=20, bg="#202020", fg="white", command=lambda: button_click(6))
button7 = Button(root, text="7", padx=42, pady=20, bg="#202020", fg="white", command=lambda: button_click(7))
button8 = Button(root, text="8", padx=42, pady=20, bg="#202020", fg="white", command=lambda: button_click(8))
button9 = Button(root, text="9", padx=42, pady=20, bg="#202020", fg="white", command=lambda: button_click(9))
button0 = Button(root, text="0", padx=42, pady=20, bg="#202020", fg="white", command=lambda: button_click(0))

button_add = Button(root, text="+", padx=41, pady=20, bg="#404040", fg="white", command=button_add)
button_sub = Button(root, text="-", padx=43, pady=20, bg="#404040", fg="white", command=button_subtract)
button_mul = Button(root, text="*", padx=42, pady=20, bg="#404040", fg="white", command=button_multiply)
button_div = Button(root, text="/", padx=42, pady=20, bg="#404040", fg="white", command=button_divide)
button_equal = Button(root, text="=", padx=92, pady=20, bg="#404040", fg="white", command=button_equal)
button_clear = Button(root, text="Clear", padx=32, pady=20, bg="#404040", fg="white", command=button_clear)
button_dot = Button(root, text=".", padx=43.2, pady=20, bg="#404040", fg="white", command=button_dot)

# Put buttons on screen

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=1)

button_add.grid(row=4, column=0)
button_sub.grid(row=5, column=0)
button_mul.grid(row=4, column=2)
button_div.grid(row=5, column=2)
button_equal.grid(row=6, column=1, columnspan=2)
button_clear.grid(row=6, column=0)
button_dot.grid(row=5, column=1)

root.mainloop()
