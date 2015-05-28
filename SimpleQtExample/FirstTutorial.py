__author__ = 'igore_000'

import sys
from PySide.QtCore import *
from PySide.QtGui import *

app = QApplication(sys.argv)

label = QLabel('This is a message on a transparent label')

label.setStyleSheet('color: red; font: italic bold 30pt')
label.setWindowFlags(Qt.FramelessWindowHint)
label.setAttribute(Qt.WA_TranslucentBackground)
label.show()

QTimer.singleShot(5000, app.quit)
app.exec_()
