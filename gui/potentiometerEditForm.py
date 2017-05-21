# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'potentiometerEditForm.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_potentiometerEditForm(object):
    def setupUi(self, potentiometerEditForm):
        potentiometerEditForm.setObjectName("potentiometerEditForm")
        potentiometerEditForm.resize(832, 674)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(potentiometerEditForm.sizePolicy().hasHeightForWidth())
        potentiometerEditForm.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(potentiometerEditForm)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(potentiometerEditForm)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.ADDDREF_BTN = QtWidgets.QToolButton(potentiometerEditForm)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/plusIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ADDDREF_BTN.setIcon(icon)
        self.ADDDREF_BTN.setAutoRaise(True)
        self.ADDDREF_BTN.setObjectName("ADDDREF_BTN")
        self.horizontalLayout_4.addWidget(self.ADDDREF_BTN)
        self.RMDREF_BTN = QtWidgets.QToolButton(potentiometerEditForm)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/minusIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RMDREF_BTN.setIcon(icon1)
        self.RMDREF_BTN.setAutoRaise(True)
        self.RMDREF_BTN.setObjectName("RMDREF_BTN")
        self.horizontalLayout_4.addWidget(self.RMDREF_BTN)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 2, 4, 1, 1)
        self.DREFS_TABLE = QtWidgets.QTableWidget(potentiometerEditForm)
        self.DREFS_TABLE.setObjectName("DREFS_TABLE")
        self.DREFS_TABLE.setColumnCount(5)
        self.DREFS_TABLE.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.DREFS_TABLE.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.DREFS_TABLE.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.DREFS_TABLE.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.DREFS_TABLE.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.DREFS_TABLE.setHorizontalHeaderItem(4, item)
        self.gridLayout_3.addWidget(self.DREFS_TABLE, 3, 1, 1, 1)
        self.drefsHelpText = QtWidgets.QLabel(potentiometerEditForm)
        self.drefsHelpText.setMinimumSize(QtCore.QSize(250, 0))
        self.drefsHelpText.setMaximumSize(QtCore.QSize(300, 16777215))
        self.drefsHelpText.setTextFormat(QtCore.Qt.RichText)
        self.drefsHelpText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.drefsHelpText.setWordWrap(True)
        self.drefsHelpText.setObjectName("drefsHelpText")
        self.gridLayout_3.addWidget(self.drefsHelpText, 3, 3, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_3, 8, 0, 1, 6)
        self.nameLineEdit = QtWidgets.QLineEdit(potentiometerEditForm)
        self.nameLineEdit.setMinimumSize(QtCore.QSize(250, 0))
        self.nameLineEdit.setMaximumSize(QtCore.QSize(350, 16777215))
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.gridLayout.addWidget(self.nameLineEdit, 3, 2, 1, 3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.CMDS_TABLE = QtWidgets.QTableWidget(potentiometerEditForm)
        self.CMDS_TABLE.setToolTipDuration(3)
        self.CMDS_TABLE.setObjectName("CMDS_TABLE")
        self.CMDS_TABLE.setColumnCount(2)
        self.CMDS_TABLE.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.CMDS_TABLE.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.CMDS_TABLE.setHorizontalHeaderItem(1, item)
        self.gridLayout_4.addWidget(self.CMDS_TABLE, 6, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_12 = QtWidgets.QLabel(potentiometerEditForm)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.ADDCMD_BTN = QtWidgets.QToolButton(potentiometerEditForm)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/plusIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ADDCMD_BTN.setIcon(icon2)
        self.ADDCMD_BTN.setAutoRaise(True)
        self.ADDCMD_BTN.setObjectName("ADDCMD_BTN")
        self.horizontalLayout_6.addWidget(self.ADDCMD_BTN)
        self.RMCMD_BTN = QtWidgets.QToolButton(potentiometerEditForm)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/minusIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.RMCMD_BTN.setIcon(icon3)
        self.RMCMD_BTN.setAutoRaise(True)
        self.RMCMD_BTN.setObjectName("RMCMD_BTN")
        self.horizontalLayout_6.addWidget(self.RMCMD_BTN)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.gridLayout_4.addLayout(self.horizontalLayout_7, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(potentiometerEditForm)
        self.label.setMinimumSize(QtCore.QSize(250, 0))
        self.label.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 6, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 10, 0, 1, 6)
        self.IDlineEdit = QtWidgets.QLineEdit(potentiometerEditForm)
        self.IDlineEdit.setEnabled(False)
        self.IDlineEdit.setMinimumSize(QtCore.QSize(250, 0))
        self.IDlineEdit.setMaximumSize(QtCore.QSize(350, 16777215))
        self.IDlineEdit.setReadOnly(True)
        self.IDlineEdit.setObjectName("IDlineEdit")
        self.gridLayout.addWidget(self.IDlineEdit, 4, 2, 1, 3)
        self.PIN_comboBox = QtWidgets.QComboBox(potentiometerEditForm)
        self.PIN_comboBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.PIN_comboBox.setObjectName("PIN_comboBox")
        self.gridLayout.addWidget(self.PIN_comboBox, 5, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(potentiometerEditForm)
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
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 6)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 6, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(potentiometerEditForm)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(potentiometerEditForm)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 9, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(potentiometerEditForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(potentiometerEditForm)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(potentiometerEditForm)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 5, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(potentiometerEditForm)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 4, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 12, 0, 1, 1)
        self.valueSlider = QtWidgets.QSlider(potentiometerEditForm)
        self.valueSlider.setEnabled(False)
        self.valueSlider.setMaximumSize(QtCore.QSize(200, 16777215))
        self.valueSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 5px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal{\n"
"    border: 1px solid #999999;\n"
"    height: 8px;     \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #00979d, stop:1 #007579);\n"
"    margin: 2px 0;\n"
"}")
        self.valueSlider.setMaximum(1023)
        self.valueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.valueSlider.setInvertedAppearance(False)
        self.valueSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.valueSlider.setTickInterval(128)
        self.valueSlider.setObjectName("valueSlider")
        self.gridLayout.addWidget(self.valueSlider, 1, 4, 1, 1)
        self.valueLabel = QtWidgets.QLabel(potentiometerEditForm)
        self.valueLabel.setMinimumSize(QtCore.QSize(40, 0))
        self.valueLabel.setObjectName("valueLabel")
        self.gridLayout.addWidget(self.valueLabel, 1, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 5, 1, 1)

        self.retranslateUi(potentiometerEditForm)
        self.ADDDREF_BTN.clicked.connect(potentiometerEditForm.addDataref)
        self.RMDREF_BTN.clicked.connect(potentiometerEditForm.rmDataref)
        self.ADDCMD_BTN.clicked.connect(potentiometerEditForm.addCommand)
        self.RMCMD_BTN.clicked.connect(potentiometerEditForm.rmCommand)
        self.CMDS_TABLE.cellDoubleClicked['int','int'].connect(potentiometerEditForm.editXPCommand)
        self.nameLineEdit.editingFinished.connect(potentiometerEditForm.updateXMLdata)
        self.PIN_comboBox.currentIndexChanged['int'].connect(potentiometerEditForm.updateXMLdata)
        self.CMDS_TABLE.itemChanged['QTableWidgetItem*'].connect(potentiometerEditForm.updateXMLdata)
        self.PIN_comboBox.currentTextChanged['QString'].connect(potentiometerEditForm.updatePin)
        self.DREFS_TABLE.cellDoubleClicked['int','int'].connect(potentiometerEditForm.editXPDataref)
        self.DREFS_TABLE.itemChanged['QTableWidgetItem*'].connect(potentiometerEditForm.updateXMLdata)
        QtCore.QMetaObject.connectSlotsByName(potentiometerEditForm)

    def retranslateUi(self, potentiometerEditForm):
        _translate = QtCore.QCoreApplication.translate
        potentiometerEditForm.setWindowTitle(_translate("potentiometerEditForm", "Form"))
        self.label_11.setText(_translate("potentiometerEditForm", "Set Dataref: "))
        self.ADDDREF_BTN.setText(_translate("potentiometerEditForm", "..."))
        self.RMDREF_BTN.setText(_translate("potentiometerEditForm", "..."))
        item = self.DREFS_TABLE.horizontalHeaderItem(0)
        item.setText(_translate("potentiometerEditForm", "Dataref"))
        item = self.DREFS_TABLE.horizontalHeaderItem(1)
        item.setText(_translate("potentiometerEditForm", "Index"))
        item = self.DREFS_TABLE.horizontalHeaderItem(2)
        item.setText(_translate("potentiometerEditForm", "Set to Value"))
        item = self.DREFS_TABLE.horizontalHeaderItem(3)
        item.setText(_translate("potentiometerEditForm", "Type"))
        item = self.DREFS_TABLE.horizontalHeaderItem(4)
        item.setText(_translate("potentiometerEditForm", "Unit"))
        self.drefsHelpText.setText(_translate("potentiometerEditForm", "<html><head/><body><p>Enter series of points [pot input value, output dataref value]. The output value of the dataref in between 2 points will be linearly interpolated. </p><p>Note that the potentiometer value varies between 0 and 1023 (this is the raw output reading from the ADC of the arduino)</p><p>For example to set the dataref to vary linearly between 10 and 300 when the potentiometer value varies between 0 and 1023, enter: </p><p><span style=\" color:#0000ff;\">[0,10], [1023,300]</span></p></body></html>"))
        self.CMDS_TABLE.setToolTip(_translate("potentiometerEditForm", "<html><head/><body><p>Enter intervals where the command should be sent. </p><p>For example to send the command if the pot value is between 0 and 200 or between 600 and 800, enter: </p><p><span style=\" color:#0000ff;\">(0,200), (600,800)</span></p></body></html>"))
        item = self.CMDS_TABLE.horizontalHeaderItem(0)
        item.setText(_translate("potentiometerEditForm", "Command"))
        item = self.CMDS_TABLE.horizontalHeaderItem(1)
        item.setText(_translate("potentiometerEditForm", "Send if pot value is in intervals"))
        item.setToolTip(_translate("potentiometerEditForm", "<html><head/><body><p>Enter intervals where the command should be sent. </p><p>For example to send the command if the pot value is between 0 and 200 or between 600 and 800, enter: </p><p><span style=\" color:#0000ff;\">(0,200), (600,800)</span></p></body></html>"))
        self.label_12.setText(_translate("potentiometerEditForm", "Send XPlane Command: "))
        self.ADDCMD_BTN.setText(_translate("potentiometerEditForm", "..."))
        self.RMCMD_BTN.setText(_translate("potentiometerEditForm", "..."))
        self.label.setText(_translate("potentiometerEditForm", "<html><head/><body><p>Enter intervals where the command should be sent. </p><p>For example to send the command if the pot value is between 0 and 200 or between 600 and 800, enter: </p><p><span style=\" color:#0000ff;\">[0,200], [600,800]</span></p></body></html>"))
        self.label_8.setText(_translate("potentiometerEditForm", "Edit potentiometer"))
        self.label_17.setText(_translate("potentiometerEditForm", "Value"))
        self.label_15.setText(_translate("potentiometerEditForm", "Command actions:"))
        self.label_3.setText(_translate("potentiometerEditForm", "Name"))
        self.label_9.setText(_translate("potentiometerEditForm", "Dataref Actions:"))
        self.label_18.setText(_translate("potentiometerEditForm", "Arduino pin:"))
        self.label_19.setText(_translate("potentiometerEditForm", "ID"))
        self.valueLabel.setText(_translate("potentiometerEditForm", "0"))

import resources_rc
