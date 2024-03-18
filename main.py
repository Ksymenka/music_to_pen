#!/usr/bin/env python3
import sys 
import os
sys.path.append(os.path.expanduser("~/.local/lib/python3.11/"))
sys.path.append(os.path.join(os.getcwd(), "music_to_pen"))
from music_to_pen.gui import Gui
from music_to_pen.updater import Updater 

if __name__ == "__main__":
        update = Updater()
        update.check_updates()
        gui = Gui(450, 450)