#!/usr/bin/env python3

# use this file to install/uninstall application

import importlib.util
import sys
import shutil
import pwd
import os
import pathlib
from settings import Settings

class InstallProject:


    # some variables

    installed = False
    cwd = os.getcwd() 
    home = os.path.expanduser("~")
    settings = Settings()

    # project paths

    project_paths = {
        'module_dir' : cwd,
        'icon' : os.path.join(cwd, "../icons/pendrive.ico"),
        'desktop' : os.path.join(cwd, "../music_to_pen.desktop"),
        'name' : 'music_to_pen',
        'icon_path' : os.path.join(cwd, '../icons/pendrive.ico') 
    }

    # system paths

    system_paths = {
        'dep_path' : os.path.join(home, '.local/lib/python3.11/music_to_pen'),
        'bin_path' : os.path.join(home, '.local/bin/music_to_pen'),
        'app_path' : os.path.join(home, '.local/share/applications'),
    }

    # constructor

    def __init__(self) -> None:
        if importlib.util.find_spec("tkinter") is None:
            print("Tkinter may not be installed. App may not function properly") 

        for key, path in self.system_paths.items():
            if not os.path.exists(path):
                print(f"Path {path} didn't exists, creating...")
                os.makedirs(path)
        self.create_desktop()


    # install methods
    
    def install(self) -> None:
        try:
            self.copy_modules()
            self.copy_main()
            self.copy_icon()
            self.copy_desktop()
            print("Install successful")
            self.installed = True
        except Exception as e:
            print(f"There was an error while installing: {e}")


    def copy_modules(self) -> None:
        for module in os.listdir(self.project_paths['module_dir']):
            module_path_origin = os.path.join(self.project_paths['module_dir'], module)
            if os.path.isfile(module_path_origin):
                shutil.copy(module_path_origin, self.system_paths['dep_path'])
                print(f"Moved file from {module_path_origin} to {self.system_paths['dep_path']}")

    def copy_main(self) -> None:
        main_file_path = os.path.join(self.cwd, "../main.py")
        shutil.copy(main_file_path, self.system_paths['bin_path'])
        print(f"Moved file to {self.system_paths['bin_path']}")

    def copy_desktop(self) -> None:
        dest = os.path.join(self.system_paths['app_path'], 'music_to_pen.desktop')
        shutil.copy(self.project_paths['desktop'], dest)
        os.chmod(dest, 0o755)
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
            self.installed = False
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

    # other
    
    def check_if_installed(self) -> None:
        file_ammount = 0
        for file in os.walk(self.system_paths['bin_path']):
            file_ammount += 1
        if file_ammount == 0:
            return False
        else:
            return True
        
    def create_desktop(self) -> None:
        file = self.project_paths['desktop']
        content = f'''#!/usr/bin/env xdg-open
[Desktop Entry]
Name=Music to pendrive
Exec={os.path.join(self.system_paths['bin_path'], 'main.py')}
Icon={os.path.join(self.system_paths['app_path'], 'pendrive.ico')}
Terminal=false
Type=Application
        '''
        with open(file, 'w') as desktop_file:
            desktop_file.write(content)
        os.chmod(file, 0o755)
        


def main() -> None:

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