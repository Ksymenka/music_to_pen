import sys
import os
from git import Repo
import git 
import requests
from modules.settings import Settings
from tkinter import messagebox

class Updater:
    def __init__(self) -> None:
        self.project_path = self.get_project_path()
        print(f"Project path: {self.project_path}")
        self.repo = Repo(self.project_path)
        self.origin = self.repo.remotes.origin

        
    def get_project_path(self) -> None:
        settings = Settings()
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
        settings = Settings()
        try:
            self.origin.fetch()
            self.origin.pull()
            
            print("Updated succesfully")
        except git.GitCommandError as e:
            print(f"There was an error while updating: {e}")
        messagebox.showinfo("Updated", "Updated succesfully")
        
