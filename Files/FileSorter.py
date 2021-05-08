import calendar
import datetime
import os
from pathlib import Path
import shutil
from Config.Config import getConfigValue, getExtensions, getSubfolders, getNumberOfConfigsSection


class FileSorter:

    def browseFiles(path, organizedFolderPath, question):
        directory = Path(path)
        for item in directory.iterdir():
            if item.is_dir():
                FileSorter.browseFiles(item, organizedFolderPath, question)
            else:
                FileSorter.organizeFileByExtension(item, organizedFolderPath, question)

    def organizeFileByExtension(item, organizedFolderPath, question):
        subfolders = getSubfolders()
        extension = str(os.path.splitext(item)[1]).lower()

        NumberOfConfigsSection = (getNumberOfConfigsSection("extensions"))
        extensionsFolders = []
        chkOrganizeByYear = []
        chkOrganizeByMonth = []

        for i in range(1, NumberOfConfigsSection + 1):
            extensionFolder = "extensionsfolder" + str(i)
            folder = "Folder" + str(i)
            extensionsFolders.append(extensionFolder)
            chkOrganizeByYear.append(folder)
            chkOrganizeByMonth.append(folder)

        for i in range(0, NumberOfConfigsSection):
            organizeByYear = getConfigValue(chkOrganizeByYear[i], "orderbyyear")
            organizeByMonth = getConfigValue(chkOrganizeByYear[i], "orderbymonth")

            if extension in getExtensions("extensions", str(extensionsFolders[i])):

                if organizeByYear == "True" and organizeByMonth == "True":
                    FileSorter.organizeByYearAndMonth(organizedFolderPath, item, subfolders[i], question)
                elif organizeByYear == "True" and organizeByMonth == "False":
                    FileSorter.organizeByYear(organizedFolderPath, item, subfolders[i], question)
                elif organizeByYear == "False" and organizeByMonth == "True":
                    FileSorter.organizeByMonth(organizedFolderPath, item, subfolders[i], question)
                else:
                    Path(item).rename(organizedFolderPath + "/" + subfolders[i] + "/" + item.name)

        try:
            Path(item).rename(organizedFolderPath + "/" + "Otros" + "/" + item.name)
        except OSError:
            pass

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

        try:
            Path(item).rename(copyFilePath)
        except OSError:
            if question == 6:
                shutil.move(item, copyFilePath)
            else:
                print("no remplazado")

    def organizeByMonth(organizedFolderPath, item, imgSubFolder, question):
        creationMonthName = calendar.month_name[datetime.date.fromtimestamp(os.path.getmtime(item)).month].capitalize()
        monthFolder = organizedFolderPath + "/" + imgSubFolder + "/" + creationMonthName

        copyFilePath = monthFolder + "/" + item.name

        os.makedirs(monthFolder, exist_ok=True)

        try:
            Path(item).rename(copyFilePath)
        except OSError:
            if question == 6:
                shutil.move(item, copyFilePath)
            else:
                print("no remplazado")
