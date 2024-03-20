Simple python program that lets you transfer and convert your music files from pc to usb stick with use of ffmpeg. Only for linux.

# Usage

You can just run it with `python3 ./main.py`. There is also a `music_to_pen/install.py` script that will create `music_to_pen.desktop` file and put in in `$HOME/.local/share/applications/`. 

## Python virt env

For this script to work you need to setup python virtual env with `python3 -m venv {path/to/repo}` and `chmod a+x {path/to/repo/bin/activate}`

## Updating

Every time you run main.py it checks for newer commits. If it found any it will ask you for updating. That will pull newest commit to the current branch. In other words if you click *update now* the app will be updated. 
