import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from PyQt5.QtWidgets import QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QAction, qApp, QUndoStack, QFontDialog
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from datetime import datetime as dt

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "C:\PyQt"
scriptDir = os.path.dirname(os.path.realpath(__file__))




class Notepad(QWidget):

    def __init__(self):
        super().__init__()
        self.text = QTextEdit(self)
        self.clr_btn = QPushButton('Clear')
        self.sav_btn = QPushButton('Save')
        self.opn_btn = QPushButton('Open')

        self.init_ui()

    def init_ui(self):
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        h_layout.addWidget(self.clr_btn)
        h_layout.addWidget(self.sav_btn)
        h_layout.addWidget(self.opn_btn)

        v_layout.addWidget(self.text)
        v_layout.addLayout(h_layout)

        self.sav_btn.clicked.connect(self.save_text)
        self.clr_btn.clicked.connect(self.clear_text)
        self.opn_btn.clicked.connect(self.open_text)
        
        
        self.setLayout(v_layout)
        
        self.show()

    def save_text(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File',"/","Text Documents(.txt)", os.getenv('HOME'))
        with open(filename[0], 'w') as f:
            my_text = self.text.toPlainText()
            f.write(my_text)

    def open_text(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File',"Text Documents(.txt)", os.getenv('HOME'))
        with open(filename[0], 'r') as f:
            file_text = f.read()
            self.text.setText(file_text)

    def clear_text(self):
        self.text.clear()

    def del_text(self):
        self.text.remove()

    def paste_text(self):
        self.text.paste()

    def copy_text(self):
        self.text.copy()
    
    
    def fontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.text.setFont(font)
    
    def cut_text(self):
        self.text.cut()
    
    def time_text(self):
        a = dt.now()     
        print(a)

    
class Writer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.form_widget = Notepad()
        self.setCentralWidget(self.form_widget)

        self.init_ui()

    def init_ui(self):
        bar = self.menuBar()
        file = bar.addMenu('File')
        edit = bar.addMenu('Edit')
        style = bar.addMenu('Style')
        hell = bar.addMenu('Help')

        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+N')

        save_action = QAction('&Save', self)
        save_action.setShortcut('Ctrl+S')

        open_action = QAction('&Open', self)
        open_action.setShortcut('Ctrl+O')

        quit_action = QAction('&Quit', self)
        quit_action.setShortcut('Alt+F4')

        clear_action = QAction('&Clear', self)
        clear_action.setShortcut('Ctrl+L')

        #undo_action = QAction('&Undo', self)

        del_action = QAction('&Delete', self)
        del_action.setShortcut('del')

        pas_action = QAction('&Paste', self)
        pas_action.setShortcut('Ctrl+V')

        copy_action = QAction('&Copy', self)
        copy_action.setShortcut('Ctrl+C')

        font_action = QAction('&Font', self)
        font_action.setShortcut('Ctrl+F')
        
        cut_action = QAction('&Cut', self)
        cut_action.setShortcut('Ctrl+X')

        time_action = QAction('&Time', self)
        time_action.setShortcut('F5')

        file.addAction(new_action)
        file.addAction(save_action)
        file.addAction(open_action)
        file.addAction(quit_action)

        edit.addAction(clear_action)
        #edit.addAction(undo_action)
        edit.addAction(del_action)
        edit.addAction(pas_action)
        edit.addAction(copy_action)
        edit.addAction(cut_action)
        edit.addAction(time_action)

        style.addAction(font_action)

        quit_action.triggered.connect(self.quit_trigger)
        file.triggered.connect(self.respond)

        edit.triggered.connect(self.respond)

        style.triggered.connect(self.respond)
        

        self.show()

    def quit_trigger(self):
        qApp.quit()

    def respond(self, q):
        signal = q.text()

        if signal == 'New':
            self.form_widget.clear_text()
        elif signal == '&Open':
            self.form_widget.open_text()
        elif signal == '&Save':
            self.form_widget.save_text()
        
        elif signal == '&Clear':
            self.form_widget.clear_text()

        elif signal == '&Back':
            self.form_widget.back_text()

        elif signal == '&Undo':
            self.form_widget.undo_text()

        elif signal == '&Paste':
            self.form_widget.paste_text()

        elif signal == '&Copy':
            self.form_widget.copy_text()
        
        elif signal == '&Del':
            self.form_widget.del_text()

        elif signal == '&Font':
            self.form_widget.fontDialog()

        elif signal == '&Cut':
            self.form_widget.cut_text()

        elif signal == '&Time':
            self.form_widget.time_text()


app = QApplication(sys.argv)
app.setStyle("Fusion")
#app.setWindowTitle("Notepad")
writer = Writer()
sys.exit(app.exec_())
