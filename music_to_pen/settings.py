import configparser
import os
from tkinter import messagebox

class Settings:
    config = configparser.ConfigParser()
    config_path = os.path.expanduser("~/.config/music_to_pen/")
    config_file_name = "settings.ini"
    config_full_path = os.path.join(config_path, config_file_name)

    def __init__(self):
        if not os.path.exists(Settings.config_path):
            os.makedirs(Settings.config_path)
        if not os.path.exists(Settings.config_full_path):
            open(Settings.config_full_path, 'x')
        Settings.config['saved_path'] = {}

    def read_options(self):
        Settings.config.read(Settings.config_full_path)
        return Settings.config['saved_path']

    def is_configs_exists(self):
        return os.path.exists(Settings.config_full_path)
    
    def save_options(self, source_path=None, dest_path=None, old_path=None):
        if source_path is not None:
            Settings.config['saved_path']['Source_path'] = source_path
        

        if  dest_path is not None:
            Settings.config['saved_path']['dest_path'] = dest_path 
        
        if old_path is not None:
            Settings.config['saved_path']['old_path'] = old_path 

        with open(Settings.config_full_path, "a") as configfile:
            Settings.config.write(configfile)
            print("Options has been saved to a file at ", Settings.config_full_path)
            
    def remove_options(self):
        self.config.read(Settings.config_full_path)
        if self.config.has_section('saved_path'):
            self.config.remove_section('saved_path')
            with open(Settings.config_full_path, 'w') as configfile:
                self.config.write(configfile)
            print("Config file has been deleted")
            messagebox.showinfo("Removed", "Settings have been removed")
            
    def save_one_option(self, section : str, key : str, value : str): 
        try:
            if not Settings.config.has_section(section):
                Settings.config.add_section(section)
            Settings.config.set(section, key, value)
            with open(Settings.config_full_path, 'a') as configfile:
                Settings.config.write(configfile)
        except Exception as e:
            print(f"There was an error while saving: {e}")

            

       
