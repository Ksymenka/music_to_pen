#!/usr/bin/env python3

# use this file to install/uninstall application

import importlib.util
import sys
import shutil
import pwd
import os

class InstallProject:


    # project paths

    cwd = os.getcwd() 



    project_paths = {
        'module_dir' : os.path.join(cwd, "music_to_pen"),
        'icon' : os.path.join(cwd, "icons/pendrive.ico"),
        'desktop' : os.path.join(cwd, "music_to_pen.desktop"),
        'name' : 'music_to_pen',
        'icon_path' : os.path.join(cwd, 'icons/pendrive.ico') 
    }

    # system paths

    system_paths = {
        'dep_path' : '/usr/lib/python3.11/music_to_pen',
        'bin_path' : '/usr/bin/music_to_pen',
        'app_path' : '/usr/share/applications' 
    }

    # constructor

    def __init__(self) -> None:
        if importlib.util.find_spec("tkinter") is None:
            print("Tkinter may not be installed. App may not function properly") 


        dep_dir = self.system_paths['dep_path']
        bin_dir = self.system_paths['bin_path']

        if not os.path.exists(dep_dir):
            os.makedirs(dep_dir)
        if not os.path.exists(bin_dir):
            os.makedirs(bin_dir)

    # install methods
    
    def install(self) -> None:
        try:
            self.copy_modules()
            self.copy_main()
            self.copy_icon()
            self.copy_desktop()
            print("Install successful")
        except Exception as e:
            print(f"There was an error while installing: {e}")


    def copy_modules(self) -> None:
        for module in os.listdir(self.project_paths['module_dir']):
            module_path_origin = os.path.join(self.project_paths['module_dir'], module)
            if os.path.isfile(module_path_origin):
                shutil.copy(module_path_origin, self.system_paths['dep_path'])
                print(f"Moved file from {module_path_origin} to {self.system_paths['dep_path']}")

    def copy_main(self) -> None:
        main_file_path = os.path.join(self.cwd, "main.py")
        shutil.copy(main_file_path, self.system_paths['bin_path'])
        print(f"Moved file to {self.system_paths['bin_path']}")

    def copy_desktop(self) -> None:
        dest = os.path.join(self.system_paths['app_path'], 'music_to_pen.desktop')
        shutil.copy(self.project_paths['desktop'], dest)
        print(f"Moved file to {dest}")

    def copy_icon(self) -> None:
        dest = os.path.join(self.system_paths['app_path'], "pendrive.ico")
        shutil.copy(self.project_paths['icon_path'], dest)
        print(f"Moved file to {dest}")
    
    # remove methods
    def uninstall(self) -> None:
        try:
            self.remove_modules()
            self.remove_icon()
            self.remove_main()
            self.remove_desktop()
            print("Uninstall successful")
        except Exception as e:
            print(f"An error occurred while uninstalling: {e}")
        
    def remove_modules(self) -> None:
        shutil.rmtree(self.system_paths['dep_path'])
        print(f"Removed project modules at {self.system_paths['dep_path']}")
    
    def remove_icon(self) -> None:
        dest = os.path.join(self.system_paths['app_path'], 'pendrive.ico')
        os.remove(dest)
        print(f"Removed icon file at {dest}")

    def remove_main(self) -> None:
        dest = os.path.join(self.system_paths['bin_path'], "main.py")
        os.remove(dest)
        print(f"Removed main binary file at {dest}")

    def remove_desktop(self) -> None:
        dest = os.path.join(self.system_paths['app_path'], 'music_to_pen.desktop')
        os.remove(dest)
        print(f"Removed desktop icon at {dest}")

def main() -> None:
    if os.getuid() != 0:
        print("Run this scipt only as root")
        sys.exit(1)

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    arg = sys.argv

    if len(arg) < 2:
        print("No argument provided.\nPlease select action (install/uninstall)")
        sys.exit(1)

    install = InstallProject()
    match arg[1]:
        case "install":
            install.install()
        case "uninstall":
            install.uninstall()
        case _:
            print("Invalid argument.\nPlease select action (install/uninstall)")

if __name__ == "__main__":
    main()
