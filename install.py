# use this file to install/uninstall application

import importlib.util
import sys
import os
class Install:


    # project paths

    cwd = os.getcwd() 

    project_paths = {
        'module_dir' : os.path.join(cwd, "modules"),
        'icon' : os.path.join(cwd, "icons/pendrive.ico"),
        'desktop' : os.path.join(cwd, "music_to_pen.desktop"),
        'name' : 'music_to_pen',
        'icon_path' : os.path.join(cwd, 'icons/pendrive.ico') # icons from https://www.iconarchive.com/show/windows-8-metro-icons-by-dakirby309/Drives-USB-alt-1-Metro-icon.html
    }

    # system paths

    system_paths = {
        'dep_path' : '/usr/lib/python3.11/',
        'bin_path' : '/usr/bin/',
        'app_path' : os.path.join(os.path.expanduser("~"), '.local/share/applications/') 
    }

    # constructor

    def __init__(self) -> None:
        if importlib.util.find_spec("tkinter") is None:
            print("Tkinter may not be installed. App may not function properly") 

        dep_dir = os.path.join(self.system_paths['dep_path'], self.project_paths['name'])
        bin_dir = os.path.join(self.system_paths['bin_path'], self.project_paths['name'])

        if not os.path.exists(dep_dir):
            os.makedirs(dep_dir)
        if not os.path.exists(bin_dir):
            os.makedirs(bin_dir)

    # install methods
    
    def install(self):
        self.move_modules()
        self.move_main()
        self.move_icon()
        self.move_desktop()

    def move_modules(self):
        for module in os.listdir(self.project_paths['module_dir']):
            if os.path.isfile(module):
                module_path_origin = os.path.join(self.project_paths['module_dir'], module)
                module_path_destination = os.path.join(self.system_paths['dep_path'], module)
                os.replace(module_path_origin, module_path_destination)
                print(f"Moved file {module}")

    def move_main(self):
        main_file_path = os.path.join(self.cwd, "main.py")
        main_file_dest = os.path.join(self.system_paths['bin_path'], self.project_paths['name'], "main.py")
        os.replace(main_file_path, main_file_dest)
        print(f"Moved file to {main_file_dest}")

    def move_desktop(self):
        dest = os.path.join(self.system_paths['app_path'], 'music_to_pen.desktop')
        os.replace(self.project_paths['desktop'], dest)
        print(f"Moved file to {dest}")

    def move_icon(self):
        dest = os.path.join(self.system_paths['app_path'], "pendrive.ico")
        os.replace(self.project_paths['icon_path'], dest)
        print(f"Moved file to {dest}")
    
    # remove methods
        