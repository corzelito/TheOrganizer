import ctypes

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from Config.Config import changeValues
from Files.Extensions import *


class extensionsWindowUI(QMainWindow):
    def __init__(self, buttonIndex):
        super().__init__()
        uic.loadUi("ui/extensionsWindow.ui", self)
        self.setWindowTitle("Extensiones")
        self.loadConfig(buttonIndex)
        self.cmbExtensions.addItems(Extensions.types)
        self.cmbExtensions.currentIndexChanged.connect(self.selectionchange)
        self.btntoRight.clicked.connect(self.moveToRight)
        self.btntoLeft.clicked.connect(self.moveToLeft)
        self.btntoAllRight.clicked.connect(self.moveAllToRight)
        self.btntoAllLeft.clicked.connect(lambda: self.moveAllToLeft(self.cmbExtensions.currentIndex()))
        self.saveButton.clicked.connect(lambda: self.saveValue(buttonIndex))

    def loadConfig(self, buttonIndex):
        Extensions.addItemsToList2(self, buttonIndex)

    def selectionchange(self, comboIndex):
        if comboIndex == 0:
            self.listWidget.clear()
        else:
            Extensions.addItemsToList1(self, sorted(Extensions.extensions[comboIndex - 1]))

    def moveToRight(self):
        for row in Extensions.getRows(self):
            self.listWidget_2.addItem(self.listWidget.takeItem(row))

    def moveToLeft(self):
        for row in Extensions.getRowsList2(self):
            self.listWidget_2.takeItem(row)

    def moveAllToRight(self):
        while self.listWidget.count() > 0:
            self.listWidget_2.addItem(self.listWidget.takeItem(0))

    def moveAllToLeft(self, comboIndex):
        while self.listWidget_2.count() > 0:
            self.listWidget_2.takeItem(0)
        Extensions.addItemsToList1(self, sorted(Extensions.extensions[comboIndex - 1]))

        if comboIndex == 0:
            self.listWidget.clear()

    def saveValue(self, buttonIndex):
        extensionFolder = "extensionsfolder" + str(buttonIndex)

        extensionConfig = ''
        for i in Extensions.getList2(self):
            extensionConfig += i + " , "
        extensionConfig = extensionConfig[:-2]

        changeValues("extensions", str(extensionFolder), extensionConfig)

        ctypes.windll.user32.MessageBoxW(0, "Se han guardado todos tus ajustes correctamente", "Guardado completado", 0)