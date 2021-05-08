import calendar
import datetime
import os
from pathlib import Path
import shutil
from Config.Config import getConfigValue, getExtensions


class FileSorter:

    def browseFiles(path, organizedFolderPath, subfolders, question):
        directory = Path(path)
        for item in directory.iterdir():
            if item.is_dir():
                FileSorter.browseFiles(item, organizedFolderPath, subfolders, question)
            else:
                FileSorter.organizeFileByExtension(item, organizedFolderPath, subfolders, question)

    def organizeFileByExtension(item, organizedFolderPath, subfolders, question):
        images = getExtensions("extensions", "extensionsfolder1")
        documents = getExtensions("extensions", "extensionsfolder2")
        videos = getExtensions("extensions", "extensionsfolder3")

        extension = str(os.path.splitext(item)[1]).lower()
        chkorganizeByYear = getConfigValue("Folder1", "orderbyyear")
        chkorganizeByMonth = getConfigValue("Folder1", "orderbymonth")

        if extension in images:
            if chkorganizeByYear == "True" and chkorganizeByMonth == "True":
                FileSorter.organizeByYearAndMonth(organizedFolderPath, item, subfolders[0], question)
            elif chkorganizeByYear == "True" and chkorganizeByMonth == "False":
                FileSorter.organizeByYear(organizedFolderPath, item, subfolders[0], question)
            elif chkorganizeByYear == "False" and chkorganizeByMonth == "True":
                FileSorter.organizeByMonth(organizedFolderPath, item, subfolders[0], question)
            else:
                Path(item).rename(organizedFolderPath + "/" + subfolders[0] + "/" + item.name)

        elif extension in videos:
            Path(item).rename(organizedFolderPath + "/" + subfolders[1] + "/" + item.name)
        elif extension in documents:
                Path(item).rename(organizedFolderPath + "/" + subfolders[2] + "/" + item.name)
        else:
            Path(item).rename(organizedFolderPath + "/" + subfolders[3] + "/" + item.name)

    def organizeByYearAndMonth(organizedFolderPath, item, imgSubFolder, question):
        year = datetime.date.fromtimestamp(os.path.getmtime(item)).year
        yearFolder = organizedFolderPath + "/" + imgSubFolder + "/" + str(year)

        creationMonthName = calendar.month_name[datetime.date.fromtimestamp(os.path.getmtime(item)).month].capitalize()
        monthFolder = yearFolder + "/" + creationMonthName

        copyFilePath = monthFolder + "/" + item.name
        os.makedirs(yearFolder, exist_ok=True)
        os.makedirs(monthFolder, exist_ok=True)

        try:
            Path(item).rename(copyFilePath)
        except OSError:
            if question == 6:
                shutil.move(item, copyFilePath)
            else:
                print("no remplazado")

    def organizeByYear(organizedFolderPath, item, imgSubFolder, question):
        year = datetime.date.fromtimestamp(os.path.getmtime(item)).year
        yearFolder = organizedFolderPath + "/" + imgSubFolder + "/" + str(year)

        copyFilePath = yearFolder + "/" + item.name

        os.makedirs(yearFolder, exist_ok=True)
        Path(item).rename(copyFilePath)

    def organizeByMonth(organizedFolderPath, item, imgSubFolder, question):
        creationMonthName = calendar.month_name[datetime.date.fromtimestamp(os.path.getmtime(item)).month].capitalize()
        monthFolder = organizedFolderPath + "/" + imgSubFolder + "/" + creationMonthName

        copyFilePath = monthFolder + "/" + item.name

        os.makedirs(monthFolder, exist_ok=True)
        Path(item).rename(copyFilePath)
