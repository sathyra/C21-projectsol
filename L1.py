import numpy as np
from tkinter import *
root=Tk()
root.geometry("600x400")
arr1 = np.array([3, 2, 0, 1])
arr2 = np.array(['banana', 'cherry', 'apple'])

#Defining the sorting function
def srt_ar_asc():
    newarr3 = np.sort(arr1)
    label.config(text=newarr3)

def srt_ar_dsc():
    newarr3 = -np.sort(-arr1)
    label.config(text=newarr3)

def srt_txt_asc():
    newarr4 = np.sort(arr2)
    label.config(text=newarr4)

#display the array elements
Message(root, text= arr1,bg='light blue', font = 50).pack()

#ascending button
Button(root, text="Sort Array Ascending", command=srt_ar_asc).pack(pady=20)

#descending button
Button(root, text="Sort Array Descending", command=srt_ar_dsc).pack(pady=20)

#Button and text elements
Message(root, text= arr2,bg='light blue', font = 50).pack()
Button(root, text="Sort Text", command=srt_txt_asc).pack(pady=20)

#output is displayed using the label
label = Label(root,width = 35, bg='light blue', font = 50)
label.pack()
root.mainloop()
