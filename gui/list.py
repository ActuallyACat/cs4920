# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list.ui'
#
# Created: Mon Oct  8 17:54:58 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_Lists(QtGui.QWidget):
    def __init__(self, parent, control):
        super(Ui_Lists, self).__init__(parent)
        self.setupUi(control)
        
    def setupUi(self, control):
        """initial setup for lists
        Consists of buttons for 'new UE list' and 'new word list' as well as functionality
        to all for a drop down to add new lists.
        This is all housed on the left hand side of the main setup and has scrolling functionality
        if the lists become too long.

        There is  also the ability to adjust the width of the left hand side with a fix minimum size.
        """
        self.control = control
        self.words = []
        self.UEs = []
        self.setObjectName(_fromUtf8("Form"))
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollAreaLists = QtGui.QScrollArea(self)
        self.scrollAreaLists.setFrameShape(QtGui.QFrame.StyledPanel)
        self.scrollAreaLists.setFrameShadow(QtGui.QFrame.Sunken)
        self.scrollAreaLists.setLineWidth(1)
        self.scrollAreaLists.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollAreaLists.setWidgetResizable(True)
        self.scrollAreaLists.setObjectName(_fromUtf8("scrollAreaLists"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.ListUENewButton = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.ListUENewButton.setObjectName(_fromUtf8("ListUENewButton"))
        self.verticalLayout_2.addWidget(self.ListUENewButton)
        self.List = QtGui.QWidget(self.scrollAreaWidgetContents_2)
        self.List.setObjectName(_fromUtf8("List"))
        self.verticalLayout_2.addWidget(self.List)
        self.ListWordNewButton = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.ListWordNewButton.setObjectName(_fromUtf8("ListWordNewButton"))
        self.verticalLayout_2.addWidget(self.ListWordNewButton)
        self.spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.spacerItem)
        self.scrollAreaLists.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollAreaLists)

        self.retranslateUi()
        QtCore.QObject.connect(self.ListUENewButton, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.newUEList())
        QtCore.QObject.connect(self.ListWordNewButton, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.newWordList())
        QtCore.QMetaObject.connectSlotsByName(self)
        
        
        self.displayNone()
        self.displayAll()
        self.hideWordListButton()

    def retranslateUi(self):
	"""allows buttons to shift correctly if left hand side gets extended"""
        self.ListUENewButton.setText(QtGui.QApplication.translate("Form", "New UE List", None, QtGui.QApplication.UnicodeUTF8))
        self.ListWordNewButton.setText(QtGui.QApplication.translate("Form", "New Word List", None, QtGui.QApplication.UnicodeUTF8))

    def newWordList(self):
	"""definitions for the button newWordList and also to set up on release state"""
        temp = Ui_List(self, self.control)
        self.words.append(temp)
        self.displayNone()
        self.displayAll()
    
    def newUEList(self):
	"""definitions for the button newUEList and also to set up on release state"""
        temp = Ui_List(self, self.control)
        self.UEs.append(temp)
        self.displayNone()
        self.displayAll()
        
    def populateWords(self, names):
	"""add words to a word list"""
        self.clearWordList()
        for name in names:
            temp = Ui_List(self, self.control)
            temp.populate(name)
            self.words.append(temp)
            
        self.displayNone()
        self.displayAll()
        
    def populateUEs(self, names):
	"""add UEs to a UE list"""
        self.clearUEList()
        for name in names:
            temp = Ui_List(self, self.control)
            temp.populate(name)
            self.UEs.append(temp)
        
        self.displayNone()
        self.displayAll()
        
    def displayAll(self):
	"""expand all words and UE lists to be displayed"""
        self.verticalLayout_2.addWidget(self.ListUENewButton)
        for ue in self.UEs:
            self.verticalLayout_2.addWidget(ue)
        
        self.verticalLayout_2.addWidget(self.ListWordNewButton)
        for word in self.words:
            self.verticalLayout_2.addWidget(word)
            
        self.verticalLayout_2.addItem(self.spacerItem)
        
    def displayNone(self):
	"""hide all words and UE lists from being displayed"""
        self.verticalLayout_2.removeWidget(self.ListUENewButton)
        for ue in self.UEs:
            self.verticalLayout_2.removeWidget(ue)
        
        self.verticalLayout_2.removeWidget(self.ListWordNewButton)
        for word in self.words:
            self.verticalLayout_2.removeWidget(word)
            
        self.verticalLayout_2.removeItem(self.spacerItem)
            
            
    def clearUEList(self):
	"""delete the current UE list, make a new empty list and hide"""
        for word in self.words:
            word.hide()
            word.destroy()
            self.words.remove(word)
            
    def clearWordList(self):
	"""delete the current word list, make a new empty list and hide"""
        for ue in self.UEs:
            ue.hide()
            ue.destroy()
            self.meanings.remove(ue)
        
    def displayText(self, list):
        list.displayText()
        if list in self.words:
            self.control.newWordList(list.text)
        elif list in self.UEs:
            self.control.newUEList(list.text)
    

    def hideWordListButton(self):
	"""This was implemented in the eventuality that we may not have wordlists completed"""
        self.ListWordNewButton.hide()

class Ui_List(QtGui.QWidget):
    """
    This is used for the creation of new lists under word or UE lists
    """
    def __init__(self, parent, control):
        super(Ui_List, self).__init__(parent)
        self.setupUi(control, parent)
        
    def setupUi(self, control, parent):
        self.control = control
        self.parent = parent
        self.text = ""
        self.setObjectName(_fromUtf8("List"))
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ListNameEdit = QtGui.QLineEdit(self)
        self.ListNameEdit.setObjectName(_fromUtf8("ListNameEdit"))
        self.verticalLayout.addWidget(self.ListNameEdit)
        self.Listendview = QtGui.QWidget(self)
        self.Listendview.setObjectName(_fromUtf8("Listendview"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.Listendview)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.line_2 = QtGui.QFrame(self.Listendview)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout.addWidget(self.line_2)
        self.viewButton = QtGui.QToolButton(self.Listendview)
        self.viewButton.setObjectName(_fromUtf8("viewButton"))
        self.horizontalLayout.addWidget(self.viewButton)
        self.line = QtGui.QFrame(self.Listendview)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.label = QtGui.QLabel(self.Listendview)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.Listendview)
        
        self.retranslateUi()
        self.namechange()
        QtCore.QObject.connect(self.ListNameEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), lambda: self.parent.displayText(self))
        QtCore.QObject.connect(self.viewButton, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.control.viewList(self.text))
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
	"""allow the buttons to scale if dimenisions change"""
        self.label.setText(QtGui.QApplication.translate("List", self.text, None, QtGui.QApplication.UnicodeUTF8))
        self.viewButton.setText(QtGui.QApplication.translate("List", "View", None, QtGui.QApplication.UnicodeUTF8))


    def namechange(self):
	"""change the name of the list"""
        self.Listendview.hide()
        self.ListNameEdit.show()
        self.viewButton.setDisabled(True)
        
    def populate(self, text):
        self.displayText()
        self.text = text
        self.label.setText(QtGui.QApplication.translate("List", self.text, None, QtGui.QApplication.UnicodeUTF8))
    
    def displayText(self):
        self.ListNameEdit.hide()
        self.Listendview.show()
        self.text = self.ListNameEdit.text()
        self.label.setText(QtGui.QApplication.translate("List", self.text, None, QtGui.QApplication.UnicodeUTF8))
        self.viewButton.setEnabled(True)
