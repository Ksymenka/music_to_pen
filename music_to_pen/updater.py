import os

class Updater:
    # def __init__(self, project_dir : str):
    #     pass
        
    def get_project_path(self) -> None:
        file_path = os.path.realpath(__file__)
        
        if 'music_to_pen' in file_path:
            last_index = file_path.find('music_to_pen') + len('music_to_pen')
            return file_path[:last_index]
        

update = Updater()
print(update.get_project_path())
