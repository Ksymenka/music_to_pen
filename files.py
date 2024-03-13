import os
import subprocess
import random
import shutil

class FileOperation:
    # constuctor methods
    def __init__(self, source_path : str = os.path.expanduser('~/Pobrane'), desination_path : str = None, old_path : str = os.path.expanduser("~/Movies")):
        # paths
        self.source_path = source_path
        self.desination_path = desination_path or self.check_sus_dest()
        self.old_path = old_path
        if not os.path.exists(old_path): 
            os.makedirs(old_path)
            
    def check_sus_dest(self):
        sus_paths = ["/media/", "/mnt"]
        for path in sus_paths:
            found_mount_point = self.check_dest_is_dir_recursively(path)
            if found_mount_point is not None:
                return found_mount_point

    def check_dest_is_dir_recursively(self, path):
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for dir_name in dirs:
                    dir_path = os.path.join(root, dir_name)
                    if os.path.ismount(dir_path):
                        print(dir_path, " is a directory a mounted directory")
                        return os.path.abspath(dir_path)
            print("Didn't found any mount point. Is usb stick connected?")
        return None
            
    # file operation methods

    def create_new_name(self, file : str): # used in convert_file
        path = os.path.abspath(file)
        name = os.path.splitext(file)
        new_name = name[0] + '.mp3'
        return new_name
    

    def convert_file(self, file_path : str): # used in process_files
        new_file_path = os.path.join(os.path.dirname(file_path), self.create_new_name(file_path))
        subprocess.run(['ffmpeg', '-i', file_path, '-vn', new_file_path, '-loglevel', 'quiet'])
            
    def move_files(self, file_path : str): # used to move files to accurate directories
        try:
            if file_path.endswith(".mp3"):
                print("File", file_path, " is getting moved to ", self.desination_path)
                shutil.move(file_path, self.desination_path)
            elif file_path.endswith(".mp4"):
                print("File", file_path, " is getting moved to ", self.old_path)
                shutil.move(file_path, self.old_path)            
            else:
                print("File", file_path, " is not a music containing file, excluding...")
        except shutil.Error:
            print("File already exists, overwritting...")
            file_name = os.path.basename(file_path)
            destination_file_path = os.path.join(self.desination_path, file_name)
            os.remove(destination_file_path)
            self.move_files(file_path)
            

    def process_files_with_progress(self, progress_bar, status_label): # used to change file format to mp3 from mp4 and then upload it to approprieate 
        print("Searching for files in source directory...")
        files = os.listdir(self.source_path)
        total_files = len(files)
        progress_bar["maximum"] = total_files

        status_label["text"] = "Preparing..."

        for index, file in enumerate(files, start=1):
            print("Processing file", file, " atm")
            status_label["text"] = f"Processing file {file}"
            file_path = os.path.join(self.source_path, file)
            self.convert_file(file_path)

            progress_bar["value"] = index
            progress_bar.update_idletasks()

        print("Converting files done")
        status_label["text"] = "Converting files done"
        progress_bar["value"] = 0 

        files = os.listdir(self.source_path)
        for index, file in enumerate(files, start=1):
            print("Moving file ", file, " atm")
            status_label["text"] = f"Moving file {file}"
            file_path = os.path.join(self.source_path, file)
            self.move_files(file_path)

            progress_bar["value"] = index
            progress_bar.update_idletasks()

        print("Moving files done.")
        progress_bar["value"] = 0
        status_label["text"] = "Done"
        