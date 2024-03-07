import configparser
import os

class Settings:
    config = configparser.ConfigParser()
    config_path = os.path.expanduser("~/.config/music_to_pen/")
    config_file_name = "settings.ini"
    config_full_path = os.path.join(config_path, config_file_name)

    def __init__(self):
        if not os.path.exists(Settings.config_path):
            os.makedirs(Settings.config_path)

    def read_options(self):
        Settings.config.read(Settings.config_full_path)
        return Settings.config['saved_path']

    def is_configs_exists(self):
        return os.path.exists(Settings.config_full_path)
    
    def save_options(self, source_path : str, dest_path : str, old_path : str):
        Settings.config['saved_path'] = {
            'Source_path' : source_path,
            'dest_path' : dest_path,
            'old_path' : old_path
        }
        with open(Settings.config_full_path, "w") as configfile:
            Settings.config.write(configfile)

    def remove_options(self):
        if os.path.exists(Settings.config_full_path):
            os.remove(Settings.config_full_path)