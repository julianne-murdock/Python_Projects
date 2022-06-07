#
# Author: Julianne Murdock
#
# Date: June 7th 2022
#
# Purpose: Create a Python script that will allow the user
# of a file transfer program to have a better UI: choose specific
# folders to be checked daily, browse folder that will receive the 
# copied files, allow user to inititate the file check process.
#
import tkinter as tk
from tkinter import *
import shutil
import os
import time
from datetime import datetime, timedelta
from tkinter import filedialog as fd

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry('{}x{}'.format(800, 500))
        self.master.title('File Transfer Assignment') #Title of window. 
        self.master.config(bg='#9fbfdf')
        self.lblSource = Label(self.master, text='Source Folder:  ', font=('Arial', 12,), fg = 'black', bg='#9fbfdf' ) 
        self.lblSource.grid(row=0, column=0, padx=(30,0), pady=(30,0)) 
        self.lblDestination = Label(self.master, text='Destination Folder ', font=('Arial', 12,), fg = 'black', bg='#9fbfdf' ) 
        self.lblDestination.grid(row=1, column=0, padx=(30,0), pady=(30,0)) 
        self.txtWeb = Entry(self.master, font=('Arial', 12,), fg = 'black', bg='lightblue')  
        self.txtWeb.grid(row=0, column=1, padx=(10,0), pady=(30,0))
        self.txtWeb2 = Entry(self.master, font=('Arial', 12,), fg = 'black', bg='lightblue')  
        self.txtWeb2.grid(row=1, column=1, padx=(10,0), pady=(30,0)) 
        self.btnSource = Button(self.master, text ="Source", width= 10, height=2, command = self.chooseSource) #This connects the button to the chooseSource function below
        self.btnSource.grid(row=2, column=0, padx=(30,0), pady=(30,0), sticky=S)  
        self.btnDestination = Button(self.master, text ="Destination", width= 10, height=2, command = self.chooseDestination) #This connects the button to the chooseDestination function below
        self.btnDestination.grid(row=2, column=2, padx=(0,0), pady=(30,0), sticky=S)  
        self.btnTransfer = Button(self.master, text ="Transfer", width= 10, height=2, command = self.fileTransfer) #This calls the file transfer function which transfers the file. 
        self.btnTransfer.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=N)

    def chooseSource(self):
        src = fd.askdirectory() #function that lets you to search a directory
        self.txtWeb.delete(0, END) #clears the entry box
        self.txtWeb.insert(0, src) #puts the file into the entry box
    
    def chooseDestination(self):
        dest = fd.askdirectory()
        self.txtWeb2.delete(0, END)
        self.txtWeb2.insert(0, dest)

    def fileTransfer(self):
        source = self.txtWeb.get() #input is read from line one to character zero
        destination = self.txtWeb2.get() #input is read from line one to character zero
        files = os.listdir(source)

        for i in files:
            #gets the absolute path to the file
            absolutePath = os.path.join(source, i)
            #gets the modification time
            mtime = os.path.getmtime(absolutePath)
            #converts the modification time to a date and time format.
            modTime=datetime.fromtimestamp(mtime)
            current = datetime.now()
            twentyFour = current - timedelta(hours=24)
            if modTime > twentyFour:
                shutil.move(absolutePath, destination)
        
if __name__ == "__main__":
    root = tk.Tk() #syntax to create a window from the tkinter
    App = ParentWindow(root)#App is the class, root is the tkninter window
    root.mainloop() #This will loop the code so that it remains on the page