# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unsavedchanges_confirmationdialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_confirmationDialog(object):
    def setupUi(self, confirmationDialog):
        confirmationDialog.setObjectName("confirmationDialog")
        confirmationDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        confirmationDialog.resize(385, 98)
        confirmationDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(confirmationDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(confirmationDialog)
        self.label.setMaximumSize(QtCore.QSize(32, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/attention.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(confirmationDialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(confirmationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(confirmationDialog)
        self.buttonBox.accepted.connect(confirmationDialog.accept)
        self.buttonBox.rejected.connect(confirmationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(confirmationDialog)

    def retranslateUi(self, confirmationDialog):
        _translate = QtCore.QCoreApplication.translate
        confirmationDialog.setWindowTitle(_translate("confirmationDialog", "Delete Item"))
        self.label_2.setText(_translate("confirmationDialog", "You have unsaved changes, these will be lost! Are you sure you want to continue?"))

import resources_rc
