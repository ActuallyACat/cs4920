# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bassic.ui'
#
# Created: Mon Oct  8 18:11:06 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import control, list, meaningArea, ue, scrollSentences, list

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self, control):
        super(Ui_MainWindow, self).__init__()
        control.addGui(self)
        self.setupUi(control)
    def setupUi(self, control):
        self.control = control
        self.setObjectName(_fromUtf8("MainWindow"))
        self.resize(639, 411)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setMinimumSize(QtCore.QSize(300, 300))
        self.splitter.setLineWidth(4)
        self.splitter.setMidLineWidth(1)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.leftPane = QtGui.QWidget(self.splitter)
        self.leftPane.setMinimumSize(QtCore.QSize(150, 0))
        self.leftPane.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.leftPane.setObjectName(_fromUtf8("leftPane"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.leftPane)
        self.verticalLayout_9.setMargin(0)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.ModePane = QtGui.QWidget(self.leftPane)
        self.ModePane.setMinimumSize(QtCore.QSize(50, 100))
        self.ModePane.setObjectName(_fromUtf8("ModePane"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.ModePane)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.modePaneButtons = QtGui.QWidget(self.ModePane)
        self.modePaneButtons.setObjectName(_fromUtf8("modePaneButtons"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.modePaneButtons)
        self.verticalLayout_11.setMargin(0)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.pushButtonDictionary = QtGui.QPushButton(self.modePaneButtons)
        self.pushButtonDictionary.setObjectName(_fromUtf8("pushButtonDictionary"))
        self.verticalLayout_11.addWidget(self.pushButtonDictionary)
        self.pushButtonLookUp = QtGui.QPushButton(self.modePaneButtons)
        self.pushButtonLookUp.setObjectName(_fromUtf8("pushButtonLookUp"))
        self.verticalLayout_11.addWidget(self.pushButtonLookUp)
        self.horizontalLayout_4.addWidget(self.modePaneButtons)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_9.addWidget(self.ModePane)
        self.scrollAreaLists = list.Ui_Lists(self.leftPane, self.control)
        self.scrollAreaLists.setObjectName(_fromUtf8("scrollAreaLists"))
        
        self.verticalLayout_9.addWidget(self.scrollAreaLists)
        self.rightPane = QtGui.QWidget(self.splitter)
        self.rightPane.setBaseSize(QtCore.QSize(0, 0))
        self.rightPane.setObjectName(_fromUtf8("rightPane"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.rightPane)
        self.verticalLayout_10.setMargin(0)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.searchArea = QtGui.QWidget(self.rightPane)
        self.searchArea.setMinimumSize(QtCore.QSize(150, 50))
        self.searchArea.setObjectName(_fromUtf8("searchArea"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.searchArea)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.searchInput = QtGui.QLineEdit(self.searchArea)
        self.searchInput.setObjectName(_fromUtf8("searchInput"))
        self.horizontalLayout_3.addWidget(self.searchInput)
        self.searchButton = QtGui.QPushButton(self.searchArea)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.horizontalLayout_3.addWidget(self.searchButton)
        self.verticalLayout_10.addWidget(self.searchArea)
        self.UEarea = scrollSentences.Ui_ScrollArea(self.rightPane)
        self.UEarea.setObjectName(_fromUtf8("UEarea"))
        self.verticalLayout_10.addWidget(self.UEarea)

        
        self.dictionary_2 = QtGui.QWidget(self.rightPane)
        self.dictionary_2.setObjectName(_fromUtf8("dictionary_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dictionary_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        
        #this stores dictionary words
        self.dictionaryWords = meaningArea.Ui_meaningArea(self.dictionary_2, self.control)
        self.dictionaryWords.setMinimumSize(QtCore.QSize(100, 100))
        self.dictionaryWords.setObjectName(_fromUtf8("dictionaryWords"))
        self.verticalLayout_2.addWidget(self.dictionaryWords)
        self.DictionaryWordsScrollArea = scrollSentences.Ui_ScrollArea(self.dictionary_2)
        self.DictionaryWordsScrollArea.setObjectName(_fromUtf8("DictionaryWordsScrollArea"))
        self.verticalLayout_2.addWidget(self.DictionaryWordsScrollArea)
        self.verticalLayout_10.addWidget(self.dictionary_2)
        
        self.rightPaneSpacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(self.rightPaneSpacerItem)
        
        self.saveArea = QtGui.QWidget(self.rightPane)
        self.saveArea.setObjectName(_fromUtf8("saveArea"))
        self.saveAreahorizontalLayout_6 = QtGui.QHBoxLayout(self.saveArea)
        self.saveAreahorizontalLayout_6.setMargin(0)
        self.saveAreahorizontalLayout_6.setObjectName(_fromUtf8("saveAreahorizontalLayout_6"))
        saveAreaspacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.saveAreahorizontalLayout_6.addItem(saveAreaspacerItem3)
        self.comboBoxListLabel = QtGui.QLabel(self.saveArea)
        self.comboBoxListLabel.setObjectName(_fromUtf8("comboBoxListLabel"))
        self.saveAreahorizontalLayout_6.addWidget(self.comboBoxListLabel)
        self.comboBoxList = QtGui.QComboBox(self.saveArea)
        self.comboBoxList.setObjectName(_fromUtf8("comboBox"))
        self.saveAreahorizontalLayout_6.addWidget(self.comboBoxList)
        self.saveAreaButton = QtGui.QPushButton(self.saveArea)
        self.saveAreaButton.setObjectName(_fromUtf8("saveAreaButton"))
        self.saveAreaButton.setDisabled(True)
        self.saveAreahorizontalLayout_6.addWidget(self.saveAreaButton)
        self.verticalLayout_10.addWidget(self.saveArea)
        
        self.exportArea = QtGui.QWidget(self.rightPane)
        self.exportArea.setObjectName(_fromUtf8("exportArea"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.exportArea)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.exportButton = QtGui.QPushButton(self.exportArea)
        self.exportButton.setObjectName(_fromUtf8("exportButton"))
        self.horizontalLayout_6.addWidget(self.exportButton)
        self.verticalLayout_10.addWidget(self.exportArea)
        
        self.horizontalLayout_2.addWidget(self.splitter)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 639, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuTitle = QtGui.QMenu(self.menubar)
        self.menuTitle.setObjectName(_fromUtf8("menuTitle"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.setMenuBar(self.menubar)
        self.actionHelp = QtGui.QAction(self)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionAbout = QtGui.QAction(self)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionSettings = QtGui.QAction(self)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionImport = QtGui.QAction(self)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.actionExit = QtGui.QAction(self)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuTitle.addAction(self.actionExit)
        self.menuOptions.addAction(self.actionSettings)
        self.menuOptions.addAction(self.actionImport)
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuTitle.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        
        self.actionHelp.triggered.connect(lambda: control.test("help"))
        self.actionAbout.triggered.connect(lambda: control.test("about"))
        self.actionSettings.triggered.connect(lambda: control.test("settings"))
        self.actionImport.triggered.connect(lambda: control.importButton())
        self.actionExit.setShortcut('Ctrl+I')
        self.actionExit.triggered.connect(QtGui.qApp.quit)
        self.actionExit.setShortcut('Ctrl+Q')
    

        self.retranslateUi()
        #button connection time
        QtCore.QObject.connect(self.pushButtonDictionary, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.control.test("dictionary mode"))
        QtCore.QObject.connect(self.pushButtonLookUp, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.control.test("lookup mode"))

        QtCore.QObject.connect(self.pushButtonDictionary, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.control.dictionaryMode(self.searchInput.text()))
        QtCore.QObject.connect(self.pushButtonLookUp, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.control.lookUpMode(self.searchInput.text()))
        
        QtCore.QObject.connect(self.searchButton, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.control.test("search button"))
        QtCore.QObject.connect(self.searchButton, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.control.search(self.searchInput.text()))
        QtCore.QObject.connect(self.searchInput, QtCore.SIGNAL(_fromUtf8("returnPressed()")), lambda: self.control.search(self.searchInput.text()))
        QtCore.QObject.connect(self.saveAreaButton, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.control.addToList(self.comboBoxList.currentText()))
        QtCore.QObject.connect(self.exportButton, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.control.export())

        QtCore.QMetaObject.connectSlotsByName(self)
        self.control.lookUpMode("")

    def retranslateUi(self, ):
        self.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDictionary.setText(QtGui.QApplication.translate("MainWindow", "Dictionary", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonLookUp.setText(QtGui.QApplication.translate("MainWindow", "Look up", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.dictionary_2.setProperty("mode_type", QtGui.QApplication.translate("MainWindow", "TEXT", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxListLabel.setText(QtGui.QApplication.translate("MainWindow", "Add all to List", None, QtGui.QApplication.UnicodeUTF8))
        self.saveAreaButton.setText(QtGui.QApplication.translate("MainWindow", "Add to List", None, QtGui.QApplication.UnicodeUTF8))
        self.exportButton.setText(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTitle.setTitle(QtGui.QApplication.translate("MainWindow", "title", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOptions.setTitle(QtGui.QApplication.translate("MainWindow", "options", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "about", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("MainWindow", "help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "about", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setText(QtGui.QApplication.translate("MainWindow", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))

    def addListToComboBox(self, text):
        self.comboBoxList.addItem(_fromUtf8(text))
        self.saveAreaButton.setEnabled(True)
        
    def dictionaryMode(self):
        self.dictionary_2.show()
        self.UEarea.hide()
        self.DictionaryWordsScrollArea.hide()
        self.pushButtonDictionary.setDisabled(True)
        self.pushButtonLookUp.setEnabled(True)
        
        
        self.verticalLayout_10.removeWidget(self.saveArea)
        self.verticalLayout_10.removeWidget(self.exportArea)
        self.verticalLayout_10.addItem(self.rightPaneSpacerItem)
        self.verticalLayout_10.addWidget(self.saveArea)
        self.verticalLayout_10.addWidget(self.exportArea)
        
        
    def dictionaryModeList(self):
        self.verticalLayout_10.removeItem(self.rightPaneSpacerItem)
        
    def listMode(self):
        self.UEarea.show()
        self.dictionary_2.hide()
        self.pushButtonLookUp.setDisabled(True)
        self.pushButtonDictionary.setEnabled(True)
        
        self.verticalLayout_10.removeItem(self.rightPaneSpacerItem)

def new(control):
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = Ui_MainWindow(control)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    control = control.control()
    new(control)
    
