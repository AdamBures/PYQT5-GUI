
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 133)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 151, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.usd_to_czk)
        self.num = QtWidgets.QLabel(self.centralwidget)
        self.num.setGeometry(QtCore.QRect(420, 30, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num.setFont(font)
        self.num.setObjectName("num")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 133))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Answear"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.num.setText(_translate("MainWindow", "0"))

    def usd_to_czk(self, **kwargs):
        answear = ""
        error = ""
        try:
            a = int(self.textEdit.text())
            usd = 23
            answear = a * usd
            self.usd_to_czk.setText(answear)
        
        except:
                error = "Number not entered!"
        
        if(error):
            self.num.setText(str(round(answear, 3)))

class Ui_Window2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 133)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 151, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.czk_to_usd)
        self.num = QtWidgets.QLabel(self.centralwidget)
        self.num.setGeometry(QtCore.QRect(420, 30, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num.setFont(font)
        self.num.setObjectName("num")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 133))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Answear"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.num.setText(_translate("MainWindow", "0"))

    def czk_to_usd(self, **kwargs):
        answear = ""
        error = ""
        try:
            b = int(self.textEdit.text())
            usd = 23
            answear = b / usd
            self.usd_to_czk.setText(answear)
        
        except:
                error = "Number not entered!"
        
        if(error):
            self.num.setText(str(round(answear, 3)))

class Ui_Window3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 133)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 151, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.eur_to_czk)
        self.num = QtWidgets.QLabel(self.centralwidget)
        self.num.setGeometry(QtCore.QRect(420, 30, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num.setFont(font)
        self.num.setObjectName("num")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 133))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Answear"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.num.setText(_translate("MainWindow", "0"))

    def eur_to_czk(self, **kwargs):
        answear = ""
        error = ""
        try:
            c = int(self.textEdit.text())
            eur = 26
            answear = c * eur
            self.eur_to_czk.setText(answear)
        
        except:
            error = "Number not entered!"
        
        if(error):
            self.num.setText(str(round(answear, 3)))

class Ui_Window4(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 133)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 151, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.czk_to_eur)
        self.num = QtWidgets.QLabel(self.centralwidget)
        self.num.setGeometry(QtCore.QRect(420, 30, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num.setFont(font)
        self.num.setObjectName("num")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 133))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Answear"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.num.setText(_translate("MainWindow", "0"))


    def czk_to_eur(self, **kwargs):
        answear = ""
        error = ""
        try:
            c = int(self.textEdit.text())
            eur = 26
            answear = c / eur
            self.eur_to_czk.setText(answear)
        
        except:
            error = "Number not entered!"
        
        if(error):
            self.num.setText(str(round(answear, 3)))

class Ui_Window5(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 133)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 151, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.rub_to_czk)
        self.num = QtWidgets.QLabel(self.centralwidget)
        self.num.setGeometry(QtCore.QRect(420, 30, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num.setFont(font)
        self.num.setObjectName("num")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 133))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Answear"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.num.setText(_translate("MainWindow", "0"))

    def rub_to_czk(self):
        answear = ""
        error = ""
        try:
            d = int(self.textEdit.text())
            rub = 0.36
            answear = d * rub
            self.rub_to_czk.setText(answear)
        
        except:
            error = "Number not entered!"

        if (error):
            self.num.setText(str(round(answear, 3)))


class Ui_Window6(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 133)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 151, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.czk_to_rub)
        self.num = QtWidgets.QLabel(self.centralwidget)
        self.num.setGeometry(QtCore.QRect(420, 30, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num.setFont(font)
        self.num.setObjectName("num")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 133))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Answear"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.num.setText(_translate("MainWindow", "0"))

    def czk_to_rub(self):
        answear = ""
        error = ""
        try:
            d = int(self.textEdit.text())
            rub = 0.36
            answear = d / rub
            self.czk_to_rub.setText(answear)
        
        except:
            error = "Number not entered!"

        if (error):
            self.num.setText(str(round(answear, 3)))

class Ui_Window7(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 133)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 151, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.aud_to_czk)
        self.num = QtWidgets.QLabel(self.centralwidget)
        self.num.setGeometry(QtCore.QRect(420, 30, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num.setFont(font)
        self.num.setObjectName("num")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 133))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Answear"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.num.setText(_translate("MainWindow", "0"))

    def aud_to_czk(self):
        answear = ""
        error = ""
        try:
            d = int(self.textEdit.text())
            aud = 15.7
            answear = d * aud
            self.aud_to_czk.setText(answear)
        
        except:
            error = "Number not entered!"

        if (error):
            self.num.setText(str(round(answear, 3)))

class Ui_Window8(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 133)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 151, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.czk_to_aud)
        self.num = QtWidgets.QLabel(self.centralwidget)
        self.num.setGeometry(QtCore.QRect(420, 30, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num.setFont(font)
        self.num.setObjectName("num")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 133))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Answear"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.num.setText(_translate("MainWindow", "0"))

    def czk_to_aud(self):
        answear = ""
        error = ""
        try:
            d = int(self.textEdit.text())
            aud = 15.7
            answear = d / aud
            self.czk_to_aud.setText(answear)
        
        except:
            error = "Number not entered!"

        if (error):
            self.num.setText(str(round(answear, 3)))

class Ui_Window9(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 133)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 151, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.gbp_to_czk)
        self.num = QtWidgets.QLabel(self.centralwidget)
        self.num.setGeometry(QtCore.QRect(420, 30, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num.setFont(font)
        self.num.setObjectName("num")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 133))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Answear"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.num.setText(_translate("MainWindow", "0"))

    def gbp_to_czk(self):
        answear = ""
        error = ""
        try:
            d = int(self.textEdit.text())
            gbp = 29.5
            answear = d * gbp
            self.czk_to_aud.setText(answear)
        
        except:
            error = "Number not entered!"

        if (error):
            self.num.setText(str(round(answear, 3)))

class Ui_Window10(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 133)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 151, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.czk_to_gbp)
        self.num = QtWidgets.QLabel(self.centralwidget)
        self.num.setGeometry(QtCore.QRect(420, 30, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num.setFont(font)
        self.num.setObjectName("num")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 133))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Answear"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.num.setText(_translate("MainWindow", "0"))

    def czk_to_gbp(self):
        answear = ""
        error = ""
        try:
            d = int(self.textEdit.text())
            gbp = 29.5
            answear = d / gbp
            self.czk_to_aud.setText(answear)
        
        except:
            error = "Number not entered!"

        if (error):
            self.num.setText(str(round(answear, 3)))


class Ui_Window11(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 133)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 151, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.hrk_to_czk)
        self.num = QtWidgets.QLabel(self.centralwidget)
        self.num.setGeometry(QtCore.QRect(420, 30, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num.setFont(font)
        self.num.setObjectName("num")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 133))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Answear"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.num.setText(_translate("MainWindow", "0"))

    def hrk_to_czk(self):
        answear = ""
        error = ""
        try:
            d = float(self.textEdit.text())
            hrk = 3.42
            answear = d * hrk
            self.hrk_to_czk.setText(answear)
        
        except:
            error = "Number not entered!"

        if (error):
            self.num.setText(str(round(answear, 3)))


class Ui_Window12(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 133)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 151, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.czk_to_hrk)
        self.num = QtWidgets.QLabel(self.centralwidget)
        self.num.setGeometry(QtCore.QRect(420, 30, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num.setFont(font)
        self.num.setObjectName("num")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 133))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Answear"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.num.setText(_translate("MainWindow", "0"))

    def czk_to_hrk(self):
        answear = ""
        error = ""
        try:
            d = int(self.textEdit.text())
            hrk = 3.42
            answear = d / hrk
            self.czk_to_hrk.setText(answear)
        
        except:
            error = "Number not entered!"

        if (error):
            self.num.setText(str(round(answear, 3)))

class Ui_Window13(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 133)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 151, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.mxn_to_czk)
        self.num = QtWidgets.QLabel(self.centralwidget)
        self.num.setGeometry(QtCore.QRect(420, 30, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num.setFont(font)
        self.num.setObjectName("num")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 133))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Answear"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.num.setText(_translate("MainWindow", "0"))

    def mxn_to_czk(self):
        answear = ""
        error = ""
        try:
            d = int(self.textEdit.text())
            mxn = 1.2
            answear = d * mxn
            self.mxn_to_czk.setText(answear)
        
        except:
            error = "Number not entered!"

        if (error):
            self.num.setText(str(round(answear, 3)))


class Ui_Window14(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 133)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 151, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.czk_to_mxn)
        self.num = QtWidgets.QLabel(self.centralwidget)
        self.num.setGeometry(QtCore.QRect(420, 30, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num.setFont(font)
        self.num.setObjectName("num")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 133))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Answear"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.num.setText(_translate("MainWindow", "0"))

    def czk_to_mxn(self):
        answear = ""
        error = ""
        try:
            d = int(self.textEdit.text())
            mxn = 1.2
            answear = d / mxn
            self.mxn_to_czk.setText(answear)
        
        except:
            error = "Number not entered!"

        if (error):
            self.num.setText(str(round(answear, 3)))

class Ui_Window15(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 133)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 151, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pln_to_czk)
        self.num = QtWidgets.QLabel(self.centralwidget)
        self.num.setGeometry(QtCore.QRect(420, 30, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num.setFont(font)
        self.num.setObjectName("num")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 133))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Answear"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.num.setText(_translate("MainWindow", "0"))

    def pln_to_czk(self):
        answear = ""
        error = ""
        try:
            d = int(self.textEdit.text())
            pln = 5.9
            answear = d * pln
            self.pln_to_czk.setText(answear)
        
        except:
            error = "Number not entered!"

        if (error):
            self.num.setText(str(round(answear, 3)))

class Ui_Window16(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 133)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 151, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.czk_to_pln)
        self.num = QtWidgets.QLabel(self.centralwidget)
        self.num.setGeometry(QtCore.QRect(420, 30, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num.setFont(font)
        self.num.setObjectName("num")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 133))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Answear"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.num.setText(_translate("MainWindow", "0"))

    def czk_to_pln(self):
        answear = ""
        error = ""
        try:
            d = int(self.textEdit.text())
            pln = 5.9
            answear = d / pln
            self.czk_to_pln.setText(answear)
        
        except:
            error = "Number not entered!"

        if (error):
            self.num.setText(str(round(answear, 3)))

class Ui_Window17(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 133)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 151, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.ils_to_czk)
        self.num = QtWidgets.QLabel(self.centralwidget)
        self.num.setGeometry(QtCore.QRect(420, 30, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num.setFont(font)
        self.num.setObjectName("num")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 133))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Answear"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.num.setText(_translate("MainWindow", "0"))

    def ils_to_czk(self):
        answear = ""
        error = ""
        try:
            d = int(self.textEdit.text())
            ils = 6.5
            answear = d * ils
            self.ils_to_czk.setText(answear)
        
        except:
            error = "Number not entered!"

        if (error):
            self.num.setText(str(round(answear, 3)))

class Ui_Window18(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 133)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 151, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.czk_to_ils)
        self.num = QtWidgets.QLabel(self.centralwidget)
        self.num.setGeometry(QtCore.QRect(420, 30, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num.setFont(font)
        self.num.setObjectName("num")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 133))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Answear"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.num.setText(_translate("MainWindow", "0"))

    def czk_to_ils(self):
        answear = ""
        error = ""
        try:
            d = int(self.textEdit.text())
            ils = 6.5
            answear = d / ils
            self.ils_to_czk.setText(answear)
        
        except:
            error = "Number not entered!"

        if (error):
            self.num.setText(str(round(answear, 3)))


class Ui_MainWindow(object):    
    def setupUi(self, MainWindow, Ui_Window):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(623, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.czktousd = QtWidgets.QPushButton(self.centralwidget)
        self.czktousd.setGeometry(QtCore.QRect(10, 210, 191, 61))
        self.czktousd.clicked.connect(self.czk_to_usd)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.czktousd.setFont(font)
        self.czktousd.setObjectName("czktousd")
        self.usdtoczk = QtWidgets.QPushButton(self.centralwidget)
        self.usdtoczk.setGeometry(QtCore.QRect(10, 140, 191, 61))
        self.usdtoczk.clicked.connect(self.usd_to_czk)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.usdtoczk.setFont(font)
        self.usdtoczk.setObjectName("usdtoczk")
        self.eurtoczk = QtWidgets.QPushButton(self.centralwidget)
        self.eurtoczk.setGeometry(QtCore.QRect(10, 280, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.eurtoczk.setFont(font)
        self.eurtoczk.setObjectName("eurtoczk")
        self.eurtoczk.clicked.connect(self.eur_to_czk)
        self.czktoeur = QtWidgets.QPushButton(self.centralwidget)
        self.czktoeur.setGeometry(QtCore.QRect(10, 350, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.czktoeur.setFont(font)
        self.czktoeur.setObjectName("czktoeur")
        self.czktoeur.clicked.connect(self.czk_to_eur)
        self.rubtoczk = QtWidgets.QPushButton(self.centralwidget)
        self.rubtoczk.setGeometry(QtCore.QRect(10, 420, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.rubtoczk.setFont(font)
        self.rubtoczk.setObjectName("rubtoczk")
        self.rubtoczk.clicked.connect(self.rub_to_czk)
        self.czktorub = QtWidgets.QPushButton(self.centralwidget)
        self.czktorub.setGeometry(QtCore.QRect(10, 490, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.czktorub.setFont(font)
        self.czktorub.setObjectName("czktorub")
        self.czktorub.clicked.connect(self.czk_to_rub)
        self.audtoczk = QtWidgets.QPushButton(self.centralwidget)
        self.audtoczk.setGeometry(QtCore.QRect(210, 140, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.audtoczk.setFont(font)
        self.audtoczk.setObjectName("audtoczk")
        self.audtoczk.clicked.connect(self.aud_to_czk)
        self.czktoaud = QtWidgets.QPushButton(self.centralwidget)
        self.czktoaud.setGeometry(QtCore.QRect(210, 210, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.czktoaud.setFont(font)
        self.czktoaud.setObjectName("czktoaud")
        self.czktoaud.clicked.connect(self.czk_to_aud)
        self.gbptoczk = QtWidgets.QPushButton(self.centralwidget)
        self.gbptoczk.setGeometry(QtCore.QRect(210, 280, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.gbptoczk.setFont(font)
        self.gbptoczk.setObjectName("gbptoczk")
        self.gbptoczk.clicked.connect(self.gbp_to_czk)
        self.czktogbp = QtWidgets.QPushButton(self.centralwidget)
        self.czktogbp.setGeometry(QtCore.QRect(210, 350, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.czktogbp.setFont(font)
        self.czktogbp.setObjectName("czktogbp")
        self.czktogbp.clicked.connect(self.czk_to_gbp)
        self.hrktoczk = QtWidgets.QPushButton(self.centralwidget)
        self.hrktoczk.setGeometry(QtCore.QRect(210, 420, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.hrktoczk.setFont(font)
        self.hrktoczk.setObjectName("hrktoczk")
        self.hrktoczk.clicked.connect(self.hrk_to_czk)
        self.czktohrk = QtWidgets.QPushButton(self.centralwidget)
        self.czktohrk.setGeometry(QtCore.QRect(210, 490, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.czktohrk.setFont(font)
        self.czktohrk.setObjectName("czktohrk")
        self.czktohrk.clicked.connect(self.czk_to_hrk)
        self.mxntoczk = QtWidgets.QPushButton(self.centralwidget)
        self.mxntoczk.setGeometry(QtCore.QRect(410, 140, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.mxntoczk.setFont(font)
        self.mxntoczk.setObjectName("mxntoczk")
        self.mxntoczk.clicked.connect(self.mxn_to_czk)
        self.czktomxn = QtWidgets.QPushButton(self.centralwidget)
        self.czktomxn.setGeometry(QtCore.QRect(410, 210, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.czktomxn.setFont(font)
        self.czktomxn.setObjectName("czktomxn")
        self.czktomxn.clicked.connect(self.czk_to_mxn)
        self.plntoczk = QtWidgets.QPushButton(self.centralwidget)
        self.plntoczk.setGeometry(QtCore.QRect(410, 280, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.plntoczk.setFont(font)
        self.plntoczk.setObjectName("plntoczk")
        self.plntoczk.clicked.connect(self.pln_to_czk)
        self.czktopln = QtWidgets.QPushButton(self.centralwidget)
        self.czktopln.setGeometry(QtCore.QRect(410, 350, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.czktopln.setFont(font)
        self.czktopln.setObjectName("czktopln")
        self.czktopln.clicked.connect(self.czk_to_pln)
        self.ilstoczk = QtWidgets.QPushButton(self.centralwidget)
        self.ilstoczk.setGeometry(QtCore.QRect(410, 420, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.ilstoczk.setFont(font)
        self.ilstoczk.setObjectName("ilstoczk")
        self.ilstoczk.clicked.connect(self.ils_to_czk)
        self.czktoils = QtWidgets.QPushButton(self.centralwidget)
        self.czktoils.setGeometry(QtCore.QRect(410, 490, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.czktoils.setFont(font)
        self.czktoils.setObjectName("czktoils")
        self.czktoils.clicked.connect(self.czk_to_ils)
        self.xobraz = QtWidgets.QLabel(self.centralwidget)
        self.xobraz.setGeometry(QtCore.QRect(270, 10, 141, 111))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.xobraz.setFont(font)
        self.xobraz.setObjectName("xobraz")
        MainWindow.setCentralWidget(self.centralwidget)
        self.applikace = QtWidgets.QMenuBar(MainWindow)
        self.applikace.setGeometry(QtCore.QRect(0, 0, 623, 21))
        self.applikace.setObjectName("applikace")
        MainWindow.setMenuBar(self.applikace)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Price Calculator"))
        self.czktousd.setText(_translate("MainWindow", "CZK to USD"))
        self.usdtoczk.setText(_translate("MainWindow", "USD to CZK"))
        self.eurtoczk.setText(_translate("MainWindow", "EUR to CZK"))
        self.czktoeur.setText(_translate("MainWindow", "CZK to EUR"))
        self.rubtoczk.setText(_translate("MainWindow", "RUB to CZK"))
        self.czktorub.setText(_translate("MainWindow", "CZK to RUB"))
        self.audtoczk.setText(_translate("MainWindow", "AUD to CZK"))
        self.czktoaud.setText(_translate("MainWindow", "CZK to AUD"))
        self.gbptoczk.setText(_translate("MainWindow", "GBP to CZK"))
        self.czktogbp.setText(_translate("MainWindow", "CZK to GBP"))
        self.hrktoczk.setText(_translate("MainWindow", "HRK to CZK"))
        self.czktohrk.setText(_translate("MainWindow", "CZK to HRK"))
        self.mxntoczk.setText(_translate("MainWindow", "MXN to CZK"))
        self.czktomxn.setText(_translate("MainWindow", "CZK to MXN"))
        self.plntoczk.setText(_translate("MainWindow", "PLN to CZK"))
        self.czktopln.setText(_translate("MainWindow", "CZK to PLN"))
        self.ilstoczk.setText(_translate("MainWindow", "ILS to CZK"))
        self.czktoils.setText(_translate("MainWindow", "CZK to ILS"))
        self.xobraz.setText(_translate("MainWindow", "$"))

    def usd_to_czk(self, setupUi):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Window()
        self.ui.setupUi(self.window)
        self.window.show()

    def czk_to_usd(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_Window2()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def eur_to_czk(self):
        self.window3 = QtWidgets.QMainWindow()
        self.ui = Ui_Window3()
        self.ui.setupUi(self.window3)
        self.window3.show()
    
    def czk_to_eur(self):
        self.window4 = QtWidgets.QMainWindow()
        self.ui = Ui_Window4()
        self.ui.setupUi(self.window4)
        self.window4.show()

    def rub_to_czk(self):
        self.window5 = QtWidgets.QMainWindow()
        self.ui = Ui_Window5()
        self.ui.setupUi(self.window5)
        self.window5.show()

    def czk_to_rub(self):
        self.window6 = QtWidgets.QMainWindow()
        self.ui = Ui_Window6()
        self.ui.setupUi(self.window6)
        self.window6.show()

    def aud_to_czk(self):
        self.window7 = QtWidgets.QMainWindow()
        self.ui = Ui_Window7()
        self.ui.setupUi(self.window7)
        self.window7.show()

    def czk_to_aud(self):
        self.window8 = QtWidgets.QMainWindow()
        self.ui = Ui_Window8()
        self.ui.setupUi(self.window8)
        self.window8.show()

    def gbp_to_czk(self):
        self.window9 = QtWidgets.QMainWindow()
        self.ui = Ui_Window9()
        self.ui.setupUi(self.window9)
        self.window9.show()

    def czk_to_gbp(self):
        self.window10 = QtWidgets.QMainWindow()
        self.ui = Ui_Window10()
        self.ui.setupUi(self.window10)
        self.window10.show()
    
    def hrk_to_czk(self):
        self.window11 = QtWidgets.QMainWindow()
        self.ui = Ui_Window11()
        self.ui.setupUi(self.window11)
        self.window11.show()

    def czk_to_hrk(self):
        self.window12 = QtWidgets.QMainWindow()
        self.ui = Ui_Window12()
        self.ui.setupUi(self.window12)
        self.window12.show()

    def mxn_to_czk(self):
        self.window13 = QtWidgets.QMainWindow()
        self.ui = Ui_Window13()
        self.ui.setupUi(self.window13)
        self.window13.show()

    def czk_to_mxn(self):
        self.window14 = QtWidgets.QMainWindow()
        self.ui = Ui_Window14()
        self.ui.setupUi(self.window14)
        self.window14.show()

    def pln_to_czk(self):
        self.window15 = QtWidgets.QMainWindow()
        self.ui = Ui_Window15()
        self.ui.setupUi(self.window15)
        self.window15.show()

    def czk_to_pln(self):
        self.window16 = QtWidgets.QMainWindow()
        self.ui = Ui_Window16()
        self.ui.setupUi(self.window16)
        self.window16.show()

    def ils_to_czk(self):
        self.window17 = QtWidgets.QMainWindow()
        self.ui = Ui_Window17()
        self.ui.setupUi(self.window17)
        self.window17.show()

    def czk_to_ils(self):
        self.window18 = QtWidgets.QMainWindow()
        self.ui = Ui_Window18()
        self.ui.setupUi(self.window18)
        self.window18.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, Ui_Window)
    MainWindow.show()
    sys.exit(app.exec_())
