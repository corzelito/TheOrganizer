from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from Config.Config import changeValues
from Files.Extensions import Extensions
from Files.Extensions import *

class extensionsWindowUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/extensionsWindow.ui", self)
        self.setWindowTitle("Extensiones")
        self.loadConfig()
        types = ('', 'Imágenes', 'Vídeo', 'Música', 'Documentos', 'Otros')

        self.cmbExtensions.addItems(types)
        self.cmbExtensions.currentIndexChanged.connect(self.selectionchange)
        self.btntoRight.clicked.connect(self.moveToRight)
        self.saveButton.clicked.connect(self.saveValue)
        self.btnTest.clicked.connect(self.moveToLeft)

    def moveToRight(self):
        for row in Extensions.getRows(self):
            self.listWidget_2.addItem(self.listWidget.takeItem(row))

    def moveToLeft(self):
        for row in Extensions.getRowsList2(self):
            self.listWidget.addItem(self.listWidget_2.takeItem(row))

    def selectionchange(self, comboIndex):
        if comboIndex == 0:
            self.listWidget.clear()
        elif comboIndex == 1:
            Extensions.addItemsToList1(self, Extensions.images)
        elif comboIndex == 2:
            Extensions.addItemsToList1(self, Extensions.video)
        elif comboIndex == 3:
            Extensions.addItemsToList1(self, Extensions.music)
        elif comboIndex == 4:
            Extensions.addItemsToList1(self, Extensions.document)
        elif comboIndex == 5:
            Extensions.addItemsToList1(self, Extensions.all)

    def loadConfig(self):
        Extensions.addItemsToList2(self)
      
    def saveValue(self):
        array = ''
        for i in Extensions.getList2(self):
            array += i + " , "
        array = array[:-2]

        changeValues("extensions", "extensionsfolder1", array)
        #TODO QUE FUNCIONE CON TODOS LOS BOTONES

    def moveAll_clicked(self):
        while self.listWidget.count() > 0:
            self.listWidget_2.addItem(self.listWidget.takeItem(0))
