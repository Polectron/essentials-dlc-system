import zlib
import sys
import pyperclip
import json
import base64

from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication
from dlceditor import Ui_MainWindow

MAP = 0
TILESET = 1
SCRIPT = 2
DATA = 3
PBS = 4
AUDIO = 5
GRAPHICS = 6
VARIABLE = 7
SWITCH = 8

ADD = 0
UPDATE = 1
SET = 2

BOOL = 0
STR = 1
INT = 2

class DLCEditor(QMainWindow):
    def __init__(self):
        super(DLCEditor, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.steps = {"steps":[]}
        self.setUI()
        self.typeIndex = self.ui.comboType.currentIndex()
        self.actionIndex = self.ui.comboAction.currentIndex()

    def setUI(self):

        self.ui.plainTextEdit.setReadOnly(True)
        self.updateTextEdit()

        self.ui.copyButton.clicked.connect(self.copy)
        self.ui.addButton.clicked.connect(self.addStep)
        self.ui.deleteButton.clicked.connect(self.removeStep)
        self.ui.generateButton.clicked.connect(self.generateScript)
        self.ui.comboType.currentIndexChanged.connect(self.updateForm)
        self.ui.comboAction.currentIndexChanged.connect(self.updateForm)
        self.ui.tabWidget.currentChanged.connect(self.changedTab)

        self.ui.valueTabs.setEnabled(False)
        self.ui.valueTabs.setCurrentIndex(0)

        self.ui.tabWidget

        print(self.ui.comboType.model().item(PBS).setEnabled(False))

        self.show()

    def changedTab(self):
        if self.ui.tabWidget.currentIndex() == 1:
            self.ui.addButton.setEnabled(False)
        else:
            self.ui.addButton.setEnabled(True)

    def copy(self):
        pyperclip.copy(self.ui.plainTextEdit.toPlainText())

    def addStep(self):
        #print(self.typeIndex, self.actionIndex)

        if self.typeIndex == MAP:
            if self.actionIndex == ADD:
                self.steps["steps"].append({"action":"add","type":"map","file":self.ui.fileURL.text(),"name":self.ui.fileName.text(),"id":self.ui.idBox.value()})
            elif self.actionIndex == UPDATE:
                self.steps["steps"].append({"action":"update","type":"map","file":self.ui.fileURL.text(),"id":self.ui.idBox.value()})
        elif self.typeIndex == VARIABLE:
            #print(self.actionIndex)
            if self.actionIndex == SET:
                value = None
                if self.ui.valueTabs.currentIndex() == BOOL:
                    value = self.ui.valueBool.currentIndex() == 0
                elif self.ui.valueTabs.currentIndex() == STR:
                    value = self.ui.valueText.text()
                elif self.ui.valueTabs.currentIndex() == INT:
                    value = self.ui.valueInt.value()
                self.steps["steps"].append({"action":"set","type":"variable","id":self.ui.idBox.value(),"value":value})
        elif self.typeIndex == SWITCH:
            if self.actionIndex == SET:
                value = None
                if self.ui.valueTabs.currentIndex() == BOOL:
                    value = self.ui.valueBool.currentIndex() == 0
                self.steps["steps"].append({"action":"set","type":"switch","id":self.ui.idBox.value(),"value":value})
        elif self.typeIndex == SCRIPT:
            self.steps["steps"].append({"action":"add","type":"script","file":self.ui.fileURL.text(),"name":self.ui.fileName.text()})
        elif self.typeIndex == TILESET:
            self.steps["steps"].append({"action":"add","type":"tileset","file":self.ui.fileURL.text(),"id":self.ui.idBox.value()})
        elif self.typeIndex == DATA:
            self.steps["steps"].append({"action":"add","type":"data","file":self.ui.fileURL.text(),"name":self.ui.fileName.text()})
        elif self.typeIndex == PBS:
            self.steps["steps"].append({"action":"add","type":"pbs","file":self.ui.fileURL.text(),"name":self.ui.fileName.text()})
        elif self.typeIndex == AUDIO:
            self.steps["steps"].append({"action":"add","type":"audio","file":self.ui.fileURL.text(),"name":self.ui.fileName.text()})
        elif self.typeIndex == GRAPHICS:
            self.steps["steps"].append({"action":"add","type":"graphics","file":self.ui.fileURL.text(),"name":self.ui.fileName.text()})

        self.ui.plainTextEdit.clear()
        self.updateTextEdit()

    def removeStep(self):
        if len(self.steps["steps"])>=1:
            self.steps["steps"].pop()
            self.updateTextEdit()

    def updateTextEdit(self):
        self.ui.plainTextEdit.setPlainText(json.dumps(self.steps, indent=4, sort_keys=True))

    def generateScript(self):
        compressed = zlib.compress(self.ui.scriptText.toPlainText().encode("UTF-8"))
        compressed = base64.b64encode(compressed)
        #print(compressed)
        pyperclip.copy(compressed.decode("UTF-8"))

    def updateForm(self):
        self.typeIndex = self.ui.comboType.currentIndex()
        self.actionIndex = self.ui.comboAction.currentIndex()
        self.ui.label.setText("Nombre: ")

        self.ui.fileName.setEnabled(True)
        self.ui.fileURL.setEnabled(True)
        self.ui.idBox.setEnabled(True)
        self.ui.fileName.setText("")
        self.ui.fileURL.setText("")

        if self.typeIndex == VARIABLE or self.typeIndex == SWITCH:
            self.actionIndex = SET
            if self.ui.comboAction.count() < 3:
                self.ui.comboAction.addItem("Establecer valor")
            self.ui.comboAction.setCurrentIndex(SET)
            self.ui.fileURL.setEnabled(False)
            self.ui.fileName.setEnabled(False)
            self.ui.valueTabs.setEnabled(True)

            if self.typeIndex == VARIABLE:
                self.ui.valueTabs.setTabEnabled(0, True)
                self.ui.valueTabs.setTabEnabled(1, True)
                self.ui.valueTabs.setTabEnabled(2, True)

            elif self.typeIndex == SWITCH:
                self.ui.valueTabs.setTabEnabled(0, True)
                self.ui.valueTabs.setTabEnabled(1, False)
                self.ui.valueTabs.setTabEnabled(2, False)
        else:
            self.ui.valueTabs.setEnabled(False)
            if self.ui.comboAction.count() > 2:
                self.ui.comboAction.removeItem(2)
                self.ui.comboAction.setCurrentIndex(0)

            if self.typeIndex == MAP:
                if self.actionIndex == UPDATE:
                    self.ui.fileName.setEnabled(False)
            elif self.typeIndex == TILESET:
                self.ui.fileName.setEnabled(False)
            elif self.typeIndex == AUDIO:
                self.ui.label.setText("Nombre de carpeta: ")
                self.ui.idBox.setEnabled(False)
            elif self.typeIndex == GRAPHICS:
                self.ui.label.setText("Nombre de carpeta: ")
                self.ui.idBox.setEnabled(False)
            elif self.typeIndex == PBS:
                self.ui.idBox.setEnabled(False)
            elif self.typeIndex == DATA:
                self.ui.label.setText("Nombre: ")
                self.ui.idBox.setEnabled(False)
            elif self.typeIndex == SCRIPT:
                self.ui.idBox.setEnabled(False)




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = DLCEditor()
    sys.exit(app.exec_())

