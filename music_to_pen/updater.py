import os
from git import Repo
import requests

class Updater:
    def __init__(self) -> None:
        self.project_path = self.get_project_path()
        self.repo = Repo(self.project_path)

        
    def get_project_path(self) -> None:
        file_path = os.path.realpath(__file__)
        
        if 'music_to_pen' in file_path:
            last_index = file_path.find('music_to_pen') + len('music_to_pen')
            return file_path[:last_index]
        
    def get_remote_commit(self) -> None:
        response = requests.get("https://api.github.com/repos/ksymenka/music_to_pen/commits")
        if response.status_code == 200:
            return response.json()[0]['sha']

    def get_local_commit(self):
        return self.repo.head.commit.hexsha
    
    def check_updates(self):
        if self.get_local_commit() and self.get_remote_commit():
            if self.get_remote_commit() == self.get_local_commit:
                print("Project is up to date")
            else:
                print("There is update avaible")
        else:
            print("There was an error while getting commits") 
    
     

update = Updater()
update.check_updates()
