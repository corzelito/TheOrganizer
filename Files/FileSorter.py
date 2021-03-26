import calendar
import datetime
import os
from pathlib import Path


class FileSorter:
    def browseFiles(path, organizedFolderPath, subfolders, checkConfig):
        directory = Path(path)
        for item in directory.iterdir():
            if item.is_dir():
                FileSorter.browseFiles(item, organizedFolderPath, subfolders, checkConfig)
            else:
                FileSorter.organizeFileByExtension(item, organizedFolderPath, subfolders, checkConfig)

    def organizeFileByExtension(item, organizedFolderPath, subfolders, checkConfig):
        images = [".png", ".jpg", ".jpeg"]
        documents = [".doc", ".pdf", ".docx"]
        videos = [".mp4", ".mov"]

        extension = str(os.path.splitext(item)[1]).lower()
        chkorganizeByYear = checkConfig[0]
        chkorganizeByMonth = checkConfig[1]

        if extension in images:
            if chkorganizeByMonth and chkorganizeByYear:
                FileSorter.organizeByYearAndMonth(organizedFolderPath, item, subfolders[0])
            else:
                Path(item).rename(organizedFolderPath + "/" + subfolders[0] + "/" + item.name)

        elif extension in videos:
            Path(item).rename(organizedFolderPath + "/" + subfolders[1] + "/" + item.name)
        elif extension in documents:
            Path(item).rename(organizedFolderPath + "/" + subfolders[2] + "/" + item.name)
        else:
            Path(item).rename(organizedFolderPath + "/" + subfolders[3] + "/" + item.name)

    def organizeByYearAndMonth(organizedFolderPath, item, imgSubFolder):
        year = datetime.date.fromtimestamp(os.path.getmtime(item)).year
        yearFolder = organizedFolderPath + "/" + imgSubFolder + "/" + str(year)

        creationMonthName = calendar.month_name[datetime.date.fromtimestamp(os.path.getmtime(item)).month].capitalize()
        monthFolder = yearFolder + "/" + creationMonthName

        copyFilePath = monthFolder + "/" + item.name

        os.makedirs(yearFolder, exist_ok=True)
        os.makedirs(monthFolder, exist_ok=True)
        Path(item).rename(copyFilePath)
