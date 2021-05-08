import calendar
import datetime
import os
from pathlib import Path
import shutil
from Config.Config import getConfigValue, getExtensions


class FileSorter:
    #TODO PETA CON MISMOS ARCHIVOS
    def browseFiles(path, organizedFolderPath, subfolders):
        directory = Path(path)
        for item in directory.iterdir():
            if item.is_dir():
                FileSorter.browseFiles(item, organizedFolderPath, subfolders)
            else:
                FileSorter.organizeFileByExtension(item, organizedFolderPath, subfolders)

    def organizeFileByExtension(item, organizedFolderPath, subfolders):
        images = getExtensions("extensions", "extensionsfolder1")
        documents = getExtensions("extensions", "extensionsfolder2")
        videos = getExtensions("extensions", "extensionsfolder3")

        extension = str(os.path.splitext(item)[1]).lower()
        chkorganizeByYear = getConfigValue("Folder1", "orderbyyear")
        chkorganizeByMonth = getConfigValue("Folder1", "orderbymonth")

        if extension in images:
            if chkorganizeByYear == "True" and chkorganizeByMonth == "True":
                FileSorter.organizeByYearAndMonth(organizedFolderPath, item, subfolders[0])
            elif chkorganizeByYear == "True" and chkorganizeByMonth == "False":
                FileSorter.organizeByYear(organizedFolderPath, item, subfolders[0])
            elif chkorganizeByYear == "False" and chkorganizeByMonth == "True":
                FileSorter.organizeByMonth(organizedFolderPath, item, subfolders[0])
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

        try:
            Path(item).rename(copyFilePath)
        except OSError:
            #TODO HACER QUE OPCION PARA REEMPLAZAR Y AVISAR
            # Remplazar si existe
            shutil.move(item, copyFilePath)
            print("remplazado")

    def organizeByYear(organizedFolderPath, item, imgSubFolder):
        year = datetime.date.fromtimestamp(os.path.getmtime(item)).year
        yearFolder = organizedFolderPath + "/" + imgSubFolder + "/" + str(year)

        copyFilePath = yearFolder + "/" + item.name

        os.makedirs(yearFolder, exist_ok=True)
        Path(item).rename(copyFilePath)

    def organizeByMonth(organizedFolderPath, item, imgSubFolder):
        creationMonthName = calendar.month_name[datetime.date.fromtimestamp(os.path.getmtime(item)).month].capitalize()
        monthFolder = organizedFolderPath + "/" + imgSubFolder + "/" + creationMonthName

        copyFilePath = monthFolder + "/" + item.name

        os.makedirs(monthFolder, exist_ok=True)
        Path(item).rename(copyFilePath)
