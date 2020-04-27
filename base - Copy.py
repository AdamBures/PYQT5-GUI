
from PyQt5 import QtCore, QtGui, QtWidgets


class Regis(object):
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
        self.reg_but.clicked.connect(self.check)
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(36, 270, 141, 21))
        self.label.setObjectName("info_text")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Register"))
        self.username1.setText(_translate("MainWindow", "Username:"))
        self.pass1.setText(_translate("MainWindow", "Password:"))
        self.reg_but.setText(_translate("MainWindow", "Register"))
        self.email1.setText(_translate("MainWindow", "Email:"))
        self.label.setText(_translate("MainWindow", " "))

    def check(self, MainWindow):
            username1 = self.usr_edit.toPlainText()
            pass1 = self.pass_edit.toPlainText()
            email1 = self.email_edit.toPlainText()
            with open("data.txt", "a+") as f:
                data = f.read()
                for email1 in "data.txt":
	                for username1 in "data.txt":
		                if((email1 in "data.txt") or (username1 in "data.txt")):
		                    self.label.setText("Account already satisfied")
		                else:
		                    f.write(username1+ "-" + pass1+ "-" + email1 +"\n")
		                   

                    


class Adm(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 347)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcome_admin = QtWidgets.QLabel(self.centralwidget)
        self.welcome_admin.setGeometry(QtCore.QRect(20, 20, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.welcome_admin.setFont(font)
        self.welcome_admin.setObjectName("welcome_admin")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 120, 501, 181))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Admin"))
        self.welcome_admin.setText(_translate("MainWindow", "Welcome admin: "))

    

class Usr(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(491, 310)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcome_user = QtWidgets.QLabel(self.centralwidget)
        self.welcome_user.setGeometry(QtCore.QRect(10, 20, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.welcome_user.setFont(font)
        self.welcome_user.setObjectName("welcome_user")
        self.reg_but = QtWidgets.QPushButton(self.centralwidget)
        self.reg_but.setGeometry(QtCore.QRect(160, 180, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.reg_but.setFont(font)
        self.reg_but.setObjectName("reg_but")
        self.reg_but.clicked.connect(QtWidgets.qApp.quit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 491, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "User"))
        self.welcome_user.setText(_translate("MainWindow", "Welcome user"))
        self.reg_but.setText(_translate("MainWindow", "Exit"))
    


class Base(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(285, 347)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username = QtWidgets.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(10, 30, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(10, 100, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.login_but = QtWidgets.QPushButton(self.centralwidget)
        self.login_but.setGeometry(QtCore.QRect(40, 210, 221, 51))
        self.login_but.clicked.connect(self.check)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.login_but.setFont(font)
        self.login_but.setObjectName("login_but")
        self.info_text = QtWidgets.QLabel(self.centralwidget)
        self.info_text.setGeometry(QtCore.QRect(36, 270, 141, 21))
        self.info_text.setObjectName("info_text")
        self.registe_but = QtWidgets.QPushButton(self.centralwidget)
        self.registe_but.setGeometry(QtCore.QRect(170, 270, 91, 21))
        self.registe_but.setObjectName("registe_but")
        self.registe_but.clicked.connect(self.reg)
        self.email = QtWidgets.QLabel(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(10, 150, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.email.setFont(font)
        self.email.setObjectName("email")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.username.setText(_translate("MainWindow", "Username:"))
        self.password.setText(_translate("MainWindow", "Password:"))
        self.login_but.setText(_translate("MainWindow", "Login"))
        self.info_text.setText(_translate("MainWindow", "Doesn\'t have account ?"))
        self.registe_but.setText(_translate("MainWindow", "Register"))
        self.email.setText(_translate("MainWindow", "Email:"))


    def usr(self, MainWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = Usr()
        self.ui.setupUi(self.window)
        self.window.show()

    def check(self, MainWindow):
        username1 = self.usr_edit.toPlainText()
        pass1 = self.pass_edit.toPlainText()
        email1 = self.email_edit.toPlainText()
        admin_user = "admin"
        admin_pass= "admin"
        admin_email = "admin"

        with open("data.txt", "r+") as f:
            f.read()
            for username1 in "data.txt":
            	for pass1 in "data.txt":
            		for email1 in "data.txt":
                        if ((username1 in "data.txt") and (pass1 in "data.txt") and (email1 in "data.txt")):
                            return self.window.show()
                            
		            	if ((username1 == admin_user) and (pass1 == admin_pass) and (email1 == admin_email)):
		            	    return admin()

		            	else:
		                    self.info_text("You don't have an account Please create one.")

        
    def reg(self):
        self.window1 = QtWidgets.QMainWindow()
        self.ui = Regis()
        self.ui.setupUi(self.window1)
        self.window1.show()

    def admin(self, MainWindow):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Adm()
        self.ui.setupUi(self.window2)
        self.window2.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Base()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

