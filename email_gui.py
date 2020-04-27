
from PyQt5 import QtCore, QtGui, QtWidgets
import smtplib


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(698, 619)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.your_email_entry = QtWidgets.QTextEdit(self.centralwidget)
        self.your_email_entry.setGeometry(QtCore.QRect(260, 40, 381, 31))
        self.your_email_entry.setObjectName("your_email_entry")
        self.your_email = QtWidgets.QLabel(self.centralwidget)
        self.your_email.setGeometry(QtCore.QRect(76, 42, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.your_email.setFont(font)
        self.your_email.setScaledContents(False)
        self.your_email.setObjectName("your_email")
        self.receiver_email_entry = QtWidgets.QTextEdit(self.centralwidget)
        self.receiver_email_entry.setGeometry(QtCore.QRect(260, 90, 381, 31))
        self.receiver_email_entry.setObjectName("receiver_email_entry")
        self.receiver_email = QtWidgets.QLabel(self.centralwidget)
        self.receiver_email.setGeometry(QtCore.QRect(30, 90, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.receiver_email.setFont(font)
        self.receiver_email.setScaledContents(False)
        self.receiver_email.setObjectName("receiver_email")
        self.content_entry = QtWidgets.QTextEdit(self.centralwidget)
        self.content_entry.setGeometry(QtCore.QRect(60, 170, 591, 341))
        self.content_entry.setObjectName("content_entry")
        self.content_label = QtWidgets.QLabel(self.centralwidget)
        self.content_label.setGeometry(QtCore.QRect(60, 150, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.content_label.setFont(font)
        self.content_label.setObjectName("content_label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 520, 521, 41))
        self.pushButton.clicked.connect(self.send_email)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 698, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Email sender"))
        self.your_email.setText(_translate("MainWindow", "Your email"))
        self.receiver_email.setText(_translate("MainWindow", "Email of receiver"))
        self.content_label.setText(_translate("MainWindow", "Content:"))
        self.pushButton.setText(_translate("MainWindow", "Send email"))

    def send_email(self):
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()

        self.server.login("sasi12345677@gmail.com", "jwyhxnizhyeuupbu")

        self.subject = "NEW MAIL"
        self.body = self.content_entry.toPlainText()

        self.msg = f"{self.subject}\n\n{self.body}"

        self.server.sendmail(
            "sasi12345677@gmail.com",
            self.receiver_email_entry(),
            self.msg
        )
        print("Email has been send")
        self.server.quit()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
