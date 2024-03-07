#!/usr/bin/env python3
from files import FileOperation
from tkinter import *
from tkinter import ttk, filedialog

class Gui:
    def __init__(self,size_x : int, size_y : int): 

        # create files.py instance
        self.files_operations = FileOperation() 


        # window initzializtaion
        self.root = Tk()
        size = str(size_x) + "x" + str(size_y)
        self.root.geometry(size)
        self.root.title("Music to usb stick")

        # selected dirs
        self.selected_source = StringVar(value=self.files_operations.source_path)
        self.selected_dest = StringVar(value=self.files_operations.desination_path)
        self.selected_old = StringVar(value=self.files_operations.changed_files_path)

        # mainframe
        self.mainframe = ttk.Frame(self.root)
        self.mainframe.grid(row=0, column=0, rowspan=6, columnspan=3, sticky=(W,N,E,S))

        # source label
        self.label_source = Label(self.mainframe, text="Source directory:")
        self.label_source.grid(row=0, column=0, sticky=(W,E))
        
        # destination label
        
        self.label_dest = Label(self.mainframe, text="Destination directory:")
        self.label_dest.grid(row=1, column=0, sticky=(E))

        # old labael
        
        self.label_old = Label(self.mainframe, text="Old mp4 files directory:")
        self.label_old.grid(row=2, column=0, sticky=(E))

        # choose source

        self.select_source = Button(self.mainframe, textvariable=self.selected_source, command=self.select_source)
        self.select_source.grid(row=0,column=3)

        # choose dest

        self.select_dest = Button(self.mainframe, textvariable=self.selected_dest, command=self.select_dest)
        self.select_dest.grid(row=1,column=3)
        
        # choose old
        self.select_old = Button(self.mainframe, textvariable=self.selected_old, command=self.select_old)
        self.select_old.grid(row=2,column=3)

        self.root.mainloop()

    def select_directory(self):
        selected = filedialog.askdirectory()
        print("User choose", selected, " directory")
        return selected

    def select_source(self):
        self.selected_source.set(self.select_directory())

    def select_dest(self):
        self.selected_dest.set(self.select_directory())

    def select_old(self):
        self.selected_old.set(self.select_directory()) 
gui = Gui(600, 600)
