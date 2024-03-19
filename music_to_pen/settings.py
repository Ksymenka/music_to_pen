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
        Settings.config.read(Settings.config_full_path)
        if Settings.config.has_section('saved_path'):
            Settings.config.remove_section('saved_path')
            with open(Settings.config_full_path, 'w') as configfile:
                Settings.config.write(configfile)
            print("Config file has been deleted")
            messagebox.showinfo("Removed", "Settings have been removed")
            
    def save_one_option(self, section : str, key : str, value : str): 
        old = self.read_options()

        try:
            if not Settings.config.has_section(section):
                Settings.config.add_section(section)
            Settings.config.set(section, key, value)
            with open(Settings.config_full_path, 'w') as configfile:
                Settings.config.write(configfile)
                Settings.config.write(old)
        except Exception as e:
            print(f"There was an error while saving: {e}")
            
    def read_one_option(self, section : str, key : str):
        if Settings.config.has_section(section) and Settings.config.has_option(section, key):
            Settings.config.read(Settings.config_full_path)
            return Settings.config.get(section, key)
        
    def remove_one_option(self, section : str, key : str):
        try:
            if Settings.config.has_section(section):
                if Settings.config.has_option(section, key):
                    Settings.config.remove_option(section, key)
                    with open(Settings.config_full_path, 'r') as configfile:
                        lines = configfile.readlines()

                    with open(Settings.config_full_path, 'w') as configfile:
                        for line in lines:
                            if f"{key} =" not in line:
                                configfile.write(line)
                    print(f"Option '{key}' from section '{section}' has been removed.")
                else:
                    print(f"Key '{key}' not found in section '{section}'.")
            else:
                print(f"Section '{section}' not found in the configuration.")
        except Exception as e:
            print(f"There was an error while removing the option: {e}")





            

       
