'''
Created on 11/10/2012

@author: sebastien
'''

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Import(object):
    def setupUi(self, Import):
        Import.setObjectName(_fromUtf8("Import"))
        Import.resize(386, 186)
        self.verticalLayout = QtGui.QVBoxLayout(Import)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.Description = QtGui.QLabel(Import)
        self.Description.setWordWrap(True)
        self.Description.setObjectName(_fromUtf8("Description"))
        self.verticalLayout.addWidget(self.Description)
        self.progressBar = QtGui.QProgressBar(Import)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.finishedButton = QtGui.QWidget(Import)
        self.finishedButton.setObjectName(_fromUtf8("finishedButton"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.finishedButton)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.closeButton = QtGui.QPushButton(self.finishedButton)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout.addWidget(self.finishedButton)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(Import)
        QtCore.QMetaObject.connectSlotsByName(Import)

    def retranslateUi(self, Import):
        Import.setWindowTitle(QtGui.QApplication.translate("Import", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.Description.setText(QtGui.QApplication.translate("Import", "Importing from: #########", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("Import", "Close", None, QtGui.QApplication.UnicodeUTF8))

    def setProgress(self, value):
        self.progressBar.setProperty("value", value)
        if value >= 100:
            pass

    def getFile(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 
        '/home')
        
        f = open(fname, 'r')
        
        with f:        
            data = f.read()
            #self.textEdit.setText(data) 

            
            
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Import = QtGui.QDialog()
    ui = Ui_Import()
    ui.setupUi(Import)
    Import.show()
    sys.exit(app.exec_())