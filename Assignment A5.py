#Mason Thomas
#Assignment A5
#GUI Dev

import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

#Goobal holders
imageFile = None

#Create Window
root = Tk()
root.title("Payroll Every Two Weeks")
root.geometry("750x600")

#Display Instructions
title = Label(text = "Comic Convention Registration")
title.place(relx=.8, rely=.1, anchor=CENTER)
subTitle = Label(text = "Comic Convention Registration")
subTitle.place(relx=.5, rely=.4, anchor=CENTER)

#Picture Frame
pic = ttk.Frame(root, width=750,height=200)
pic.grid(column=0,row=0)
pic.configure(borderwidth="2")
pic.configure(relief="groove")

#Radio Boxes
v = IntVar()
tk.Label(root, text="Select Badge Type:").place(relx=.3, rely=.55, anchor=W)

tk.Radiobutton(root, text="Convetion + Superhero Experience", variable=v, value=380).place(relx=.3, rely=.6, anchor=W)
tk.Radiobutton(root, text="Convention + Autograpghs", variable=v,value=275).place(relx=.3, rely=.65, anchor=W)
tk.Radiobutton(root, text="Convention", variable=v,value=209).place(relx=.3, rely=.7, anchor=W)





class PriceCalculator:
    def __init__(self, master):
        global imageFile
        
        imageFile = "comic.png"

        frame = pic
        img = Image.open(imageFile)
        photo = ImageTk.PhotoImage(img.resize((750,200)))
        lblImage = ttk.Label(frame, image = photo)
        lblImage.image = photo
        lblImage.place(relx=.5,rely=.5,anchor=CENTER)

        self.label_groupSize = tk.Label(master, text="Group Size:")
        self.label_groupSize.place(relx=.3, rely=.5, anchor=CENTER)

        self.label_regCost = tk.Label(master, text="Registration Cost:")
        self.label_regCost.place(relx=.5, rely=.9, anchor=CENTER)

        self.groupSize = tk.Entry(master)
        self.groupSize.place(relx=.7, rely=.5, anchor=CENTER)

        self.button_clear = tk.Button(master, text="Clear", command=self.btnClear)
        self.button_clear.place(relx=.6, rely=.8, anchor=CENTER)

        self.button_calculate = tk.Button(master, text="Calculate", command=self.btnCalculate)
        self.button_calculate.place(relx=.4, rely=.8, anchor=CENTER)


    def btnClear(self):
        self.groupSize.delete(0, tk.END)
        self.label_regCost.config(text="Registration Cost:")

    def btnCalculate(self):
        groupSize = int(self.groupSize.get())

        if(groupSize <= 20):
            selection = int(v.get())
            rc = selection * groupSize
            self.label_regCost.config(text="Registration Cost: ${:.2f}".format(rc))
        else: 
            print("Error", "Invalid input. Please enter a valid group size.")
            


app = PriceCalculator(root)
root.mainloop()
