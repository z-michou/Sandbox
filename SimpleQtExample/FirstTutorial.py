__author__ = 'igore_000'

import sys
from PySide.QtCore import *
from PySide.QtGui import *

def toggleOn():
    label.show()
    QTimer.singleShot(700, toggleOff)

def toggleOff():
    label.hide()
    QTimer.singleShot(200, toggleOn)


app = QApplication(sys.argv)

label = QLabel('This is a message on a transparent label')

label.setStyleSheet('color: red; font: italic bold 30pt')
label.setWindowFlags(Qt.FramelessWindowHint)
label.setAttribute(Qt.WA_TranslucentBackground)
label.setAttribute(Qt.WA_ShowWithoutActivating)

toggleOn()
QTimer.singleShot(5000, app.quit)
app.exec_()
