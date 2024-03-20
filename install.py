#!/usr/bin/env python3

# use this file to install/uninstall application

import sys
import os

class InstallProject:
    

    cwd = os.getcwd() 
    desktop_path = os.path.expanduser("~/.local/share/applications/music_to_pen.desktop")

    def __init__(self):
        print(f"Cwd: {self.cwd}")
        app_path = os.path.expanduser("~/.local/share/applications/")
        if not os.path.exists(app_path):
            print(f"Path {app_path} did not exists, creating...")
            os.makedirs(app_path)

    def reinstall(self) -> None:
        self.uninstall()
        self.install()

    def install(self) -> None:
        self.create_desktop()
        src = os.path.join(self.cwd, "music_to_pen.desktop")
        os.rename(src, self.desktop_path)
        print(f"Moved file to {self.desktop_path}")
    
    def uninstall(self) -> None:
        os.remove(self.desktop_path)
        print(f"Removed desktop file at {self.desktop_path}")

    def create_desktop(self) -> None:
        path = os.path.join(self.cwd, "music_to_pen.desktop")
        content = f'''#!/usr/bin/env xdg-open
[Desktop Entry]
Name=Music to pendrive
Exec={os.path.join(self.cwd, "main.py")}
Icon={os.path.join(self.cwd, 'icons/pendrive.ico')}
Terminal=false
Type=Application
        '''
        with open(path, 'w') as desktop_file:
            desktop_file.write(content)
        os.chmod(path, 0o755)
        print(f"Created desktop file at {path}")
        print(f"File content: {path}")
        


def main() -> None:
    arg = sys.argv

    if InstallProject.cwd != os.path.dirname(os.path.abspath(__file__)):
        print (InstallProject.cwd, "\n", os.path.dirname(os.path.abspath(__file__)))
        print("Please run this file from the same directory as it is, exiting...")
        sys.exit()
        return

    if len(arg) < 2:
        print("No argument provided.\nPlease select action (install/uninstall/reinstall)")
        sys.exit(1)

    install = InstallProject()

    match arg[1]:
        case "install":
            install.install()
        case "uninstall":
            install.uninstall()
        case "reinstall":
            install.reinstall()
        case _:
            print("Invalid argument.\nPlease select action (install/uninstall/reinstall)")
        
    

if __name__ == "__main__":
    main()
