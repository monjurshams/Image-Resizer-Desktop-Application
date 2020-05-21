from tkinter import *
from tkinter import filedialog
import cv2
from tkinter import messagebox
import pkg_resources.py2_warn

class FrontEnd(object):
    def __init__(self,root):
        
        self.L1  = Label(root,text = "Select your Image")
        self.L1.grid(row = 0, column = 0)

        self.list1 = Listbox(root,height =1,width =40)
        self.list1.grid(row =0, column = 1)
        
        self.b1 = Button(root, text='Open Browser', command=self.UploadAction)
        self.b1.grid(row = 1,column=0 )
        
        self.L2  = Label(root,text = "Original Height[px]")
        self.L2.grid(row = 2, column = 0)
        self.list2 = Listbox(root,height =1,width =20)
        self.list2.grid(row =2, column = 1)

        self.L3  = Label(root,text = "Original Width[px]")
        self.L3.grid(row = 3, column = 0)
        self.list3 = Listbox(root,height =1,width =20)
        self.list3.grid(row =3, column = 1)

        self.L4  = Label(root,text = "Enter new height[px]")
        self.L4.grid(row = 5, column = 0)

        self.height = StringVar()
        self.E1 = Entry(root,textvariable = self.height)
        self.E1.grid(row = 5, column=1)

        self.L5  = Label(root,text = "Enter new width[px]")
        self.L5.grid(row = 6, column = 0)

        self.width = StringVar()
        self.E2 = Entry(root,textvariable = self.width )
        self.E2.grid(row = 6, column=1)

        
        self.L6  = Label(root,text = "Enter new file name")
        self.L6.grid(row = 7, column = 0)

        self.name = StringVar()
        self.E3 = Entry(root,textvariable = self.name )
        self.E3.grid(row = 7, column=1)
        self.L7  = Label(root,text = ".jpg")
        self.L7.grid(row = 7, column = 2,columnspan = 2)

        self.b2 = Button(root, text='Convert', command=self.ConvertImage)
        self.b2.grid(row = 8,column=0 )

        
    def UploadAction(self,event=None):
        self.filename = filedialog.askopenfilename()
        self.list1.delete(0,END)
        self.list1.insert(END,self.filename)
        self.img  = cv2.imread(self.filename)
        
        self.list2.delete(0,END)
        self.list2.insert(END,self.img.shape[0])
        self.list3.delete(0,END)
        self.list3.insert(END,self.img.shape[1])

    def ConvertImage(self):
        self.new_height = int(self.height.get())
        self.new_width = int(self.width.get())
        self.new_name = str(self.name.get()+".jpg")
        if(self.new_height<self.img.shape[0] and self.new_width<self.img.shape[1] ):
            self.resized_image = cv2.resize(self.img,(self.new_height,self.new_width))
            cv2.imwrite(self.new_name,self.resized_image) 
            messagebox.showinfo("Image Converter", "Converting Done!")
        else:
            messagebox.showinfo("Image Converter", "Converting Error, Please check the new sizes")
        


root = Tk()
root.wm_title("Image Resizer")
FrontEnd(root)
root.mainloop()