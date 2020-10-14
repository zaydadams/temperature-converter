from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("620x300")
root.title("Temperature Unit Convertor")

labelframe_c = LabelFrame(root, text = "Celcuis to Fahrenheit" , padx=48, pady=48)
labelframe_c.pack(fill="both")
labelframe_c .place(x = 20, y = 10)
entry_c = Entry(labelframe_c)
entry_c.pack()

labelframe_f = LabelFrame(root, text = "Fahrenheit to Celcuis" ,padx=48, pady=48)
labelframe_f.pack(fill="both")
labelframe_f .place(x = 300 , y = 10)
entry_f = Entry(labelframe_f)
entry_f.pack()

button_c =Button(root, text = "Activate-Celcuis to Fahrenheit")
button_c .place(x = 20, y = 180)

button_f = Button(root, text = "Activate-Fahrenheit to Celcuis")
button_f .place(x = 300, y =180)

btn_Calculate =Button(root, text ="Calculate Conversion")
btn_Calculate .pack()
btn_Calculate .place(x = 20 , y = 250)

btn_result= Entry(root, bg ="green2" ,)
btn_result .pack()
btn_result .place(x = 200 , y = 250 )

root.mainloop()
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
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

labelfr_1 = LabelFrame(root, text = "Celcuis to Fahrenheit" , padx=48, pady=48)
labelfr_1.pack(fill="both")
labelfr_1 .place(x = 20, y = 10)
entryfr_1 = Entry(labelfr_1, state="disable")
entryfr_1.pack()

labelfr_2 = LabelFrame(root, text = "Fahrenheit to Celcuis" ,padx=48, pady=48)
labelfr_2.pack(fill="both")
labelfr_2 .place(x = 350 , y = 10)
entryfr_2 = Entry(labelfr_2, state="disable")
entryfr_2.pack()

def active_1():
    entryfr_1.configure(state="normal")

entryfr_1_btn=Button(root, text="Activate-Faranheit to Celcuis", command=active_cel)
entryfr_1_btn.pack()
entryfr_1_btn.place(x = 128, y = 150)

def convert():
    if entryfr_1:
        num1= float(entryfr_1.get())
        num2= (num1*9/5)+32
        answer.insert(0, float(num2))

def convert1():
    if entryfr_2:
        num2= float(entryfr_2.get())
        num1= (num2-32)*5/9
        answer.insert(0, float(num1))

def active_cel():
    entryfr_2.configure(state="normal")

entryfr_2_btn=Button(root, text="Activate-Celcuis to Faranheit", command=active_cel)
entryfr_2_btn.pack()
entryfr_2_btn.place(x = 128, y = 150)

cal_btn=Button(root, text="Calculate conversion", command=convert)
cal_btn.pack(side:left)
cal_btn.place


button_1 =Button(root, text = "Activate-Celcuis to Fahrenheit")
button_1 .place(x = 20, y = 180)

button_2 = Button(root, text = "Activate-Fahrenheit to Celcuis")
button_2 .place(x = 350, y =180)

button_3 = Button(root, text ="clear")
button_3 .place(x = 500, y = 300)

button_4 = Button(root, text ="exit")
button_4 .place(x = 500, y = 350)

btn_Calculate =Button(root, text ="Calculate Conversion")
btn_Calculate .pack()
btn_Calculate .place(x = 20 , y = 250)

btn_result= Entry(root, bg ="green2" ,)
btn_result .pack()
btn_result .place(x = 200, y = 260 )



root.mainloop()






