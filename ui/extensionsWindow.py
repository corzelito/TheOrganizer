from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from Config.Config import changeValues
from Files.Extensions import *


class extensionsWindowUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/extensionsWindow.ui", self)
        self.setWindowTitle("Extensiones")
        self.loadConfig()
        types = ('', 'Archivos', 'Audio', 'Código', 'Ejecutables', 'Fuentes', 'Hojas de cálculo', 'Imágenes', 'Libros',
                 'Presentaciones', 'Texto', 'Vídeo', 'Web', 'Todos')

        self.cmbExtensions.addItems(types)
        self.cmbExtensions.currentIndexChanged.connect(self.selectionchange)
        self.btntoRight.clicked.connect(self.moveToRight)
        self.btntoLeft.clicked.connect(self.moveToLeft)
        self.btntoAllRight.clicked.connect(self.moveAllToRight)
        self.btntoAllLeft.clicked.connect(self.moveAllToLeft)
        self.saveButton.clicked.connect(self.saveValue)

    def moveToRight(self):
        for row in Extensions.getRows(self):
            self.listWidget_2.addItem(self.listWidget.takeItem(row))

    def moveToLeft(self):
        for row in Extensions.getRowsList2(self):
            self.listWidget.addItem(self.listWidget_2.takeItem(row))

    def selectionchange(self, comboIndex):
        if comboIndex == 0:
            self.listWidget.clear()
        else:
            Extensions.addItemsToList1(self, sorted(Extensions.extensions[comboIndex - 1]))

    def loadConfig(self):
        Extensions.addItemsToList2(self)

    def saveValue(self):
        array = ''
        for i in Extensions.getList2(self):
            array += i + " , "
        array = array[:-2]

        changeValues("extensions", "extensionsfolder1", array)
        # TODO QUE FUNCIONE CON TODOS LOS BOTONES

    def moveAllToRight(self):
        while self.listWidget.count() > 0:
            self.listWidget_2.addItem(self.listWidget.takeItem(0))

    def moveAllToLeft(self):
        while self.listWidget_2.count() > 0:
            self.listWidget.addItem(self.listWidget_2.takeItem(0))
