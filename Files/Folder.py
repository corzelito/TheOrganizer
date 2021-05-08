import os
from pathlib import Path


class Folder:
    def makefolders(path, subfolders):
        os.makedirs(path, exist_ok=True)
        for i in subfolders:
            os.makedirs(path + "/" + i, exist_ok=True)

    def deleteAllFolders(path):
        if os.path.exists(path):
            directory = Path(path)
            for item in directory.iterdir():
                if item.is_dir():
                    Folder.deleteAllFolders(item)
                else:
                    item.unlink()
            directory.rmdir()

    def getNumberOfFiles(root):
        count = 0
        for path in os.listdir(root):
            if os.path.isfile(os.path.join(root, path)):
                count += 1
        return count