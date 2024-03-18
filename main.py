#!/usr/bin/env python3
import sys 
import os
sys.path.append(os.path.expanduser("~/.local/lib/python3.11/"))
from music_to_pen.gui import Gui

if __name__ == "__main__":
        gui = Gui(450, 450)