# use this file to install/uninstall application

import importlib.util
import sys
import shutil
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
            if os.path.isfile(module):
                module_path_origin = os.path.join(self.project_paths['module_dir'], module)
                module_path_destination = os.path.join(self.system_paths['dep_path'], module)
                shutil.copy(module_path_origin, module_path_destination)
                print(f"Moved file {module}")

    def copy_main(self) -> None:
        main_file_path = os.path.join(self.cwd, "main.py")
        main_file_dest = os.path.join(self.system_paths['bin_path'], self.project_paths['name'], "main.py")
        shutil.copy(main_file_path, main_file_dest)
        print(f"Moved file to {main_file_dest}")

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
            print("An error occurred while uninstalling: {e}")
        
    def remove_modules(self) -> None:
        shutil.rmtree(os.path.join(self.system_paths['dep_path']), self.project_paths['name'])
    
    def remove_icon(self) -> None:
        os.remove(os.path.join(self.system_paths['app_path'], 'pendrive.ico'))

    def remove_main(self) -> None:
        os.remove(os.path.join(self.system_paths['bin_path'], self.project_paths['name'], "main.py"))

    def remove_desktop(self) -> None:
        os.remove(os.path.join(self.system_paths['app_path'], 'music_to_pen.desktop'))

def main() -> None:
    if os.getuid() != 0:
        print("Run this scipt only as root")
        sys.exit(1)

    os.chdir(os.path.realpath(__file__))

    install = Install()
    arg = sys.argv
    match arg[1]:
        case "install":
            install.install()
        case "uninstall":
            install.uninstall()
        case _:
            print("Invalid argument.\nPlease select action (install/uninstall)")

if __name__ == "__main__":
    main()
