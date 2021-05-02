from Config.Config import getConfigValue


class Extensions:
    archives = (
        ".7z", ".a", ".apk", ".ar", ".bz2", ".cab", ".cpio", ".deb", ".dmg", ".egg", ".gz", ".iso", ".jar", ".lha",
        ".mar", ".pea", ".rar", ".rpm", ".s7z", ".shar", ".tar", ".tbz2", ".tgz", ".tlz", ".war",
        ".whl", ".xpi", ".zip", ".zipx", ".xz", ".pak"
    )

    audio = (
        ".aac", ".aiff", ".ape", ".au", ".flac", ".gsm", ".it", ".m3u", ".m4a", ".mid", ".mod", ".mp3", ".mpa", ".pls",
        ".ra", ".s3m", ".sid", ".wav", ".wma", ".xm"
    )

    book = (
        ".mobi", ".epub", ".azw1", ".azw3", ".azw4", ".azw6", ".azw", ".cbr", ".cbz"
    )

    code = (
        ".c", ".cc", ".class", ".clj", ".cpp", ".cs", ".cxx", ".el", ".go", ".h", ".java", ".lua", ".m", ".m4", ".php",
        ".pl", ".po", ".py", ".rb", ".rs", ".sh", ".swift", ".vb", ".vcxproj", ".xcodeproj", ".xml", ".diff", ".patch",
        ".html", ".js"
    )

    exec = (
        ".exe", ".msi", ".bin", ".command", ".sh", ".bat", ".crx"
    )

    font = (
        ".eot", ".otf", ".ttf", ".woff", ".woff2"
    )

    images = (
        ".3dm", ".3ds", ".max", ".bmp", ".dds", ".gif", ".jpg", ".jpeg", ".png", ".psd", ".xcf", ".tga", ".thm", ".tif",
        ".tiff", ".yuv", ".ai", ".eps", ".ps", ".svg", ".dwg", ".dxf", ".gpx", ".kml", ".kmz", ".webp"
    )

    sheet = (
        ".ods", ".xls", ".xlsx", ".csv", ".ics", ".vcf"
    )

    slide = (
        ".ppt", ".odp"
    )

    text = (
        ".doc", ".docx", ".ebook", ".log", ".md", ".msg", ".odt", ".org", ".pages", ".pdf", ".rtf", ".rst", ".tex",
        ".txt", ".wpd", ".wps"
    )

    video = (
        ".3g2", ".3gp", ".aaf", ".asf", ".avchd", ".avi", ".drc", ".flv", ".m2v", ".m4p", ".m4v", ".mkv", ".mng",
        ".mov", ".mp2", ".mp4", ".mpe", ".mpeg", ".mpg", ".mpv", ".mxf", ".nsv", ".ogg", ".ogv", ".ogm", ".qt", ".rm",
        ".rmvb", ".roq", ".srt", ".svi", ".vob", ".webm", ".wmv", ".yuv")

    web = (
        ".html", ".htm", ".css", ".js", ".jsx", ".less", ".scss", ".wasm", ".php"
    )

    all = images + video + audio + text

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
