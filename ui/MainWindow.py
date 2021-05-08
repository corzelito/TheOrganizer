import ctypes
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

from Config.Config import getSubfolders, makeConfigFile, getConfigValue
from Files.FileSorter import FileSorter
from Files.Folder import Folder
from ui.ConfigWindow import ConfigWindowUI


class UI(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("ui/mainWindow.ui", self)
        makeConfigFile()
        self.choosePathEntryButton.clicked.connect(self.getPathEntry)
        self.choosePathOrganizedButton.clicked.connect(self.getPathEntryOrganized)
        self.organizeButton.clicked.connect(self.organize)
        self.configButton.clicked.connect(self.ConfigWindow)
        self.progressBar.setValue(0)
        self.progressBar.hide()

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
        subfolders = getSubfolders()
        organizedFolderPath = self.labelPathEntryOrganized.toPlainText()

        # Testing
        if path == "" and organizedFolderPath == "":
            path = "C:\\Users\\Adri\\Desktop\\pruebas"
            organizedFolderPath = "C:\\Users\\Adri\\Desktop\\pruebas2"

        # YES = 6 // NO = 7
        # print(getConfigValue("ReplaceFiles", "ReplaceFiles"))
        if getConfigValue("ReplaceFiles", "ReplaceFiles") == "False":
            question = ctypes.windll.user32.MessageBoxW(0, "La opción 'No remplazar' está desactivada, en caso de tener archivos iguales en la carpeta de destino, se sobrescribiran, ¿Quieres continuar?", "Aviso", 4)
        else:
            question = 6

        Folder.makefolders(organizedFolderPath)
        FileSorter.browseFiles(path, organizedFolderPath, question)

        if question == 6:
            ctypes.windll.user32.MessageBoxW(0, "Se ha organizado todo correctamente", "Organizacion completada", 0)



    def ConfigWindow(self):
        self.w = ConfigWindowUI()
        self.w.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = UI()
    GUI.show()
    sys.exit(app.exec())
