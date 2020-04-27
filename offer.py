# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Offer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Offer")
        MainWindow.resize(466, 381)
        self.icon = QtGui.QIcon("pcicon.png")
        self.picture = QtWidgets.QLabel(MainWindow)
        self.picture.setGeometry(QtCore.QRect(180, 120, 91, 81))
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap("G:/Nová složka/Projekty/Python projekty/pcicon.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.turn_off = QtWidgets.QPushButton(self.centralwidget)
        self.turn_off.setGeometry(QtCore.QRect(70, 270, 61, 61))
        self.turn_off.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.turn_off.setObjectName("turn_off")
        self.restart = QtWidgets.QPushButton(self.centralwidget)
        self.restart.setGeometry(QtCore.QRect(200, 270, 61, 61))
        self.restart.setObjectName("restart")
        self.sleep = QtWidgets.QPushButton(self.centralwidget)
        self.sleep.setGeometry(QtCore.QRect(340, 270, 61, 61))
        self.sleep.setObjectName("sleep")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("TurnOffer", "TurnOffer"))
        self.turn_off.setText(_translate("MainWindow", "Off"))
        self.restart.setText(_translate("MainWindow", "Restart"))
        self.sleep.setText(_translate("MainWindow", "Sleep"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
