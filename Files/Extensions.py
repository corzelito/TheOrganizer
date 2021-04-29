from Config.Config import getConfigValue


class Extensions:
    images = (
        ".jpg",
        ".png"
    )

    video = (
        ".mp4",
        ".mov"
    )

    music = (
        ".mp3",
    )

    document = (
        ".doc",
    )

    all = images + video + music + document

    def getList(self):
        itemsInList = []
        for index in range(self.listWidget.count()):
            itemsInList.append(self.listWidget.item(index).text())
        return itemsInList

    def getList2(self):
        itemsInList2 = []
        for index in range(self.listWidget_2.count()):
            itemsInList2.append(self.listWidget_2.item(index).text())
        return itemsInList2

    def addItemsToList1(self, extension):
        self.listWidget.clear()
        array = []
        for i in extension:
            if i not in Extensions.getList2(self):
                array.append(i)
        self.listWidget.addItems(array)

    def addItemsToList2(self):
        array = []
        extensions = getConfigValue("extensions", "extensionsfolder1").split(" , ")

        for i in extensions:
            array.append(i)

        self.listWidget_2.addItems(array)


    def getRows(self):
        rows = sorted([index.row() for index in self.listWidget.selectedIndexes()],
                reverse=True)
        return rows

    def getRowsList2(self):
        rows = sorted([index.row() for index in self.listWidget_2.selectedIndexes()],
                reverse=True)
        return rows