# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlceditor.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(812, 608)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(490, 9, 311, 481))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 309, 479))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 311, 481))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 471, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 10, 461, 391))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.idBox = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.idBox.setObjectName("idBox")
        self.gridLayout_5.addWidget(self.idBox, 9, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 6, 1, 1, 1)
        self.fileURL = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.fileURL.setObjectName("fileURL")
        self.gridLayout_5.addWidget(self.fileURL, 5, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 8, 1, 1, 1)
        self.comboAction = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.comboAction.setObjectName("comboAction")
        self.comboAction.addItem("")
        self.comboAction.addItem("")
        self.gridLayout_5.addWidget(self.comboAction, 3, 1, 1, 1)
        self.fileName = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.fileName.setObjectName("fileName")
        self.gridLayout_5.addWidget(self.fileName, 7, 1, 1, 1)
        self.comboType = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.comboType.setObjectName("comboType")
        self.comboType.addItem("")
        self.comboType.addItem("")
        self.comboType.addItem("")
        self.comboType.addItem("")
        self.comboType.addItem("")
        self.comboType.addItem("")
        self.comboType.addItem("")
        self.comboType.addItem("")
        self.comboType.addItem("")
        self.gridLayout_5.addWidget(self.comboType, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 2, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.gridLayoutWidget_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.valueTabs = QtWidgets.QTabWidget(self.groupBox_2)
        self.valueTabs.setGeometry(QtCore.QRect(10, 20, 441, 80))
        self.valueTabs.setObjectName("valueTabs")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.valueBool = QtWidgets.QComboBox(self.tab)
        self.valueBool.setGeometry(QtCore.QRect(10, 20, 191, 22))
        self.valueBool.setObjectName("valueBool")
        self.valueBool.addItem("")
        self.valueBool.addItem("")
        self.valueTabs.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.valueText = QtWidgets.QLineEdit(self.tab_3)
        self.valueText.setGeometry(QtCore.QRect(10, 20, 401, 21))
        self.valueText.setObjectName("valueText")
        self.valueTabs.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.valueInt = QtWidgets.QSpinBox(self.tab_4)
        self.valueInt.setGeometry(QtCore.QRect(11, 20, 191, 22))
        self.valueInt.setMinimum(-99999999)
        self.valueInt.setMaximum(99999999)
        self.valueInt.setObjectName("valueInt")
        self.valueTabs.addTab(self.tab_4, "")
        self.gridLayout_5.addWidget(self.groupBox_2, 10, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.groupBox = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 441, 261))
        self.groupBox.setObjectName("groupBox")
        self.generateButton = QtWidgets.QPushButton(self.groupBox)
        self.generateButton.setGeometry(QtCore.QRect(300, 220, 121, 23))
        self.generateButton.setObjectName("generateButton")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 20, 411, 191))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 409, 189))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scriptText = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.scriptText.setGeometry(QtCore.QRect(0, 0, 411, 191))
        self.scriptText.setObjectName("scriptText")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.tab_5, "")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 500, 791, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.addButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.copyButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.copyButton.setObjectName("copyButton")
        self.horizontalLayout.addWidget(self.copyButton)
        self.deleteButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        spacerItem2 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.valueTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DLCEditor"))
        self.label_7.setText(_translate("MainWindow", "Tipo:"))
        self.label.setText(_translate("MainWindow", "Nombre:"))
        self.label_5.setText(_translate("MainWindow", "URL de archivo:"))
        self.label_2.setText(_translate("MainWindow", "ID:"))
        self.comboAction.setItemText(0, _translate("MainWindow", "Agregar"))
        self.comboAction.setItemText(1, _translate("MainWindow", "Actualizar"))
        self.comboType.setItemText(0, _translate("MainWindow", "Mapa"))
        self.comboType.setItemText(1, _translate("MainWindow", "Tileset"))
        self.comboType.setItemText(2, _translate("MainWindow", "Script"))
        self.comboType.setItemText(3, _translate("MainWindow", "Data"))
        self.comboType.setItemText(4, _translate("MainWindow", "PBS"))
        self.comboType.setItemText(5, _translate("MainWindow", "Audio"))
        self.comboType.setItemText(6, _translate("MainWindow", "Graphics"))
        self.comboType.setItemText(7, _translate("MainWindow", "Variable"))
        self.comboType.setItemText(8, _translate("MainWindow", "Interruptor"))
        self.label_6.setText(_translate("MainWindow", "Acción:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Valor"))
        self.valueBool.setItemText(0, _translate("MainWindow", "true"))
        self.valueBool.setItemText(1, _translate("MainWindow", "false"))
        self.valueTabs.setTabText(self.valueTabs.indexOf(self.tab), _translate("MainWindow", "Booleano"))
        self.valueTabs.setTabText(self.valueTabs.indexOf(self.tab_3), _translate("MainWindow", "Texto"))
        self.valueTabs.setTabText(self.valueTabs.indexOf(self.tab_4), _translate("MainWindow", "Número"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Código"))
        self.groupBox.setTitle(_translate("MainWindow", "Script"))
        self.generateButton.setText(_translate("MainWindow", "Generar y copiar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Herramientas"))
        self.addButton.setText(_translate("MainWindow", "Añadir"))
        self.copyButton.setText(_translate("MainWindow", "Copiar"))
        self.deleteButton.setText(_translate("MainWindow", "Borrar paso"))
