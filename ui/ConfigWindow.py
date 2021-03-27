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
        # print(self.chkorganizeByYear.isChecked())
        chkorganizeByYearValue = str(self.chkorganizeByYear.isChecked())
        chkorganizeByMonthValue = str(self.chkorganizeByMonth.isChecked())

        changeValues("OrderBy", "orderbyyear", chkorganizeByYearValue)
        changeValues("OrderBy", "orderbymonth", chkorganizeByMonthValue)
        print("Se han guardado los valores")