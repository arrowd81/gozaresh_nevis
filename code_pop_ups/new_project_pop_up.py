# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_project_pop_up.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_new_project(object):
    def setupUi(self, new_project_dialog):
        new_project_dialog.setObjectName("new_project_dialog")
        new_project_dialog.resize(284, 109)
        self.buttonBox = QtWidgets.QDialogButtonBox(new_project_dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 70, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(new_project_dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 221, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(new_project_dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 40, 221, 25))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(new_project_dialog)
        self.buttonBox.accepted.connect(new_project_dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(new_project_dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(new_project_dialog)

    def retranslateUi(self, new_project_dialog):
        _translate = QtCore.QCoreApplication.translate
        new_project_dialog.setWindowTitle(_translate("new_project_dialog", "new project"))
        self.label.setText(_translate("new_project_dialog", "enter project name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    new_project_dialog = QtWidgets.QDialog()
    ui = Ui_new_project()
    ui.setupUi(new_project_dialog)
    new_project_dialog.show()
    sys.exit(app.exec_())
