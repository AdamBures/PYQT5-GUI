# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regist.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(285, 347)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username1 = QtWidgets.QLabel(self.centralwidget)
        self.username1.setGeometry(QtCore.QRect(10, 30, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.username1.setFont(font)
        self.username1.setObjectName("username1")
        self.pass1 = QtWidgets.QLabel(self.centralwidget)
        self.pass1.setGeometry(QtCore.QRect(10, 100, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pass1.setFont(font)
        self.pass1.setObjectName("pass1")
        self.reg_but = QtWidgets.QPushButton(self.centralwidget)
        self.reg_but.setGeometry(QtCore.QRect(40, 210, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.reg_but.setFont(font)
        self.reg_but.setObjectName("reg_but")
        self.email1 = QtWidgets.QLabel(self.centralwidget)
        self.email1.setGeometry(QtCore.QRect(10, 150, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.email1.setFont(font)
        self.email1.setObjectName("email1")
        self.usr_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.usr_edit.setGeometry(QtCore.QRect(120, 40, 151, 31))
        self.usr_edit.setObjectName("usr_edit")
        self.pass_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.pass_edit.setGeometry(QtCore.QRect(120, 90, 151, 31))
        self.pass_edit.setObjectName("pass_edit")
        self.email_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.email_edit.setGeometry(QtCore.QRect(120, 140, 151, 31))
        self.email_edit.setObjectName("email_edit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 285, 21))
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
        self.username1.setText(_translate("MainWindow", "Username:"))
        self.pass1.setText(_translate("MainWindow", "Password:"))
        self.reg_but.setText(_translate("MainWindow", "Register"))
        self.email1.setText(_translate("MainWindow", "Email:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
