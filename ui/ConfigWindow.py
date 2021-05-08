import ast
import ctypes

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from Config.Config import changeValues, getConfigValue
from ui.extensionsWindow import extensionsWindowUI


class ConfigWindowUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/configWindow.ui", self)
        self.setWindowTitle("Configuración")
        self.loadConfig()
        self.saveButton.clicked.connect(self.saveValue)
        self.configButton.clicked.connect(lambda: self.openExtensionWindow(1))
        self.configButton_2.clicked.connect(lambda: self.openExtensionWindow(2))
        self.configButton_3.clicked.connect(lambda: self.openExtensionWindow(3))
        self.configButton_4.clicked.connect(lambda: self.openExtensionWindow(4))

    def loadConfig(self):
        self.txtFolder1.setPlainText(getConfigValue("Subfolders", "folder1"))
        self.txtFolder2.setPlainText(getConfigValue("Subfolders", "folder2"))
        self.txtFolder3.setPlainText(getConfigValue("Subfolders", "folder3"))
        self.txtFolder4.setPlainText(getConfigValue("Subfolders", "folder4"))

        # Folder1
        self.chkorganizeByYearFolder1.setChecked(ast.literal_eval(getConfigValue("Folder1", "orderbyyear")))
        self.chkorganizeByMonthFolder1.setChecked(ast.literal_eval(getConfigValue("Folder1", "orderbymonth")))

        # Folder2
        self.chkorganizeByYearFolder2.setChecked(ast.literal_eval(getConfigValue("Folder2", "orderbyyear")))
        self.chkorganizeByMonthFolder2.setChecked(ast.literal_eval(getConfigValue("Folder2", "orderbymonth")))

        # Folder3
        self.chkorganizeByYearFolder3.setChecked(ast.literal_eval(getConfigValue("Folder3", "orderbyyear")))
        self.chkorganizeByMonthFolder3.setChecked(ast.literal_eval(getConfigValue("Folder3", "orderbymonth")))

        # Folder4
        self.chkorganizeByYearFolder4.setChecked(ast.literal_eval(getConfigValue("Folder4", "orderbyyear")))
        self.chkorganizeByMonthFolder4.setChecked(ast.literal_eval(getConfigValue("Folder4", "orderbymonth")))

    def saveValue(self):
        txtFolder1 = self.txtFolder1.toPlainText()
        txtFolder2 = self.txtFolder2.toPlainText()
        txtFolder3 = self.txtFolder3.toPlainText()
        txtFolder4 = self.txtFolder4.toPlainText()

        changeValues("Subfolders", "folder1", txtFolder1)
        changeValues("Subfolders", "folder2", txtFolder2)
        changeValues("Subfolders", "folder3", txtFolder3)
        changeValues("Subfolders", "folder4", txtFolder4)

        # Folder1
        chkorganizeByYearValueFolder1 = str(self.chkorganizeByYearFolder1.isChecked())
        chkorganizeByMonthValueFolder1 = str(self.chkorganizeByMonthFolder1.isChecked())

        changeValues("Folder1", "orderbyyear", chkorganizeByYearValueFolder1)
        changeValues("Folder1", "orderbymonth", chkorganizeByMonthValueFolder1)

        # Folder2
        chkorganizeByYearValueFolder2 = str(self.chkorganizeByYearFolder2.isChecked())
        chkorganizeByMonthValueFolder2 = str(self.chkorganizeByMonthFolder2.isChecked())
        changeValues("Folder2", "orderbyyear", chkorganizeByYearValueFolder2)
        changeValues("Folder2", "orderbymonth", chkorganizeByMonthValueFolder2)

        # Folder3
        chkorganizeByYearValueFolder3 = str(self.chkorganizeByYearFolder3.isChecked())
        chkorganizeByMonthValueFolder3 = str(self.chkorganizeByMonthFolder3.isChecked())
        changeValues("Folder3", "orderbyyear", chkorganizeByYearValueFolder3)
        changeValues("Folder3", "orderbymonth", chkorganizeByMonthValueFolder3)

        # Folder4
        chkorganizeByYearValueFolder4 = str(self.chkorganizeByYearFolder4.isChecked())
        chkorganizeByMonthValueFolder4 = str(self.chkorganizeByMonthFolder4.isChecked())
        changeValues("Folder4", "orderbyyear", chkorganizeByYearValueFolder4)
        changeValues("Folder4", "orderbymonth", chkorganizeByMonthValueFolder4)

        ctypes.windll.user32.MessageBoxW(0, "Se han guardado todos tus ajustes correctamente", "Guardado completado", 0)

    def openExtensionWindow(self, buttonIndex):
        self.message = buttonIndex
        self.w = extensionsWindowUI(self.message)
        self.w.show()
