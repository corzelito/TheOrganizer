import locale
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

import ui
from ui.app import UI

if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, 'ES')
    app = QApplication(sys.argv)
    icon_name = 'ui/app_icon.png'
    app.setWindowIcon(QIcon(icon_name))
    GUI = ui.app.UI()
    GUI.show()

    GUI.setFixedSize(GUI.size())
    sys.exit(app.exec())
