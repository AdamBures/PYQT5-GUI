# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'installation_instalator.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(539, 449)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.installbar = QtWidgets.QProgressBar(self.centralwidget)
        self.installbar.setGeometry(QtCore.QRect(50, 150, 441, 23))
        self.installbar.setMaximum(100)
        self.installbar.setProperty("value", 0)
        self.installbar.setObjectName("installbar")
        self.install = QtWidgets.QLabel(self.centralwidget)
        self.install.setGeometry(QtCore.QRect(20, 10, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.install.setFont(font)
        self.install.setObjectName("install")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(434, 380, 101, 23))
        self.exit.setObjectName("exit")
        self.Install = QtWidgets.QPushButton(self.centralwidget)
        self.Install.setGeometry(QtCore.QRect(326, 380, 101, 23))
        self.Install.setCheckable(True)
        self.Install.setObjectName("Install")
        self.Install.clicked.connect(self.download)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 200, 471, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 61, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 539, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.install.setText(_translate("MainWindow", "Installation"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.Install.setText(_translate("MainWindow", "Install"))
        self.label.setText(_translate("MainWindow", "Be patient we are setting everything what you need. :)"))
        self.label_2.setText(_translate("MainWindow", "Installing"))

    def download(self, label):
        self.complete = 0
        while self.complete < 100:
            self.complete += 0.001
            self.installbar.setValue(self.complete)
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
