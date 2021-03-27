import distutils
from distutils.util import strtobool

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from Config.Config import changeValues


class ConfigWindowUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/configWindow.ui", self)
        self.setWindowTitle("Configuracion")
        self.saveButton.clicked.connect(self.saveValue)

    def saveValue(self):
        chkorganizeByYearValue = str(self.chkorganizeByYear.isChecked())
        chkorganizeByMonthValue = str(self.chkorganizeByMonth.isChecked())
        txtFolder1 = self.txtFolder1.toPlainText()
        txtFolder2 = self.txtFolder2.toPlainText()
        txtFolder3 = self.txtFolder3.toPlainText()
        txtFolder4 = self.txtFolder4.toPlainText()


        changeValues("Subfolders", "folder1", txtFolder1)
        changeValues("Subfolders", "folder2", txtFolder2)
        changeValues("Subfolders", "folder3", txtFolder3)
        changeValues("Subfolders", "folder4", txtFolder4)

        changeValues("OrderBy", "orderbyyear", chkorganizeByYearValue)
        changeValues("OrderBy", "orderbymonth", chkorganizeByMonthValue)
        # changeValues("Subfolders", "folder1", txtFolder1)
        print("Se han guardado los valores")