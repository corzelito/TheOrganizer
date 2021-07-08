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
        self.translateStrings()


    def getPathEntry(self):
        dialog = QFileDialog()
        foo_dir = dialog.getExistingDirectory(self, _("Select an awesome directory"))
        self.labelPathEntry.setPlainText(foo_dir)

    def getPathEntryOrganized(self):
        dialog = QFileDialog()
        foo_dir = dialog.getExistingDirectory(self, _("Select an awesome directory"))
        self.labelPathEntryOrganized.setPlainText(foo_dir)

    def organize(self):
        pathEntry = self.labelPathEntry.toPlainText()
        pathEntryOrganized = self.labelPathEntryOrganized.toPlainText()
        if len(pathEntry) != 0 and len(pathEntryOrganized) != 0:
            organizedFolderPath = self.labelPathEntryOrganized.toPlainText()
            # YES = 6 // NO = 7
            if getConfigValue("ReplaceFiles", "ReplaceFiles") == "False":
                question = ctypes.windll.user32.MessageBoxW(0, _(
                    "The option 'Do not replace' is disabled, if you have the same files in the destination folder, they will be overwritten, do you want to continue?"),_("Warning"), 4)
            else:
                question = 6

            Folder.makefolders(organizedFolderPath)
            FileSorter.browseFiles(pathEntry, organizedFolderPath, question)

            if question == 6:
                ctypes.windll.user32.MessageBoxW(0, _("Everything has been organized correctly."), _("Organization completed."), 0)
        else:
            ctypes.windll.user32.MessageBoxW(0, _("Fill in the fields."),
                                             "Error", 0)

    def translateStrings(self):
        self.choosePathEntryButton.setText(_("Explore"))
        self.choosePathOrganizedButton.setText(_("Explore"))
        self.organizeButton.setText(_("Organize"))
        self.labelOrigin.setText(_("Folder to order:"))
        self.labelOrganizedFolderPath.setText(_("Folder where it will be organized:"))

    def ConfigWindow(self):
        self.w = ConfigWindowUI()
        self.w.show()

