#!/usr/bin/env python3
from modules.gui import Gui
from modules.updater import Updater 

if __name__ == "__main__":
        update = Updater()
        update.check_updates()
        gui = Gui(450, 450)
