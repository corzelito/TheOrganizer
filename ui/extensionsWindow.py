from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from Files.Extensions import Extensions


class extensionsWindowUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/extensionsWindow.ui", self)
        self.setWindowTitle("Extensiones")
        types = ('', 'Imágenes', 'Vídeo', 'Música', 'Documentos', 'Otros')

        self.cmbExtensions.addItems(types)
        self.cmbExtensions.currentIndexChanged.connect(self.selectionchange)
        self.btntoRight.clicked.connect(self.moveToRight)

    def moveToRight(self):
        rows = sorted([index.row() for index in self.listWidget.selectedIndexes()],
                      reverse=True)
        for row in rows:
            # assuming the other listWidget is called listWidget_2
            self.listWidget_2.addItem(self.listWidget.takeItem(row))

    def selectionchange(self, comboIndex):
        if comboIndex == 0:
            self.listWidget.clear()
        elif comboIndex == 1:
            self.listWidget.clear()
            self.listWidget.addItems(Extensions.images)
        elif comboIndex == 2:
            self.listWidget.clear()
            self.listWidget.addItems(Extensions.video)
        elif comboIndex == 3:
            self.listWidget.clear()
            self.listWidget.addItems(Extensions.music)
        elif comboIndex == 4:
            self.listWidget.clear()
            self.listWidget.addItems(Extensions.document)
        elif comboIndex == 5:
            self.listWidget.clear()
            self.listWidget.addItems(Extensions.all)
