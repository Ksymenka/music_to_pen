import configparser
import os

class Settings:
    config = configparser.ConfigParser()

    def read_options(self):
        Settings.config.read("./settings.ini")
        return Settings.config['saved_path']

    def is_configs_exists(self):
        return os.path.exists("./settings.ini")
    
    def save_options(self, source_path : str, dest_path : str, old_path : str):
        if os.path.exists("./settings.ini"):
            return
        else: 
            Settings.config['saved_path'] = {
                'Source_path' : source_path,
                'dest_path' : dest_path,
                'old_path' : old_path
            }
            with open('./settings.ini', "w") as configfile:
                Settings.config.write(configfile)

    def remove_options(self):
        if os.path.exists('./settings.ini'):
            os.remove('./settings.ini')