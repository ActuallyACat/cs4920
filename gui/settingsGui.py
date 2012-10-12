# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Fri Oct 12 15:10:05 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_settings(QtGui.QDialog):
    def __init__(self, settingsControl):
        super(Ui_settings, self).__init__()
        self.setupUi(settingsControl)
        
    def setupUi(self, settings):
        self.components = []
        self.settingsControl = settings
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget_2 = QtGui.QWidget(self)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.widget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget_2)
        
        self.spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.spacerItem)
        
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi()
        
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.settingsControl.saveAll())

        QtCore.QMetaObject.connectSlotsByName(self)
        self.settingsControl.setSettingsGui(self)

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("settings", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("settings", "Settings:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("settings", "Save All Changes", None, QtGui.QApplication.UnicodeUTF8))

    def addSettingComponent(self, settingsComponent):
        self.verticalLayout.removeItem(self.spacerItem)
        self.verticalLayout.removeWidget(self.pushButton)
        self.verticalLayout.addWidget(settingsComponent)
        self.components.append(settingsComponent)
        self.verticalLayout.addItem(self.spacerItem)
        self.verticalLayout.addWidget(self.pushButton)


class Ui_settingsComponent(QtGui.QWidget):
    def __init__(self, parent, settingsControl):
        super(Ui_settingsComponent, self).__init__(parent)
        self.setupUi(settingsControl)
    def setupUi(self, settingsControl):
        self.data = ""
        self.settingsControl = settingsControl
        self.setObjectName(_fromUtf8("Form"))
        self.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(self)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.widget_3 = QtGui.QWidget(self.widget)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.widget_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_4 = QtGui.QWidget(self.widget)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lineEdit = QtGui.QLineEdit(self.widget_4)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.pushButton_2 = QtGui.QPushButton(self.widget_4)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi()
        
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.settingsControl)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), lambda: self.settingsControl)
 
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Anki Deck Location:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "Location", None, QtGui.QApplication.UnicodeUTF8))

    def setLabel(self, text):
        self.label_2.setText(_fromUtf8(text))

    def setButtonText(self, text):
        self.pushButton_2.setText(_fromUtf8(text))
        
    def setData(self, text):
        self.data = text
        self.lineEdit.setText(_fromUtf8(text))
        
    def getData(self):
        return self.lineEdit.text()
        
    def setButtonAction(self, action):
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("released()")), action)
 


class settingsControl(object):

    def __init__(self):
        pass
    
    def setSettingsGui(self, gui):
        self.gui = gui
        
        settingsComponent = Ui_settingsComponent(self.gui, self)
        settingsComponent.setButtonText("choose file")
        settingsComponent.setLabel("Anki deck location")
        settingsComponent.setData("/home") #get from database
        settingsComponent.setButtonAction(lambda: self.filechooser(settingsComponent))
        self.gui.addSettingComponent(settingsComponent)
    
    def filechooser(self, settingsComponent):
        fname = QtGui.QFileDialog.getOpenFileName(self.gui, 'Open file', '/home')
        settingsComponent.setData(fname)
    
    def saveAll(self):
        for settingsComponent in self.gui.components:
            data = settingsComponent.getData()
            print data

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    settingsControl = settingsControl()
    settingsGui = Ui_settings(settingsControl)
    settingsGui.show()
    sys.exit(app.exec_())

