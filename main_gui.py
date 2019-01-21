import sys
import mysql.connector
from todo_db import task
from PyQt5 import QtWidgets, QtGui
from mydesign import Ui_MainWindow # this imports the python file we generated from the .uic file


class main_window(QtWidgets.QMainWindow):

    def __init__(self):
        super(QtWidgets.QMainWindow, self).__init__()  # read on how to use super and use it well here to initialize only the QtWidgets.QMainWindow class
        self.setWindowIcon(QtGui.QIcon("todo_icon.ico")) # this sets the icon of the user interface
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.save_PushButton.setStyleSheet("background-color: rgb(0,128,0); color: white;")
        self.ui.delete_PushButton.setStyleSheet("background-color: rgb(255,0,0); color: white;")
        self.edit_PushButton_default()
        # self.groups_comboBox_default()
        self.enable_or_disable_save_PushButton()
        """ this disables the save button until the user clicks to type a new task 
            and disables the save button anytime the text input is blank"""
        self.ui.new_task_TextEdit.textChanged.connect(self.enable_or_disable_save_PushButton)
        self.ui.edit_PushButton.clicked.connect(self.change_editButton_text)
        self.ui.save_PushButton.clicked.connect(self.add_task_to_db)

    # this function makes the edit button blue by default
    def edit_PushButton_default(self):
        self.ui.edit_PushButton.setText("Edit")
        self.ui.edit_PushButton.setStyleSheet("background-color: #0066CC; color: white;")

    def change_editButton_text(self):
        if self.ui.edit_PushButton.text() == "Edit":
            self.ui.edit_PushButton.setText("Update")
            self.ui.edit_PushButton.setStyleSheet("background-color: rgb(255,69,0); color: white;")   
        else:
            self.edit_PushButton_default()

    """ this function checks whether the textEdit for new tasks is empty
        returns true if empty and false otherwise."""

    def isEmpty_new_task_TextEdit(self):
        self.content = self.ui.new_task_TextEdit.toPlainText()
        if self.content == "":
            return True
        else:
            return False

    def enable_or_disable_save_PushButton(self):
        if self.isEmpty_new_task_TextEdit():
            self.ui.save_PushButton.setEnabled(False)
        else:
            self.ui.save_PushButton.setEnabled(True)


    def add_task_to_db(self):
        self.start_date = self.ui.start_dateEdit.date().toPyDate()
        self.start_time = self.ui.start_timeEdit.time().toPyTime()
        self.end_date = self.ui.end_dateEdit.date().toPyDate()
        self.end_time = self.ui.end_timeEdit.time().toPyTime()
        self.task_description = self.ui.new_task_TextEdit.toPlainText()
        self.group = str(self.ui.groups_comboBox.currentText())
        #inserts a new task into the task database
        self.new_task = task(self.start_date, self.start_time, self.end_date, self.end_time, self.task_description, self.group) 
        # clears the text input after the user clicks the save button
        self.ui.new_task_TextEdit.clear()
        self.ui.allTasks_listWidget.addItem(self.task_description)
        # self.ls = ["one", "two", "three"]
        # self.ui.allTasks_listWidget.addItems(self.ls)
        # self.ui.gridLayout.addWidget(self.ui.allTasks_listWidget, 1, 0, 1, 2)
        # self.gridLayout.addWidget(self.listwidget, 1, 0, 1, 2)


            
app = QtWidgets.QApplication([])
application = main_window()
application.show()
sys.exit(app.exec())