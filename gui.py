#!/usr/bin/env python3
from files import FileOperation
from settings import Settings
from tkinter import *
from tkinter import ttk, filedialog

class Gui:
    def __init__(self,size_x : int, size_y : int): 

        # creates settings
        self.settings = Settings()

        # create files.py instance and adds saved paths if they exist
        if self.settings.is_configs_exists():
            paths = self.settings.read_options()
            self.files_operations = FileOperation(source_path=paths['source_path'], desination_path=paths['dest_path'], old_path=paths['old_path']) 
        else:
            self.files_operations = FileOperation()


        # window initzializtaion
        self.root = Tk()
        size = str(size_x) + "x" + str(size_y)
        self.root.geometry(size)
        self.root.title("Music to usb stick")

        # selected dirs
        self.selected_source = StringVar(value=self.files_operations.source_path)
        self.selected_dest = StringVar(value=self.files_operations.desination_path)
        self.selected_old = StringVar(value=self.files_operations.old_path)

        # mainframe
        self.mainframe = ttk.Frame(self.root)
        self.mainframe.grid(row=0, column=0, rowspan=6, columnspan=3, sticky=(W,N,E,S))

        # source label
        self.label_source = Label(self.mainframe, text="Source directory:")
        self.label_source.grid(row=2, column=0, sticky=(W,E))
        
        # destination label
        
        self.label_dest = Label(self.mainframe, text="Destination directory:")
        self.label_dest.grid(row=4, column=0, sticky=(E))

        # old labael
        
        self.label_old = Label(self.mainframe, text="Old mp4 files directory:")
        self.label_old.grid(row=6, column=0, sticky=(E))

        # choose source

        self.select_source = Button(self.mainframe, textvariable=self.selected_source, command=self.select_source)
        self.select_source.grid(row=2,column=6)

        # choose dest

        self.select_dest = Button(self.mainframe, textvariable=self.selected_dest, command=self.select_dest)
        self.select_dest.grid(row=4,column=6)
        
        # choose old
        self.select_old = Button(self.mainframe, textvariable=self.selected_old, command=self.select_old)
        self.select_old.grid(row=6,column=6)

        # save options

        self.save_options_var = IntVar(value=0)
        self.save_options = ttk.Checkbutton(self.mainframe, text="Save options", variable=self.save_options_var, onvalue=1, offvalue=0, command=lambda: self.save_options_to_a_file(self.files_operations.source_path, self.files_operations.desination_path, self.files_operations.old_path))
        self.save_options.grid(row=8, column=0)




        # padding
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5) 

        self.root.mainloop()
    


    # additional methods
    def save_options_to_a_file(self, source_path : str, dest_path : str, old_path : str):
        if self.save_options_var.get() == 1:
            print("Saving options...")
            self.settings.save_options(source_path, dest_path, old_path)
        else: 
            print("Deleting saved options...")
            self.settings.remove_options()

    def select_directory(self):
        selected = filedialog.askdirectory()
        print("User choose", selected, " directory")
        return selected

    def select_source(self):
        path = self.select_directory()
        self.files_operations.source_path = path
        self.selected_source.set(path)

    def select_dest(self):
        path = self.select_directory()
        self.files_operations.desination_path = path
        self.selected_dest.set(path)

    def select_old(self):
        path = self.select_directory()
        self.files_operations.old_path = path
        self.selected_old.set(path)

gui = Gui(600, 600)
