# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ue.ui'
#
# Created: Wed Oct 10 17:53:49 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_UEarea(object):
    def setupUi(self, UEarea):
        self.ue = []
        UEarea.setObjectName(_fromUtf8("UEarea"))
        UEarea.resize(609, 531)
        self.verticalLayout_7 = QtGui.QVBoxLayout(UEarea)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.scrollAreaUE = QtGui.QScrollArea(UEarea)
        self.scrollAreaUE.setWidgetResizable(True)
        self.scrollAreaUE.setObjectName(_fromUtf8("scrollAreaUE"))
        self.scrollAreaUEWidgetContents = QtGui.QWidget()
        self.scrollAreaUEWidgetContents.setGeometry(QtCore.QRect(0, 0, 589, 511))
        self.scrollAreaUEWidgetContents.setObjectName(_fromUtf8("scrollAreaUEWidgetContents"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.scrollAreaUEWidgetContents)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        
        
        
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.scrollAreaUE.setWidget(self.scrollAreaUEWidgetContents)
        self.verticalLayout_7.addWidget(self.scrollAreaUE)
        
        # loop and add
        self.addEntry("fe", "")
        self.addEntry("cs", "")
        self.addEntry("fes", "")
        self.addEntry("czsc", "")
        self.addEntry(" as", "")
        self.addEntry("wq", "")
        self.addEntry("", "")
        self.addEntry("", "")
        self.addEntry("", "")
        self.addEntry("", "")
        self.addEntry("", "")
        self.addEntry("", "")
        self.addEntry("", "")
        self.addEntry("", "")
        self.addEntry("", "")
        self.addEntry("", "")
        self.addEntry("", "")
        self.addEntry("", "")
        self.addEntry("", "")
        self.addEntry("", "")
        self.addEntry("", "")
        self.addEntry("", "")
        self.addEntry("", "")


        self.retranslateUi(UEarea)
        QtCore.QMetaObject.connectSlotsByName(UEarea)

    def retranslateUi(self, UEarea):
        UEarea.setWindowTitle(QtGui.QApplication.translate("UEarea", "Form", None, QtGui.QApplication.UnicodeUTF8))
        
    def addEntry(self, label, meaning):
        #usage example1
        usageExample = Ui_usageExampleSgl(self.scrollAreaUEWidgetContents)
        usageExample.setObjectName(_fromUtf8("usageExample"))
        usageExample.addElement(label)
        
        self.verticalLayout_4.addWidget(usageExample)
        self.ue.append(usageExample)
        
        
        
class Ui_usageExampleSgl(QtGui.QWidget):
    def __init__(self, parent):
        super(Ui_usageExampleSgl, self).__init__(parent)
        self.setupUi()
        
    def setupUi(self):
        
        #self.setAcceptDrops(True)
        
        #self.setDragEnabled(True)
        
        self.setObjectName(_fromUtf8("usageExample"))
        self.horizontalLayout = QtGui.QHBoxLayout(self)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.words = []
        self.parts = []
        for part in self.words:
            temp = QtGui.QLabel(self)
            temp.setObjectName(part)
            temp.setText(part)
            self.horizontalLayout.addWidget(temp)
            self.parts.append(temp)
        
        self.spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.spacerItem)

        QtCore.QMetaObject.connectSlotsByName(self)
        
    def addElement(self, text):
        temp = QtGui.QLabel(self)
        temp.setObjectName(text)
        temp.setText(text)
        self.horizontalLayout.addWidget(temp)
        self.parts.append(temp)
        self.horizontalLayout.removeItem(self.spacerItem)
        self.horizontalLayout.addItem(self.spacerItem)

        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    UEarea = QtGui.QWidget()
    ui = Ui_UEarea()
    ui.setupUi(UEarea)
    UEarea.show()
    sys.exit(app.exec_())

