# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rotencoderEditForm.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_rotencoderEditForm(object):
    def setupUi(self, rotencoderEditForm):
        rotencoderEditForm.setObjectName("rotencoderEditForm")
        rotencoderEditForm.resize(832, 674)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(rotencoderEditForm.sizePolicy().hasHeightForWidth())
        rotencoderEditForm.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(rotencoderEditForm)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(rotencoderEditForm)
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
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 5)
        self.label_17 = QtWidgets.QLabel(rotencoderEditForm)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 8, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(rotencoderEditForm)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(rotencoderEditForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(rotencoderEditForm)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 11, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(rotencoderEditForm)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 5, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(rotencoderEditForm)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 9, 0, 1, 1)
        self.PINA_comboBox = QtWidgets.QComboBox(rotencoderEditForm)
        self.PINA_comboBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.PINA_comboBox.setObjectName("PINA_comboBox")
        self.gridLayout.addWidget(self.PINA_comboBox, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 14, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.UP_CMDS_TABLE = QtWidgets.QTableWidget(rotencoderEditForm)
        self.UP_CMDS_TABLE.setMinimumSize(QtCore.QSize(0, 75))
        self.UP_CMDS_TABLE.setObjectName("UP_CMDS_TABLE")
        self.UP_CMDS_TABLE.setColumnCount(2)
        self.UP_CMDS_TABLE.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.UP_CMDS_TABLE.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.UP_CMDS_TABLE.setHorizontalHeaderItem(1, item)
        self.gridLayout_3.addWidget(self.UP_CMDS_TABLE, 4, 1, 1, 1)
        self.UP_DREFS_TABLE = QtWidgets.QTableWidget(rotencoderEditForm)
        self.UP_DREFS_TABLE.setObjectName("UP_DREFS_TABLE")
        self.UP_DREFS_TABLE.setColumnCount(6)
        self.UP_DREFS_TABLE.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.UP_DREFS_TABLE.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.UP_DREFS_TABLE.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.UP_DREFS_TABLE.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.UP_DREFS_TABLE.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.UP_DREFS_TABLE.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.UP_DREFS_TABLE.setHorizontalHeaderItem(5, item)
        self.gridLayout_3.addWidget(self.UP_DREFS_TABLE, 4, 4, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_10 = QtWidgets.QLabel(rotencoderEditForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.UP_ADDCMD_BTN = QtWidgets.QToolButton(rotencoderEditForm)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/plusIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.UP_ADDCMD_BTN.setIcon(icon)
        self.UP_ADDCMD_BTN.setAutoRaise(True)
        self.UP_ADDCMD_BTN.setObjectName("UP_ADDCMD_BTN")
        self.horizontalLayout_4.addWidget(self.UP_ADDCMD_BTN)
        self.UP_RMCMD_BTN = QtWidgets.QToolButton(rotencoderEditForm)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/minusIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.UP_RMCMD_BTN.setIcon(icon1)
        self.UP_RMCMD_BTN.setAutoRaise(True)
        self.UP_RMCMD_BTN.setObjectName("UP_RMCMD_BTN")
        self.horizontalLayout_4.addWidget(self.UP_RMCMD_BTN)
        self.testUP_CMDS_button = QtWidgets.QPushButton(rotencoderEditForm)
        self.testUP_CMDS_button.setObjectName("testUP_CMDS_button")
        self.horizontalLayout_4.addWidget(self.testUP_CMDS_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_11 = QtWidgets.QLabel(rotencoderEditForm)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.UP_ADDDREF_BTN = QtWidgets.QToolButton(rotencoderEditForm)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/plusIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.UP_ADDDREF_BTN.setIcon(icon2)
        self.UP_ADDDREF_BTN.setAutoRaise(True)
        self.UP_ADDDREF_BTN.setObjectName("UP_ADDDREF_BTN")
        self.horizontalLayout_5.addWidget(self.UP_ADDDREF_BTN)
        self.UP_RMDREF_BTN = QtWidgets.QToolButton(rotencoderEditForm)
        self.UP_RMDREF_BTN.setIcon(icon1)
        self.UP_RMDREF_BTN.setAutoRaise(True)
        self.UP_RMDREF_BTN.setObjectName("UP_RMDREF_BTN")
        self.horizontalLayout_5.addWidget(self.UP_RMDREF_BTN)
        self.testUPON_DREFS_button = QtWidgets.QPushButton(rotencoderEditForm)
        self.testUPON_DREFS_button.setObjectName("testUPON_DREFS_button")
        self.horizontalLayout_5.addWidget(self.testUPON_DREFS_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 2, 4, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 10, 0, 1, 5)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.DOWN_CMDS_TABLE = QtWidgets.QTableWidget(rotencoderEditForm)
        self.DOWN_CMDS_TABLE.setObjectName("DOWN_CMDS_TABLE")
        self.DOWN_CMDS_TABLE.setColumnCount(2)
        self.DOWN_CMDS_TABLE.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.DOWN_CMDS_TABLE.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.DOWN_CMDS_TABLE.setHorizontalHeaderItem(1, item)
        self.gridLayout_4.addWidget(self.DOWN_CMDS_TABLE, 6, 0, 1, 1)
        self.DOWN_DREFS_TABLE = QtWidgets.QTableWidget(rotencoderEditForm)
        self.DOWN_DREFS_TABLE.setObjectName("DOWN_DREFS_TABLE")
        self.DOWN_DREFS_TABLE.setColumnCount(6)
        self.DOWN_DREFS_TABLE.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.DOWN_DREFS_TABLE.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.DOWN_DREFS_TABLE.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.DOWN_DREFS_TABLE.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.DOWN_DREFS_TABLE.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.DOWN_DREFS_TABLE.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.DOWN_DREFS_TABLE.setHorizontalHeaderItem(5, item)
        self.gridLayout_4.addWidget(self.DOWN_DREFS_TABLE, 6, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_12 = QtWidgets.QLabel(rotencoderEditForm)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.DOWN_ADDCMD_BTN = QtWidgets.QToolButton(rotencoderEditForm)
        self.DOWN_ADDCMD_BTN.setIcon(icon)
        self.DOWN_ADDCMD_BTN.setAutoRaise(True)
        self.DOWN_ADDCMD_BTN.setObjectName("DOWN_ADDCMD_BTN")
        self.horizontalLayout_6.addWidget(self.DOWN_ADDCMD_BTN)
        self.DOWN_RMCMD_BTN = QtWidgets.QToolButton(rotencoderEditForm)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/minusIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.DOWN_RMCMD_BTN.setIcon(icon3)
        self.DOWN_RMCMD_BTN.setAutoRaise(True)
        self.DOWN_RMCMD_BTN.setObjectName("DOWN_RMCMD_BTN")
        self.horizontalLayout_6.addWidget(self.DOWN_RMCMD_BTN)
        self.testDOWN_CMDS_button = QtWidgets.QPushButton(rotencoderEditForm)
        self.testDOWN_CMDS_button.setObjectName("testDOWN_CMDS_button")
        self.horizontalLayout_6.addWidget(self.testDOWN_CMDS_button)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_14 = QtWidgets.QLabel(rotencoderEditForm)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_7.addWidget(self.label_14)
        self.DOWN_ADDDREF_BTN = QtWidgets.QToolButton(rotencoderEditForm)
        self.DOWN_ADDDREF_BTN.setIcon(icon)
        self.DOWN_ADDDREF_BTN.setAutoRaise(True)
        self.DOWN_ADDDREF_BTN.setObjectName("DOWN_ADDDREF_BTN")
        self.horizontalLayout_7.addWidget(self.DOWN_ADDDREF_BTN)
        self.DOWN_RMDREF_BTN = QtWidgets.QToolButton(rotencoderEditForm)
        self.DOWN_RMDREF_BTN.setIcon(icon3)
        self.DOWN_RMDREF_BTN.setAutoRaise(True)
        self.DOWN_RMDREF_BTN.setObjectName("DOWN_RMDREF_BTN")
        self.horizontalLayout_7.addWidget(self.DOWN_RMDREF_BTN)
        self.testDOWN_DREFS_button = QtWidgets.QPushButton(rotencoderEditForm)
        self.testDOWN_DREFS_button.setObjectName("testDOWN_DREFS_button")
        self.horizontalLayout_7.addWidget(self.testDOWN_DREFS_button)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.gridLayout_4.addLayout(self.horizontalLayout_7, 3, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 12, 0, 1, 5)
        self.nameLineEdit = QtWidgets.QLineEdit(rotencoderEditForm)
        self.nameLineEdit.setMinimumSize(QtCore.QSize(250, 0))
        self.nameLineEdit.setMaximumSize(QtCore.QSize(350, 16777215))
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.gridLayout.addWidget(self.nameLineEdit, 3, 1, 1, 3)
        self.switchStateButton = QtWidgets.QToolButton(rotencoderEditForm)
        self.switchStateButton.setEnabled(False)
        self.switchStateButton.setStyleSheet("border: 0px;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/switch_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/switch_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/switch_off.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/switch_on.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/switch_off.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/switch_on.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/switch_off.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/switch_on.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.switchStateButton.setIcon(icon4)
        self.switchStateButton.setIconSize(QtCore.QSize(66, 26))
        self.switchStateButton.setCheckable(True)
        self.switchStateButton.setAutoRaise(True)
        self.switchStateButton.setObjectName("switchStateButton")
        self.gridLayout.addWidget(self.switchStateButton, 1, 1, 1, 1)
        self.IDlineEdit = QtWidgets.QLineEdit(rotencoderEditForm)
        self.IDlineEdit.setEnabled(False)
        self.IDlineEdit.setMinimumSize(QtCore.QSize(250, 0))
        self.IDlineEdit.setMaximumSize(QtCore.QSize(350, 16777215))
        self.IDlineEdit.setReadOnly(True)
        self.IDlineEdit.setObjectName("IDlineEdit")
        self.gridLayout.addWidget(self.IDlineEdit, 4, 1, 1, 3)
        self.PINB_comboBox = QtWidgets.QComboBox(rotencoderEditForm)
        self.PINB_comboBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.PINB_comboBox.setObjectName("PINB_comboBox")
        self.gridLayout.addWidget(self.PINB_comboBox, 7, 1, 1, 1)
        self.label = QtWidgets.QLabel(rotencoderEditForm)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 7, 0, 1, 1)
        self.steps_comboBox = QtWidgets.QComboBox(rotencoderEditForm)
        self.steps_comboBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.steps_comboBox.setObjectName("steps_comboBox")
        self.gridLayout.addWidget(self.steps_comboBox, 5, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(rotencoderEditForm)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 2, 1, 1)

        self.retranslateUi(rotencoderEditForm)
        self.UP_ADDCMD_BTN.clicked.connect(rotencoderEditForm.addRotencUpCommand)
        self.UP_RMCMD_BTN.clicked.connect(rotencoderEditForm.rmRotencUpCommand)
        self.UP_ADDDREF_BTN.clicked.connect(rotencoderEditForm.addRotencUpDataref)
        self.UP_RMDREF_BTN.clicked.connect(rotencoderEditForm.rmRotencUpDataref)
        self.DOWN_ADDCMD_BTN.clicked.connect(rotencoderEditForm.addRotencDownCommand)
        self.DOWN_RMCMD_BTN.clicked.connect(rotencoderEditForm.rmRotencDownCommand)
        self.DOWN_ADDDREF_BTN.clicked.connect(rotencoderEditForm.addRotencDownDataref)
        self.DOWN_RMDREF_BTN.clicked.connect(rotencoderEditForm.rmRotencDownDataref)
        self.UP_CMDS_TABLE.cellDoubleClicked['int','int'].connect(rotencoderEditForm.editXPCommand)
        self.DOWN_CMDS_TABLE.cellDoubleClicked['int','int'].connect(rotencoderEditForm.editXPCommand)
        self.nameLineEdit.editingFinished.connect(rotencoderEditForm.updateXMLdata)
        self.PINA_comboBox.currentIndexChanged['int'].connect(rotencoderEditForm.updateXMLdata)
        self.UP_CMDS_TABLE.itemChanged['QTableWidgetItem*'].connect(rotencoderEditForm.updateXMLdata)
        self.DOWN_CMDS_TABLE.itemChanged['QTableWidgetItem*'].connect(rotencoderEditForm.updateXMLdata)
        self.testUP_CMDS_button.clicked.connect(rotencoderEditForm.testOnCommands)
        self.testDOWN_CMDS_button.clicked.connect(rotencoderEditForm.testOffCommands)
        self.PINA_comboBox.currentTextChanged['QString'].connect(rotencoderEditForm.updatePin)
        self.UP_DREFS_TABLE.cellDoubleClicked['int','int'].connect(rotencoderEditForm.editXPDataref)
        self.DOWN_DREFS_TABLE.cellDoubleClicked['int','int'].connect(rotencoderEditForm.editXPDataref)
        self.UP_DREFS_TABLE.itemChanged['QTableWidgetItem*'].connect(rotencoderEditForm.updateXMLdata)
        self.DOWN_DREFS_TABLE.itemChanged['QTableWidgetItem*'].connect(rotencoderEditForm.updateXMLdata)
        self.testDOWN_DREFS_button.clicked.connect(rotencoderEditForm.testOffDatarefs)
        self.testUPON_DREFS_button.clicked.connect(rotencoderEditForm.testOnDatarefs)
        self.UP_CMDS_TABLE.cellChanged['int','int'].connect(rotencoderEditForm.activateSave)
        self.PINB_comboBox.currentIndexChanged['int'].connect(rotencoderEditForm.updateXMLdata)
        self.PINB_comboBox.currentTextChanged['QString'].connect(rotencoderEditForm.updatePin)
        self.steps_comboBox.currentIndexChanged['QString'].connect(rotencoderEditForm.updateXMLdata)
        self.steps_comboBox.currentTextChanged['QString'].connect(rotencoderEditForm.updatePin)
        QtCore.QMetaObject.connectSlotsByName(rotencoderEditForm)

    def retranslateUi(self, rotencoderEditForm):
        _translate = QtCore.QCoreApplication.translate
        rotencoderEditForm.setWindowTitle(_translate("rotencoderEditForm", "Form"))
        self.label_8.setText(_translate("rotencoderEditForm", "Edit rotary encoder"))
        self.label_17.setText(_translate("rotencoderEditForm", "State"))
        self.label_19.setText(_translate("rotencoderEditForm", "ID"))
        self.label_3.setText(_translate("rotencoderEditForm", "Name"))
        self.label_15.setText(_translate("rotencoderEditForm", "Rotary encoder DOWN actions"))
        self.label_18.setText(_translate("rotencoderEditForm", "Arduino pin A:"))
        self.label_9.setText(_translate("rotencoderEditForm", "Rotary encoder UP actions:"))
        item = self.UP_CMDS_TABLE.horizontalHeaderItem(0)
        item.setText(_translate("rotencoderEditForm", "Command"))
        item = self.UP_CMDS_TABLE.horizontalHeaderItem(1)
        item.setText(_translate("rotencoderEditForm", "Send continuously"))
        item = self.UP_DREFS_TABLE.horizontalHeaderItem(0)
        item.setText(_translate("rotencoderEditForm", "Dataref"))
        item = self.UP_DREFS_TABLE.horizontalHeaderItem(1)
        item.setText(_translate("rotencoderEditForm", "Index"))
        item = self.UP_DREFS_TABLE.horizontalHeaderItem(2)
        item.setText(_translate("rotencoderEditForm", "Set to Value"))
        item = self.UP_DREFS_TABLE.horizontalHeaderItem(3)
        item.setText(_translate("rotencoderEditForm", "Set continuously"))
        item = self.UP_DREFS_TABLE.horizontalHeaderItem(4)
        item.setText(_translate("rotencoderEditForm", "Type"))
        item = self.UP_DREFS_TABLE.horizontalHeaderItem(5)
        item.setText(_translate("rotencoderEditForm", "Unit"))
        self.label_10.setText(_translate("rotencoderEditForm", "Send XPlane Commands: "))
        self.UP_ADDCMD_BTN.setText(_translate("rotencoderEditForm", "..."))
        self.UP_RMCMD_BTN.setText(_translate("rotencoderEditForm", "..."))
        self.testUP_CMDS_button.setText(_translate("rotencoderEditForm", "Test"))
        self.label_11.setText(_translate("rotencoderEditForm", "Set Dataref: "))
        self.UP_ADDDREF_BTN.setText(_translate("rotencoderEditForm", "..."))
        self.UP_RMDREF_BTN.setText(_translate("rotencoderEditForm", "..."))
        self.testUPON_DREFS_button.setText(_translate("rotencoderEditForm", "Test"))
        item = self.DOWN_CMDS_TABLE.horizontalHeaderItem(0)
        item.setText(_translate("rotencoderEditForm", "Command"))
        item = self.DOWN_CMDS_TABLE.horizontalHeaderItem(1)
        item.setText(_translate("rotencoderEditForm", "Send continuously"))
        item = self.DOWN_DREFS_TABLE.horizontalHeaderItem(0)
        item.setText(_translate("rotencoderEditForm", "Dataref"))
        item = self.DOWN_DREFS_TABLE.horizontalHeaderItem(1)
        item.setText(_translate("rotencoderEditForm", "Index"))
        item = self.DOWN_DREFS_TABLE.horizontalHeaderItem(2)
        item.setText(_translate("rotencoderEditForm", "Set to Value"))
        item = self.DOWN_DREFS_TABLE.horizontalHeaderItem(3)
        item.setText(_translate("rotencoderEditForm", "Set continuously"))
        item = self.DOWN_DREFS_TABLE.horizontalHeaderItem(4)
        item.setText(_translate("rotencoderEditForm", "Type"))
        item = self.DOWN_DREFS_TABLE.horizontalHeaderItem(5)
        item.setText(_translate("rotencoderEditForm", "Unit"))
        self.label_12.setText(_translate("rotencoderEditForm", "Send XPlane Command: "))
        self.DOWN_ADDCMD_BTN.setText(_translate("rotencoderEditForm", "..."))
        self.DOWN_RMCMD_BTN.setText(_translate("rotencoderEditForm", "..."))
        self.testDOWN_CMDS_button.setText(_translate("rotencoderEditForm", "Test"))
        self.label_14.setText(_translate("rotencoderEditForm", "Set Dataref:"))
        self.DOWN_ADDDREF_BTN.setText(_translate("rotencoderEditForm", "..."))
        self.DOWN_RMDREF_BTN.setText(_translate("rotencoderEditForm", "..."))
        self.testDOWN_DREFS_button.setText(_translate("rotencoderEditForm", "Test"))
        self.switchStateButton.setText(_translate("rotencoderEditForm", "..."))
        self.label.setText(_translate("rotencoderEditForm", "Arduino pin B:"))
        self.label_2.setText(_translate("rotencoderEditForm", "Steps per notch: "))

import resources_rc
