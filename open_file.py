from tkinter import *
from tkinter import filedialog as fd
import tkinter
from tkinter import messagebox

from PIL import Image, ImageTk

def insert_text():
    global file_name_open
    global image
    global width
    global height
    file_name_open = fd.askopenfilename()
    image = Image.open (file_name_open)
    photo = ImageTk.PhotoImage(image)
    width=photo.width()
    height=photo.height()
    canvas = tkinter.Canvas(root, height=height, width=width)
    image1 = canvas.create_image(0, 0, anchor='nw', image=photo)
    canvas.grid(row=4, column=1, columnspan=10)
    root.mainloop()
#    image.show()
#    f = open(file_name)
 #   s = f.read()
#    text.insert(1.0, s)
#    f.close()



def extract_text():
    file_name = fd.asksaveasfilename(
        filetypes=(("JPG files", "*.jpg"),("All files", "*.*")))
    Image.open(file_name_open).save(file_name)
    # f = open(file_name, 'w')
    # s = text.get(1.0, END)
    # f.write(s)
    # f.close()

def resizex2():
    x=int(resize1_entry.get())
    width_1=int(width/x)
    height_1=int(height/x)
    resized_image = image.resize((width_1,height_1))
    photo1 = ImageTk.PhotoImage(resized_image)

    # width2 = photo1.width()
    # height2 = photo1.height()
    # canvas = tkinter.Canvas(root, height=height2, width=width2)
    # image2 = canvas.create_image(0, 0, anchor='nw', image=photo1)
    # canvas.grid(row=2, column=1)
    # root.mainloop()

    file_name = fd.asksaveasfilename(filetypes=(("JPG files", "*.jpg"), ("All files", "*.*")), defaultextension='.jpg')
    resized_image.save(file_name)
    #Image.open(photo1).save(file_name)

root = Tk()
root.geometry("400x500")
# text = Text(width=50, height=25)
# text.grid(columnspan=2)
b1 = Button(text="Открыть", command=insert_text)
b1.grid(row=1, column=0, sticky=W)
b2 = Button(text="Сохранить", command=extract_text)
b2.grid(row=1, column=1, sticky=W)
#Уменьшить в 2 раза
lbl_res = Label(root, text="Во сколько раз уменьшить:")
lbl_res.grid(column=0, row=2, columnspan=2)
resize1 = StringVar()
resize1_entry = Entry(textvariable=resize1)
resize1_entry.grid(row=2, column=2, columnspan=2)
b3 = Button(text="Уменьшить", command=resizex2)
b3.grid(row=1, column=2, sticky=W)

root.mainloop()