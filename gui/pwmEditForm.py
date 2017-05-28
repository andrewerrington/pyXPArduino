# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pwmEditForm.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_pwmEditForm(object):
    def setupUi(self, pwmEditForm):
        pwmEditForm.setObjectName("pwmEditForm")
        pwmEditForm.resize(832, 674)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(pwmEditForm.sizePolicy().hasHeightForWidth())
        pwmEditForm.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(pwmEditForm)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.PWMoutValueLabel = QtWidgets.QLabel(pwmEditForm)
        self.PWMoutValueLabel.setObjectName("PWMoutValueLabel")
        self.gridLayout.addWidget(self.PWMoutValueLabel, 11, 6, 1, 1)
        self.drefInfoLabel = QtWidgets.QLabel(pwmEditForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drefInfoLabel.sizePolicy().hasHeightForWidth())
        self.drefInfoLabel.setSizePolicy(sizePolicy)
        self.drefInfoLabel.setMaximumSize(QtCore.QSize(350, 16777215))
        self.drefInfoLabel.setText("")
        self.drefInfoLabel.setWordWrap(True)
        self.drefInfoLabel.setObjectName("drefInfoLabel")
        self.gridLayout.addWidget(self.drefInfoLabel, 7, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 7, 7, 1, 1)
        self.label_7 = QtWidgets.QLabel(pwmEditForm)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 11, 5, 1, 1)
        self.drefLineEdit = QtWidgets.QLineEdit(pwmEditForm)
        self.drefLineEdit.setMinimumSize(QtCore.QSize(400, 0))
        self.drefLineEdit.setMaximumSize(QtCore.QSize(350, 16777215))
        self.drefLineEdit.setObjectName("drefLineEdit")
        self.gridLayout.addWidget(self.drefLineEdit, 6, 2, 1, 2)
        self.label_4 = QtWidgets.QLabel(pwmEditForm)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 11, 0, 1, 1)
        self.drefsHelpText = QtWidgets.QLabel(pwmEditForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drefsHelpText.sizePolicy().hasHeightForWidth())
        self.drefsHelpText.setSizePolicy(sizePolicy)
        self.drefsHelpText.setMinimumSize(QtCore.QSize(350, 0))
        self.drefsHelpText.setMaximumSize(QtCore.QSize(300, 16777215))
        self.drefsHelpText.setTextFormat(QtCore.Qt.RichText)
        self.drefsHelpText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.drefsHelpText.setWordWrap(True)
        self.drefsHelpText.setObjectName("drefsHelpText")
        self.gridLayout.addWidget(self.drefsHelpText, 12, 2, 2, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 14, 2, 1, 1)
        self.drefIndexLineEdit = QtWidgets.QLineEdit(pwmEditForm)
        self.drefIndexLineEdit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.drefIndexLineEdit.setObjectName("drefIndexLineEdit")
        self.gridLayout.addWidget(self.drefIndexLineEdit, 10, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(pwmEditForm)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 3, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(pwmEditForm)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 4, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(pwmEditForm)
        self.pushButton.setMinimumSize(QtCore.QSize(25, 20))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 5, 1, 1)
        self.PIN_comboBox = QtWidgets.QComboBox(pwmEditForm)
        self.PIN_comboBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.PIN_comboBox.setObjectName("PIN_comboBox")
        self.gridLayout.addWidget(self.PIN_comboBox, 4, 2, 1, 1)
        self.IDlineEdit = QtWidgets.QLineEdit(pwmEditForm)
        self.IDlineEdit.setEnabled(False)
        self.IDlineEdit.setMinimumSize(QtCore.QSize(250, 0))
        self.IDlineEdit.setMaximumSize(QtCore.QSize(350, 16777215))
        self.IDlineEdit.setReadOnly(True)
        self.IDlineEdit.setObjectName("IDlineEdit")
        self.gridLayout.addWidget(self.IDlineEdit, 3, 2, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(pwmEditForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(pwmEditForm)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 5, 1, 1)
        self.drefValueLabel = QtWidgets.QLabel(pwmEditForm)
        self.drefValueLabel.setText("")
        self.drefValueLabel.setObjectName("drefValueLabel")
        self.gridLayout.addWidget(self.drefValueLabel, 7, 6, 1, 1)
        self.label_5 = QtWidgets.QLabel(pwmEditForm)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(pwmEditForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: white;\n"
"background: rgb(0, 151, 157);\n"
"padding: 3px\n"
"")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 8)
        self.label = QtWidgets.QLabel(pwmEditForm)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 10, 0, 1, 1)
        self.nameLineEdit = QtWidgets.QLineEdit(pwmEditForm)
        self.nameLineEdit.setMinimumSize(QtCore.QSize(250, 0))
        self.nameLineEdit.setMaximumSize(QtCore.QSize(350, 16777215))
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.gridLayout.addWidget(self.nameLineEdit, 2, 2, 1, 3)
        self.pwmOutputLineEdit = QtWidgets.QLineEdit(pwmEditForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pwmOutputLineEdit.sizePolicy().hasHeightForWidth())
        self.pwmOutputLineEdit.setSizePolicy(sizePolicy)
        self.pwmOutputLineEdit.setMinimumSize(QtCore.QSize(400, 0))
        self.pwmOutputLineEdit.setMaximumSize(QtCore.QSize(350, 16777215))
        self.pwmOutputLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.pwmOutputLineEdit.setObjectName("pwmOutputLineEdit")
        self.gridLayout.addWidget(self.pwmOutputLineEdit, 11, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(pwmEditForm)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)

        self.retranslateUi(pwmEditForm)
        self.nameLineEdit.editingFinished.connect(pwmEditForm.updateXMLdata)
        self.PIN_comboBox.currentIndexChanged['int'].connect(pwmEditForm.updateXMLdata)
        self.PIN_comboBox.currentTextChanged['QString'].connect(pwmEditForm.updatePin)
        self.pushButton.clicked.connect(pwmEditForm.editXPDataref)
        self.drefLineEdit.editingFinished.connect(pwmEditForm.updateXMLdata)
        self.pwmOutputLineEdit.editingFinished.connect(pwmEditForm.updateXMLdata)
        self.drefLineEdit.textChanged['QString'].connect(pwmEditForm.updateXMLdata)
        self.drefIndexLineEdit.editingFinished.connect(pwmEditForm.updateXMLdata)
        QtCore.QMetaObject.connectSlotsByName(pwmEditForm)

    def retranslateUi(self, pwmEditForm):
        _translate = QtCore.QCoreApplication.translate
        pwmEditForm.setWindowTitle(_translate("pwmEditForm", "Form"))
        self.PWMoutValueLabel.setText(_translate("pwmEditForm", "TextLabel"))
        self.label_7.setText(_translate("pwmEditForm", " PWM Output Value  "))
        self.label_4.setText(_translate("pwmEditForm", "PWM Output Values:  "))
        self.drefsHelpText.setText(_translate("pwmEditForm", "<html><head/><body><p>Enter series of points: [Dataref input value, output PWM value]. The output value of the PWM in between 2 points will be linearly interpolated. Note the PWM output values must be between 0 (off) and 255 (fully on)</p><p>For example to set the PWM output to vary linearly between 10 and 255 when the dataref value varies between 0 and 1.0, enter: </p><p><span style=\" color:#0000ff;\">[0,10], [1.0,300]</span></p></body></html>"))
        self.label_19.setText(_translate("pwmEditForm", "ID"))
        self.label_18.setText(_translate("pwmEditForm", "Arduino pin:"))
        self.pushButton.setText(_translate("pwmEditForm", "Pick ..."))
        self.label_3.setText(_translate("pwmEditForm", "Name"))
        self.label_6.setText(_translate("pwmEditForm", " Dataref Value  "))
        self.label_5.setText(_translate("pwmEditForm", "Dataref Info"))
        self.label_8.setText(_translate("pwmEditForm", "Edit PWM output"))
        self.label.setText(_translate("pwmEditForm", "Dataref index"))
        self.label_2.setText(_translate("pwmEditForm", "XPlane Dataref:"))

import resources_rc
