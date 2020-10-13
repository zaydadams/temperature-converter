from tkinter import *

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





