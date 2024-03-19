#!/usr/bin/env python3
import sys 
import os
sys.path.append(os.path.expanduser("~/.local/lib/python3.11/music_to_pen/"))
sys.path.append(os.path.join(os.path.dirname(__file__), 'music_to_pen/'))
from gui import Gui
from updater import Updater 

if __name__ == "__main__":
        update = Updater()
        update.check_updates()
        gui = Gui(450, 450)