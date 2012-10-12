# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'meaningArea.ui'
#
# Created: Wed Oct 10 15:50:01 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!



from PyQt4 import QtCore, QtGui
from noj.data_structures import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_meaningArea(QtGui.QWidget):
    """ Ui_meaningArea is a subsection of the overall dictionary interface.
    It displays the the matched words, then finds the associated meanings and translation.
    """
    def __init__(self, parent, control):
        super(Ui_meaningArea, self).__init__(parent)
        self.setupUi(control)
        
    def setupUi(self, control):
        self.control = control
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.meanings = []
        
        
    def addMeaning(self, meaning, translation, meaning_object):
        """ meanings is a button you can select for UE to be populated.
        """
        meaningEntry = QtGui.QWidget(self)
        meaningEntry.setObjectName(_fromUtf8("meaningEntry"))
        meaningEntry.horizontalLayout_2 = QtGui.QHBoxLayout(meaningEntry)
        meaningEntry.horizontalLayout_2.setMargin(0)
        meaningEntry.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        meaningEntry.meaningButton = QtGui.QPushButton(meaningEntry)
        meaningEntry.meaningButton.setObjectName(_fromUtf8("meaningButton"))
        meaningEntry.horizontalLayout_2.addWidget(meaningEntry.meaningButton)
        meaningEntry.meaningLabel = QtGui.QLabel(meaningEntry)
        meaningEntry.meaningLabel.setObjectName(_fromUtf8("meaningLabel"))
        meaningEntry.meaningLabel.setWordWrap(True)
        meaningEntry.horizontalLayout_2.addWidget(meaningEntry.meaningLabel)
        self.verticalLayout.addWidget(meaningEntry)
        self.meanings.append(meaningEntry)
        
        meaningEntry.meaningButton.setText(_fromUtf8(meaning))
        meaningEntry.meaningLabel.setText(_fromUtf8(translation))
        
        QtCore.QObject.connect(meaningEntry.meaningButton, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.control.test("meaning button pressed = " + meaningEntry.meaningButton.text()))
        QtCore.QObject.connect(meaningEntry.meaningButton, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.control.wordMeanings(meaningEntry.meaningButton.text(), meaning_object))

        
        QtCore.QMetaObject.connectSlotsByName(meaningEntry)


    def clearMeanings(self):
        """ deletes meanings and then hides and destroys the object """
        for meaning in self.meanings:
            meaning.hide()
            meaning.destroy()
            self.meanings.remove(meaning)

