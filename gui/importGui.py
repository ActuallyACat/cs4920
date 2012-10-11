'''
Created on 11/10/2012

@author: sebastien
'''

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Import(QtGui.QDialog):
    def __init__(self):
        super(Ui_Import, self).__init__()
        self.setupUi()
        
    def setupUi(self):
        self.setObjectName(_fromUtf8("Import"))
        self.resize(386, 186)
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.Description = QtGui.QLabel(self)
        self.Description.setWordWrap(True)
        self.Description.setObjectName(_fromUtf8("Description"))
        self.verticalLayout.addWidget(self.Description)
        self.progressBar = QtGui.QProgressBar(self)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.finishedButtonArea = QtGui.QWidget(self)
        self.finishedButtonArea.setObjectName(_fromUtf8("finishedButton"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.finishedButtonArea)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.closeButton = QtGui.QPushButton(self.finishedButtonArea)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout.addWidget(self.finishedButtonArea)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setProgress(0)

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("Import", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("Import", "Close", None, QtGui.QApplication.UnicodeUTF8))

    def setProgress(self, value):
        self.progressBar.setProperty("value", value)
        if value < 100:
            self.closeButton.setDisabled(True)
            
    def setText(self, text):
        self.Description.setText(_fromUtf8(text))

    def getFile(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 
        '/home')
        
        return fname

            
            
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Import = Ui_Import()
    Import.setText("Importing From: " + "blaeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeh")
    Import.show()
    Import.setProgress(50)
    sys.exit(app.exec_())