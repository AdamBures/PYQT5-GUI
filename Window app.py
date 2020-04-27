import sys
from PyQt5 import QtWidgets, QtGui
import os

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "C:\PyQt"


def window():

    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.setWindowTitle("Windowed app")
    label = QtWidgets.QLabel(w)
    label.setText("Hello there")
    w.setGeometry(100, 100, 300, 200)
    label.move(100, 20)
    w.show()
    sys.exit(app.exec_())


window()
