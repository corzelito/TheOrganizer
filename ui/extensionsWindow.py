from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from Files.Extensions import Extensions
from Files.Extensions import *





class extensionsWindowUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/extensionsWindow.ui", self)
        self.setWindowTitle("Extensiones")
        types = ('', 'Imágenes', 'Vídeo', 'Música', 'Documentos', 'Otros')

        self.cmbExtensions.addItems(types)
        self.cmbExtensions.currentIndexChanged.connect(self.selectionchange)
        self.btntoRight.clicked.connect(self.moveToRight)
        # self.btnTest.clicked.connect(self.getList2Data)

    def moveToRight(self):
        for row in Extensions.getRows(self):
            self.listWidget_2.addItem(self.listWidget.takeItem(row))

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


    def get_left_elements(self):
        r = []
        for i in range(self.mInput.count()):
            it = self.mInput.item(i)
            r.append(it.text())
        return r

    def get_right_elements(self):
        r = []
        for i in range(self.mOuput.count()):
            it = self.mOuput.item(i)
            r.append(it.text())
        return r
    
    def moveSelected_clicked(self):
        for i in Extensions.getList(self):
            if i in Extensions.getList2(self):
                print("está", i)
            else:
                # print(row)
                print("no esta", i)
                self.listWidget_2.addItem(self.listWidget.takeItem(self.listWidget.currentRow()))
      

    def moveAll_clicked(self):
        while self.listWidget.count() > 0:
            self.listWidget_2.addItem(self.listWidget.takeItem(0))
    # def getListData2(self):
    #     itemsInList2 = []
    #     for index in range(self.listWidget_2.count()):
    #         itemsInList2.append(self.listWidget_2.item(index).text())
    #
    #     return itemsInList2