#
# Author: Julianne Murdock
#
# Date: May 14th 2022
#
# Purpose: Create a Python script that will automatically 
# create the .html file needed.
#
import webbrowser
import tkinter as tk
from tkinter import *

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry('{}x{}'.format(800, 500))
        self.master.title('Enter the title of the window here!') 
        self.master.config(bg='lightblue')

        self.txtWeb = Entry(self.master,text="web text", font=('Ariel', 11,), fg = 'black', bg='#CBC3E3')  
        self.txtWeb.grid(row=1, column=1, padx=(180,0), pady=(50,0)) 

        self.btnSubmit = Button(self.master, text ="Submit", width= 11, height=2, command=self.webGenerator) 
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(28,0), sticky=SE)  

    def webGenerator(self):
        g = open('WebPageGenerator.html', 'w')

        message1 = """ <html>
        <head></head>
        <body>"""

        message2 = self.txtWeb.get()
    
        message3 = """</body>
        </html>"""

        g.write(message1 + message2 + message3)
        g.close()

        webbrowser.open_new_tab('WebPageGenerator.html')
        
        
if __name__ == "__main__":
    root = tk.Tk() #Creates a window from tkinter
    App = ParentWindow(root)#App equals class, root equals tkninter window
    root.mainloop()