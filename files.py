import os
import subprocess
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
            if self.check_dest_is_dir(path) is not None:
                return path
            
    def check_dest_is_dir(self, path):
        if os.path.exists(path):
            contents = os.listdir(path)
            for file in contents:
                file_path = os.path.join(path, file)
                if os.path.isdir(file_path):
                    print(file_path, " is a directory")
                    return os.path.abspath(file_path) 
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
        if file_path.endswith(".mp3"):
            print("File", file_path, " is getting moved to ", self.desination_path)
            shutil.move(file_path, self.desination_path)
        elif file_path.endswith(".mp4"):
            print("File", file_path, " is getting moved to ", self.old_path)
            shutil.move(file_path, self.old_path)            
        else:
            print("File", file_path, " is not a music containing file, excluding...")

    def process_files(self): # used to change file format to mp3 from mp4 and then upload it to approprieate 
        files = os.listdir(self.source_path)
        for file in files:
            print("Processing file", file, " atm")
            file_path = os.path.join(self.source_path, file)
            self.convert_file(file_path)
        files = os.listdir(self.source_path)
        for file in files:
            print("Moving file ", file, " atm")
            file_path = os.path.join(self.source_path, file)
            self.move_files(file_path)