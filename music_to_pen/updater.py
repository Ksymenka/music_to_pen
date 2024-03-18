import os
from git import Repo
import requests
from install import InstallProject
import subprocess
from tkinter import messagebox

class Updater:
    def __init__(self) -> None:
        self.project_path = self.get_project_path()
        self.repo = Repo(self.project_path)
        self.origin = self.repo.remotes.origin 

        
    def get_project_path(self) -> None:
        file_path = os.path.realpath(__file__)
        
        if 'music_to_pen' in file_path:
            last_index = file_path.find('music_to_pen') + len('music_to_pen')
            return file_path[:last_index]
        
    def get_remote_commit(self) -> None:
        response = requests.get("https://api.github.com/repos/ksymenka/music_to_pen/commits")
        if response.status_code == 200:
            return response.json()[0]['sha']

    def get_local_commit(self) -> None:
        return self.repo.head.commit.hexsha
    
    def check_updates(self) -> None:
        remote_commit = self.get_remote_commit() 
        local_commit = self.get_local_commit()

        if remote_commit and local_commit:
            if remote_commit == local_commit:
                print("Project is up to date")
            else:
                print("There is update avaible")
                self.ask_for_update()
        else:
            print("There was an error while getting commits") 
            
    def ask_for_update(self) -> None:
        answer = messagebox.askyesno(title="Update avaible", message="Do you want to update now?")
        if answer:
            self.update()
            
    def update(self):
        install = InstallProject()
        if install.check_if_installed():
            install.uninstall()
        try:
            self.origin.fetch()
            self.origin.pull()
            if install.check_if_installed():
                install.install()
            
            print("Updated succesfully")
        except git.GitCommandError as e:
            print(f"There was an erroe while updating: {e}")
        
update = Updater()
update.check_updates()
