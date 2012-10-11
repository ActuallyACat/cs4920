'''
Created on 11/10/2012

@author: sebastien
'''
            
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
            
            
class Ui_ScrollArea(QtGui.QScrollArea):
    def __init__(self, parent):
        super(Ui_ScrollArea, self).__init__(parent)
        self.setupUi()
        
    def setupUi(self):
        #self.setGeometry(QtCore.QRect(20, 60, 350, 178))
        self.setWidgetResizable(True)
        self.setObjectName(_fromUtf8("DictionaryWordsScrollArea"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        #self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 332, 307))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        
        self.sentences = []
        
        self.spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(self.spacerItem)
        self.setWidget(self.scrollAreaWidgetContents_3)

        QtCore.QMetaObject.connectSlotsByName(self)
        
        #self.addSentence("tets", "tes", "0.67")
        #self.addSentence("tets", "tesewfewfewg", "0.67")
        #self.addSentence("trsgrsets", "errggergrsges", "0.67")
        #self.addSentence("trggets", "trggrgsrgsrgrgrggres", "0.67")


    def addSentence(self, meaning, translation, score):
        
        self.verticalLayout_5.removeItem(self.spacerItem)
        temp = QtGui.QWidget(self.scrollAreaWidgetContents_3)
        
        temp.meaning = meaning
        temp.translation = translation
        temp.score = score
        
        temp.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        temp.setObjectName(_fromUtf8("example1"))
        temp.horizontalLayout = QtGui.QHBoxLayout(temp)
        temp.horizontalLayout.setMargin(0)
        temp.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        temp.widget_2 = QtGui.QWidget(temp)
        temp.widget_2.setObjectName(_fromUtf8("widget_2"))
        temp.horizontalLayout_5 = QtGui.QHBoxLayout(temp.widget_2)
        temp.horizontalLayout_5.setMargin(0)
        temp.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        temp.label_2 = QtGui.QLabel(temp.widget_2)
        temp.label_2.setObjectName(_fromUtf8("label_2"))
        temp.horizontalLayout_5.addWidget(temp.label_2)
        temp.horizontalLayout.addWidget(temp.widget_2)
        temp.widget = QtGui.QWidget(temp)
        temp.widget.setObjectName(_fromUtf8("widget"))
        temp.verticalLayout = QtGui.QVBoxLayout(temp.widget)
        temp.verticalLayout.setMargin(0)
        temp.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        temp.example1sentence = QtGui.QLabel(temp.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        temp.example1sentence.setPalette(palette)
        temp.example1sentence.setAutoFillBackground(False)
        temp.example1sentence.setWordWrap(True)
        temp.example1sentence.setObjectName(_fromUtf8("example1sentence"))
        temp.verticalLayout.addWidget(temp.example1sentence)
        temp.example1translation = QtGui.QLabel(temp.widget)
        temp.example1translation.setWordWrap(False)
        temp.example1translation.setObjectName(_fromUtf8("example1translation"))
        temp.verticalLayout.addWidget(temp.example1translation)
        temp.horizontalLayout.addWidget(temp.widget)
        
        temp.spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        temp.horizontalLayout.addItem(temp.spacerItem)

        temp.line = QtGui.QFrame(self.scrollAreaWidgetContents_3)
        temp.line.setFrameShape(QtGui.QFrame.HLine)
        temp.line.setFrameShadow(QtGui.QFrame.Sunken)
        temp.line.setObjectName(_fromUtf8("line"))
        temp.verticalLayout.addWidget(temp.line)
        
        temp.label_2.setText(_fromUtf8(str(score)))
        temp.example1sentence.setText(_fromUtf8(meaning))
        temp.example1translation.setText(_fromUtf8(translation))
        
        self.verticalLayout_5.addWidget(temp)
        self.sentences.append(temp)
        
        self.verticalLayout_5.addItem(self.spacerItem)
        
    def clearSentences(self):
        while len(self.sentences) > 0:
            sentence = self.sentences.pop()
            sentence.hide()
            sentence.destroy()
            
    def getSentences(self):
        temp = []
        for sentence in self.sentences:
            temp.append(sentence.meaning)
            
        return temp
            
