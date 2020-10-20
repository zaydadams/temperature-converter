from tkinter import *

root = Tk()
root.geometry("650x400")
root.title("Temperature Unit Convertor")

labelfr_1 = Frame(root)
labelfr_1.pack()

labelfr_2 = Frame(root)
labelfr_2.pack()

num_1 = IntVar
num_2 = IntVar

labelfr_1 = LabelFrame(root, text = "Degrees Celcuis" , padx=48, pady=48)
labelfr_1.pack(fill="both")
labelfr_1 .place(x = 20, y = 10)
entryfr_1 = Entry(labelfr_1, state="disable")
entryfr_1.pack()

labelfr_2 = LabelFrame(root, text = "Degrees faranheit" ,padx=48, pady=48)
labelfr_2.pack(fill="both")
labelfr_2 .place(x = 350 , y = 10)
entryfr_2 = Entry(labelfr_2, state="disable")
entryfr_2.pack()

def active_1():
    entryfr_1.configure(state="normal")

entryfr_1_btn=Button(root, text="Activate-Faranheit to Celcuis", command=active_1)
entryfr_1_btn.pack()
entryfr_1_btn.place(x = 20, y = 150)


def active_1():
    if entryfr_1:
        num1= float(entryfr_1.get())
        num2= (num1*9/5)+32
        answer.insert(0, float(num2))

cal1_btn=Button(root, text="Calculate F-C", command=active_1)
cal1_btn.pack(side=LEFT)
cal1_btn.place(x = 50, y = 270)


def active2():
    if entryfr_2:
        num2= float(entryfr_2.get())
        num1= (num2-32)*5/9
        answer.insert(0, float(num1))

def active_1():
    entryfr_2.configure(state="normal")

entryfr_2_btn=Button(root, text="Activate-Celcuis to Faranheit", command=active_1)
entryfr_2_btn.pack()
entryfr_2_btn.place(x = 350, y = 150)

cal_btn=Button(root, text="Calculate C-F", command=active2)
cal_btn.pack(side=LEFT)
cal_btn.place(x = 50, y = 300)

answer=Entry(root, text="", background="lime")
answer.pack()
answer.place(x = 250, y = 270)

def clear_all_num():
    entryfr_1.delete(0,END)
    entryfr_2.delete(0,END)
    answer.delete(0,END)

clear_btn=Button(text="clear", command=clear_all_num)
clear_btn.pack()
clear_btn.place(x = 480, y = 350)

def escape_program():
    root.destroy()
exit_btn=Button(text="Exit" ,command=escape_program)
exit_btn.pack()
exit_btn.place(x = 550, y = 350)

root.mainloop()









