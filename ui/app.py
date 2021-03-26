import os
import sys
import calendar
import datetime
from pathlib import Path
from tkinter import filedialog

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QCheckBox
import ctypes


class UI(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("ui/gui.app.ui", self)
        #uic.loadUi("gui.app.ui", self)
        self.choosePathEntryButton.clicked.connect(self.getPathEntry)
        self.choosePathOrganizedButton.clicked.connect(self.getPathEntryOrganized)
        self.organizeButton.clicked.connect(self.organize)


    def getPathEntry(self):
        dialog = QFileDialog()
        foo_dir = dialog.getExistingDirectory(self, 'Select an awesome directory')
        self.labelPathEntry.setPlainText(foo_dir)

    def getPathEntryOrganized(self):
        dialog = QFileDialog()
        foo_dir = dialog.getExistingDirectory(self, 'Select an awesome directory')
        self.labelPathEntryOrganized.setPlainText(foo_dir)


    def organize(self):
        path = self.labelPathEntry.toPlainText()
       # if len(path) != 0:
        subfolders = ['Imagenes', 'Videos', 'Documentos', 'Otros']
        organizedFolderPath = self.labelPathEntryOrganized.toPlainText()
        checkConfig = [self.chkorganizeByYear.isChecked, self.chkorganizeByMonth.isChecked()]

        # #Testing
        # path = "C:\\Users\\Adri\\Desktop\\pruebas"
        # organizedFolderPath = "C:\\Users\\Adri\\Desktop\\pruebasFicherosExtraidos"

        makefolders(organizedFolderPath, subfolders)
        browseFiles(path, organizedFolderPath, subfolders, checkConfig)
         #0 = ok, 1 = 0k, cancel

        ctypes.windll.user32.MessageBoxW(0, "Se ha organizado todo correctamente", "Organizacion completada", 0)


def search_for_file_path():
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    return tempdir


def makefolders(path, subfolders):
    os.makedirs(path, exist_ok=True)
    for i in subfolders:
        os.makedirs(path + "/" + i, exist_ok=True)


def deleteAllFolders(path):
    directory = Path(path)
    for item in directory.iterdir():
        if item.is_dir():
            deleteAllFolders(item)
        else:
            item.unlink()
    directory.rmdir()


def browseFiles(path, organizedFolderPath, subfolders, checkConfig):
    directory = Path(path)
    for item in directory.iterdir():
        if item.is_dir():
            browseFiles(item, organizedFolderPath, subfolders, checkConfig)
        else:
            organizeFileByExtension(item, organizedFolderPath, subfolders, checkConfig)


def organizeFileByExtension(item, organizedFolderPath, subfolders, checkConfig):
    images = [".png", ".jpg", ".jpeg"]
    documents = [".doc", ".pdf", ".docx"]
    videos = [".mp4", ".mov"]

    extension = str(os.path.splitext(item)[1]).lower()
    chkorganizeByYear = checkConfig[0]
    chkorganizeByMonth = checkConfig[1]

    if extension in images:
        if (chkorganizeByMonth and chkorganizeByYear):
            organizeByYearAndMonth(organizedFolderPath, item, subfolders[0])
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = UI()
    GUI.show()
    sys.exit(app.exec())
