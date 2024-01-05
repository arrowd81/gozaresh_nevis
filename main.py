# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from code_pop_ups.add_project_pop_up import UI_add_project
from code_pop_ups.date_pop_up import UI_add_date
from code_pop_ups.delete_pop_up import UI_delete
from code_pop_ups.error_pop_up import UI_error
from code_pop_ups.new_project_pop_up import Ui_new_project


class Ui_MainWindow(object):
    def setupUi(self, MainWindow:QtWidgets.QMainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(702, 451)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.weekly_explorer = QtWidgets.QTreeWidget(self.centralwidget)
        self.weekly_explorer.setEnabled(True)
        self.weekly_explorer.setGeometry(QtCore.QRect(0, 0, 471, 421))
        self.weekly_explorer.setObjectName("weekly_explorer")
        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setGeometry(QtCore.QRect(500, 250, 181, 51))
        self.loadButton.setObjectName("loadButton")
        self.addProjectButton = QtWidgets.QPushButton(self.centralwidget)
        self.addProjectButton.setGeometry(QtCore.QRect(500, 130, 181, 51))
        self.addProjectButton.setObjectName("addProjectButton")
        self.addProjectButton.clicked.connect(self.show_add_project_dialog)
        self.newDateButton = QtWidgets.QPushButton(self.centralwidget)
        self.newDateButton.setGeometry(QtCore.QRect(500, 10, 181, 51))
        self.newDateButton.setObjectName("newDateButton")
        self.newDateButton.clicked.connect(self.show_add_date_dialog)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(500, 310, 181, 51))
        self.saveButton.setObjectName("saveButton")
        self.removeItemButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeItemButton.setGeometry(QtCore.QRect(500, 190, 181, 51))
        self.removeItemButton.setObjectName("removeItemButton")
        self.removeItemButton.clicked.connect(self.show_delete_dialog)
        self.getOutputButton = QtWidgets.QPushButton(self.centralwidget)
        self.getOutputButton.setGeometry(QtCore.QRect(500, 370, 181, 51))
        self.getOutputButton.setObjectName("getOutputButton")
        self.newProjectButton = QtWidgets.QPushButton(self.centralwidget)
        self.newProjectButton.setGeometry(QtCore.QRect(500, 70, 181, 51))
        self.newProjectButton.setObjectName("newProjectButton")
        self.newProjectButton.clicked.connect(self.show_new_project_dialog)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 702, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.projects_data = []

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow:QtWidgets.QMainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.weekly_explorer.headerItem().setText(0, _translate("MainWindow", "arash_data"))
        self.loadButton.setText(_translate("MainWindow", "Load"))
        self.addProjectButton.setText(_translate("MainWindow", "add project to date"))
        self.newDateButton.setText(_translate("MainWindow", "add new date"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.removeItemButton.setText(_translate("MainWindow", "remove item"))
        self.getOutputButton.setText(_translate("MainWindow", "get output"))
        self.newProjectButton.setText(_translate("MainWindow", "add new project"))

    def show_error_dialog(self, error_message:str):
        error_dialog = QtWidgets.QDialog()
        error_ui = UI_error()
        error_ui.setupUi(error_dialog)
        error_ui.label.setText(error_message)
        error_dialog.exec_()

    def show_new_project_dialog(self):
        new_project_dialog = QtWidgets.QDialog()
        new_project_ui = Ui_new_project()
        new_project_ui.setupUi(new_project_dialog)
        new_project_ui.buttonBox.accepted.connect(lambda: self.create_new_project(new_project_ui.lineEdit.text()))
        new_project_dialog.exec_()

    def show_add_project_dialog(self):
        if self.weekly_explorer.currentItem() is None:
            self.show_error_dialog('you must select a date to add this to')
        else:
            add_project_dialog = QtWidgets.QDialog()
            add_project_ui = UI_add_project()
            add_project_ui.setupUi(add_project_dialog)
            add_project_ui.buttonBox.accepted.connect(lambda: self.add_item(add_project_dialog,
                                                                            add_project_ui.comboBox.currentText(),
                                                                            add_project_ui.textEdit.toPlainText(),
                                                                            self.weekly_explorer.currentItem()))
            for project in self.projects_data:
                add_project_ui.comboBox.addItem(project)
            add_project_dialog.exec_()

    def show_add_date_dialog(self):
        add_date_dialog = QtWidgets.QDialog()
        add_date_ui = UI_add_date()
        add_date_ui.setupUi(add_date_dialog)
        add_date_ui.buttonBox.accepted.connect(lambda: self.add_date(add_date_dialog,
                                                                     add_date_ui.dateEdit.dateTime().date(),
                                                                     add_date_ui.lineEdit.text()))
        add_date_dialog.exec_()

    def show_delete_dialog(self):
        if self.weekly_explorer.currentItem() is None:
            self.show_error_dialog('you must select something to delete!')
        else:
            show_delete_dialog = QtWidgets.QDialog()
            delete_ui = UI_delete()
            delete_ui.setupUi(show_delete_dialog)
            delete_ui.label.setText('Are you sure you want to DELETE\n' + self.weekly_explorer.currentItem().text(0))
            delete_ui.buttonBox.accepted.connect(self.delete_tree)
            show_delete_dialog.exec_()

    def create_new_project(self, project_name:str):
        self.projects_data.append(project_name)

    def delete_tree(self):
        selected_item = self.weekly_explorer.currentItem()
        parent = selected_item.parent()
        if parent is None:
            # Top-level item
            index = self.weekly_explorer.indexOfTopLevelItem(selected_item)
            self.weekly_explorer.takeTopLevelItem(index)
        else:
            # Child item
            parent.removeChild(selected_item)

    def add_date(self, dialog:QtWidgets.QDialog, gregorian_date:QtCore.QDate, Persian_date:str):
        item = QtWidgets.QTreeWidgetItem(self.weekly_explorer)
        item.setText(0, Persian_date + ' -> ' + gregorian_date.toString("yyyy-MM-dd"))
        dialog.accept()

    def add_item(self, dialog:QtWidgets.QDialog, project_name, discription, parent:QtWidgets.QTreeWidgetItem):
        if parent.parent() is None:
            item = QtWidgets.QTreeWidgetItem(parent)
        else:
            self.show_error_dialog('you must select a date to add this to')
        item.setText(0, project_name)
        item1 = QtWidgets.QTreeWidgetItem(item)
        item1.setText(0, discription)
        dialog.accept()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
