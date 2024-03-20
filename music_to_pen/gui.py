from .files import FileOperation
from .settings import Settings
from tkinter import *
from tkinter import ttk, filedialog, messagebox 

class Gui:
    def __init__(self,size_x : int, size_y : int): 

        # creates settings
        self.settings = Settings()

        # create files.py instance and adds saved paths if they exist
        paths = self.settings.read_options()
        self.files_operations = FileOperation(**paths) 

    

        # window initzializtaion
        self.root = Tk()
        size = str(size_x) + "x" + str(size_y)
        self.root.geometry(size)
        self.root.title("Music to usb stick")

        # # selected dirs
        self.selected_source = StringVar(value=self.files_operations.source_path)
        self.selected_dest = StringVar(value=self.files_operations.dest_path)
        self.selected_old = StringVar(value=self.files_operations.old_path)

        # mainframe
        self.mainframe = ttk.Frame(self.root)
        self.mainframe.grid(row=0, column=0, rowspan=6, columnspan=3, sticky=(W,N,E,S))
        self.mainframe.grid_columnconfigure(0,weight=1)

        # setting up content

        self.setup_source_frame()
        self.setup_settings_frame()
        self.setup_progessbar()
        self.setup_process_frame()


        # padding
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=10, pady=10) 

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
        selected = filedialog.askdirectory(mustexist=True)
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

    def setup_source_frame(self):
        
        # save vars
        self.save_source_var = IntVar()
        self.save_dest_var = IntVar()
        self.save_old_var = IntVar()

        # setting up label
        self.source_frame = ttk.LabelFrame(self.mainframe, text="Path options")
        self.source_frame.grid(row=2, column=0, columnspan=3, rowspan=12, sticky=(N, E, S, W))
        self.source_frame.grid_columnconfigure(index=0,weight=3)

        # setting up buttons

        self.label_source = Label(self.source_frame, text="Source directory:")
        self.label_source.grid(row=2, column=0, sticky=(W, E))
        self.select_source = Button(self.source_frame, textvariable=self.selected_source, command=self.select_source)
        self.select_source.grid(row=2, column=6)
        
        self.save_source = Checkbutton(self.source_frame, text="Save this path", onvalue=1, offvalue=0, variable=self.save_source_var) 
        self.save_source.grid(row=2, column=12)

        self.label_dest = Label(self.source_frame, text="Destination directory:")
        self.label_dest.grid(row=4, column=0, sticky=(W, E))
        self.select_dest = Button(self.source_frame, textvariable=self.selected_dest, command=self.select_dest)
        self.select_dest.grid(row=4, column=6)

        self.save_dest = Checkbutton(self.source_frame, text="Save this path", onvalue=1, offvalue=0, variable=self.save_dest_var)
        self.save_dest.grid(row=4, column=12)

        self.label_old = Label(self.source_frame, text="Old mp4 files directory:")
        self.label_old.grid(row=6, column=0, sticky=(W, E))
        self.select_old = Button(self.source_frame, textvariable=self.selected_old, command=self.select_old)
        self.select_old.grid(row=6, column=6)

        self.save_old = Checkbutton(self.source_frame, text="Save this path", onvalue=1, offvalue=0, variable=self.save_old_var)
        self.save_old.grid(row=6, column=12)
    
    def setup_settings_frame(self):
        # setting up label
        
        self.settings_frame = ttk.LabelFrame(self.mainframe, text="Saving options")
        self.settings_frame.grid(row=14, column=0, columnspan=3, rowspan=8, sticky=(N))
        self.settings_frame.grid_columnconfigure(index=0,weight=3)

        # setting up buttons

        self.save_options_btn = ttk.Button(self.settings_frame, text="Save options", command=lambda: self.save_selected())
        self.save_options_btn.grid(row=8, column=0, pady=10)

        self.remove_options_btn = ttk.Button(self.settings_frame, text="Remove saved options", command=lambda: self.settings.remove_options())
        self.remove_options_btn.grid(row=8, column=1, pady=10)

    def setup_process_frame(self):
        self.process_files_frame = ttk.LabelFrame(self.mainframe, text="Process files")
        self.process_files_frame.grid(row=24, column=0, pady=10, padx=10, sticky=(N))

        self.process_files_btn = ttk.Button(self.process_files_frame, text="Process files", command=lambda: self.process_files_with_progress())
        self.process_files_btn.grid(row=8, column=1)

    def setup_progessbar(self):
        self.progress_label = ttk.LabelFrame(self.mainframe)
        self.progress_label.grid(row=36, column=0, sticky=(N))

        self.progess_text = ttk.Label(self.progress_label)
        self.progess_text.grid(row=24, column=6)
        self.progess = ttk.Progressbar(self.progress_label, orient="horizontal", length=200, mode="determinate")
        self.progess.grid(row=18, column=6)


    def process_files_with_progress(self):
        self.files_operations.process_files_with_progress(self.progess, self.progess_text)
        
    def save_selected(self):
        source_path = self.selected_source.get() if self.save_source_var.get() == 1 else None
        dest_path = self.selected_dest.get() if self.save_dest_var.get() == 1 else None
        old_path = self.selected_old.get() if self.save_old_var.get() == 1 else None
        
        print(f"Saving paths - Source: {source_path}, Destination: {dest_path}, Old: {old_path}")
        self.settings.save_options(source_path, dest_path, old_path)
        messagebox.showinfo("Saved", "Settings have been saved")