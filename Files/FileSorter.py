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
                FileSorter.organizeFiles(organizedFolderPath, item, subfolders[i], question,
                                         organizeByYear, organizeByMonth)
        try:
            Path(item).rename(organizedFolderPath + "/" + "Otros" + "/" + item.name)
        except OSError:
            pass

    def organizeFiles(organizedFolderPath, item, subfolder, question, organizeByYear, organizeByMonth):

        year = datetime.date.fromtimestamp(os.path.getmtime(item)).year
        yearFolder = organizedFolderPath + "/" + subfolder + "/" + str(year)
        creationMonthName = calendar.month_name[datetime.date.fromtimestamp(os.path.getmtime(item)).month].capitalize()
        monthFolder = yearFolder + "/" + creationMonthName

        # Organize by year and month
        if organizeByYear == "True" and organizeByMonth == "True":
            copyFilePath = monthFolder + "/" + item.name
            os.makedirs(yearFolder, exist_ok=True)
            os.makedirs(monthFolder, exist_ok=True)
        # Organize by year
        elif organizeByYear == "True" and organizeByMonth == "False":
            copyFilePath = yearFolder + "/" + item.name
            os.makedirs(yearFolder, exist_ok=True)
        # Organize by month
        elif organizeByYear == "False" and organizeByMonth == "True":
            monthFolder = organizedFolderPath + "/" + subfolder + "/" + creationMonthName
            copyFilePath = monthFolder + "/" + item.name
            os.makedirs(monthFolder, exist_ok=True)
        # Organize without filters
        else:
            copyFilePath = organizedFolderPath + "/" + subfolder + "/" + item.name

        try:
            Path(item).rename(copyFilePath)
        except OSError:
            if question == 6:
                shutil.move(item, copyFilePath)
            else:
                print("no remplazado")
