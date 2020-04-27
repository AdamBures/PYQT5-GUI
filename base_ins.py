from PyQt5 import QtCore, QtGui, QtWidgets


class fin(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(437, 463)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 190, 421, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 240, 421, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(40, 300, 121, 41))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.isTristate()
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(294, 382, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(QtWidgets.qApp.quit)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 411, 131))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 437, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Finished!!!"))
        self.label_2.setText(_translate(
            "MainWindow", "Everything succesfully installed you can close the installation safely"))
        self.label_3.setText(_translate(
            "MainWindow", "Or you can start the program"))
        self.checkBox.setText(_translate("MainWindow", "Start the program"))
        self.pushButton.setText(_translate("MainWindow", "Finish"))
        self.label.setText(_translate("MainWindow", "INSTALL"))


class ins(object):
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
        self.exit.clicked.connect(QtWidgets.qApp.quit)
        self.Install = QtWidgets.QPushButton(self.centralwidget)
        self.Install.setGeometry(QtCore.QRect(326, 380, 101, 23))
        self.Install.setCheckable(True)
        self.Install.setObjectName("Install")
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

        self.Install.clicked.connect(self.installing)

        self.complete = 0
        while self.complete < 100:
            self.complete += 0.001
            self.installbar.setValue(self.complete)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Installing..."))
        self.install.setText(_translate("MainWindow", "Installation"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.Install.setText(_translate("MainWindow", "Install"))
        self.label.setText(_translate(
            "MainWindow", "Be patient we are setting everything what you need. :)"))
        self.label_2.setText(_translate("MainWindow", "Installing"))

    def installing(self, MainWindow):
        self.window1 = QtWidgets.QMainWindow()
        self.ui = fin()
        self.ui.setupUi(self.window1)
        self.window1.show()


class agr(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(539, 449)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 70, 511, 271))
        self.textBrowser.setObjectName("textBrowser")
        self.Accept = QtWidgets.QRadioButton(self.centralwidget)
        self.Accept.setGeometry(QtCore.QRect(30, 350, 82, 17))
        self.Accept.setObjectName("Accept")
        self.Decline = QtWidgets.QRadioButton(self.centralwidget)
        self.Decline.setGeometry(QtCore.QRect(30, 380, 82, 17))
        self.Decline.setObjectName("Decline")
        self.Decline.isChecked()
        self.Install = QtWidgets.QPushButton(self.centralwidget)
        self.Install.setGeometry(QtCore.QRect(326, 380, 101, 23))
        self.Install.setObjectName("Install")
        self.Install.clicked.connect(lambda: self.check(
            self.Decline.isChecked(), self.label, self.user))
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(430, 380, 101, 23))
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(QtWidgets.qApp.quit)
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

        self.Install.clicked.connect(self.user)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Agreements"))
        self.label.setText(_translate("MainWindow", "User agreement"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Click accept if you accept with <span style=\" font-weight:600;\">installation</span> our super duper program into your program :)</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Click decline if you don\'t accept with installing something into your computer. </p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Accept.setText(_translate("MainWindow", "Accept"))
        self.Decline.setText(_translate("MainWindow", "Decline"))
        self.Install.setText(_translate("MainWindow", "Install"))
        self.exit.setText(_translate("MainWindow", "Exit"))

    def user(self, MainWindow):
        self.window1 = QtWidgets.QMainWindow()
        self.ui = ins()
        self.ui.setupUi(self.window1)
        self.window1.show()

    def check(self, chk, label, button):

        if chk:
            self.label.setText("Please set Agree")


class Base(object):  # Done Hurray!!!
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(348, 460)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.infotext = QtWidgets.QLabel(self.centralwidget)
        self.infotext.setGeometry(QtCore.QRect(20, 160, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.infotext.setFont(font)
        self.infotext.setObjectName("infotext")
        self.Install = QtWidgets.QPushButton(self.centralwidget)
        self.Install.setGeometry(QtCore.QRect(136, 390, 101, 23))
        self.Install.setObjectName("Install")
        self.Install.clicked.connect(self.install)
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(240, 390, 101, 23))
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(QtWidgets.qApp.quit)
        self.infotext_2 = QtWidgets.QLabel(self.centralwidget)
        self.infotext_2.setGeometry(QtCore.QRect(20, 210, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.infotext_2.setFont(font)
        self.infotext_2.setObjectName("infotext_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 390, 111, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(16, 12, 321, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 348, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Instalator"))
        self.infotext.setText(_translate(
            "MainWindow", "Press install to install the program"))
        self.Install.setText(_translate("MainWindow", "Install"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.infotext_2.setText(_translate(
            "MainWindow", "Press exit to exit the program"))
        self.label.setText(_translate("MainWindow", "Made by Adam @2019"))
        self.label_2.setText(_translate("MainWindow", "INSTALL"))

    def install(self, MainWindow):
        self.window1 = QtWidgets.QMainWindow()
        self.ui = agr()
        self.ui.setupUi(self.window1)
        self.window1.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Base()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
