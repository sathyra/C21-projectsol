
import numpy as np
from tkinter import *

root=Tk()
root.geometry("600x400")   
def sortarr():
    
    arr1 = np.array([3, 2, 0, 1])
    arr2 = np.array(['banana', 'cherry', 'apple'])

    def srt_ar_asc():
        #i = int(input1.get())
        newarr3 = np.sort(arr1)
        #print(INPUT1)
        label.config(text=newarr3)

    def srt_ar_dsc():
        #i = int(input1.get())
        newarr3 = -np.sort(-arr1)
        #print(INPUT1)
        label.config(text=newarr3)

    def srt_txt_asc():
        #i = int(input1.get())
        newarr4 = np.sort(arr2)
        #print(INPUT1)
        label.config(text=newarr4)

    Message(root, text= arr1,bg='light blue', font = 50).pack()
    Button(root, text="Sort Array Ascending", command=srt_ar_asc).pack(pady=20)

    Button(root, text="Sort Array Descending", command=srt_ar_dsc).pack(pady=20)

    Message(root, text= arr2,bg='light blue', font = 50).pack()
    Button(root, text="Sort Text", command=srt_txt_asc).pack(pady=20)
    label = Label(root,width = 35, bg='light blue', font = 50)
    label.pack(pady=20)
    # root.sortarr()

    root.mainloop()

button = Button( text ='Sorting Array', bd = '5', bg = 'yellow',command = sortarr())

### Main

# def close():
#     #top.destroy()
#     root.destroy()

# create a tkinter window
#root = Tk()             
 
# Open window having dimension 100x100
#root.geometry('500x200')
#root.title('NUMPY')

# button_dict = {}
# options = [ 'Sorting Array']

# for i in options:
    # def func(i):
        
#         if i == 'Sorting Array':
#             return sortarr
        # elif i == 'Exit':
        #     return close
        
# Create a Button
 
    # Set the position of button on the top of window.  
#button.pack()   
 
#root.mainloop()

