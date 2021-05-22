import locale
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

import ui
import gettext
from ui.MainWindow import UI
from Files.Languages import *
from Config import *

if __name__ == '__main__':

    Config.makeConfigFile()
    Languages.setLanguage()

    app = QApplication(sys.argv)
    icon_name = 'ui/app_icon.png'
    app.setWindowIcon(QIcon(icon_name))
    GUI = ui.MainWindow.UI()
    GUI.show()
    sys.exit(app.exec())
