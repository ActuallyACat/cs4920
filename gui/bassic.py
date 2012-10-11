# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bassic.ui'
#
# Created: Mon Oct  8 18:11:06 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import control, list, meaningArea, ue, scrollSentences

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, control):
        self.control = control
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(639, 411)
        self.centralwidget = QtGui.QWidget(MainWindow)
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
        self.scrollAreaLists = QtGui.QScrollArea(self.leftPane)
        self.scrollAreaLists.setFrameShape(QtGui.QFrame.StyledPanel)
        self.scrollAreaLists.setFrameShadow(QtGui.QFrame.Sunken)
        self.scrollAreaLists.setLineWidth(1)
        self.scrollAreaLists.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollAreaLists.setWidgetResizable(True)
        self.scrollAreaLists.setObjectName(_fromUtf8("scrollAreaLists"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 205, 242))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.ListUENewButton = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.ListUENewButton.setObjectName(_fromUtf8("ListUENewButton"))
        self.gridLayout.addWidget(self.ListUENewButton, 0, 0, 1, 1)
        self.ListWordNewButton = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.ListWordNewButton.setObjectName(_fromUtf8("ListWordNewButton"))
        self.gridLayout.addWidget(self.ListWordNewButton, 2, 0, 1, 1)
        
        self.List = QtGui.QWidget(self.scrollAreaWidgetContents_2)
        
        #add the lists code to a list widget
        list.Ui_List().setupUi(self.List)
        
        self.List.setObjectName(_fromUtf8("List"))
        self.gridLayout.addWidget(self.List, 1, 0, 1, 1)
        self.scrollAreaLists.setWidget(self.scrollAreaWidgetContents_2)
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
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem)
        self.verticalLayout_10.addWidget(self.exportArea)
        self.horizontalLayout_2.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 639, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuTitle = QtGui.QMenu(self.menubar)
        self.menuTitle.setObjectName(_fromUtf8("menuTitle"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionImport = QtGui.QAction(MainWindow)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuTitle.addAction(self.actionExit)
        self.menuOptions.addAction(self.actionSettings)
        self.menuOptions.addAction(self.actionImport)
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuTitle.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        
        self.actionImport.triggered.connect(lambda: control.importButton())

        self.retranslateUi(MainWindow)
        #button connection time
        QtCore.QObject.connect(self.pushButtonDictionary, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.control.test("dictionary mode"))
        QtCore.QObject.connect(self.pushButtonLookUp, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.control.test("lookup mode"))

        QtCore.QObject.connect(self.pushButtonDictionary, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.control.dictionaryMode(self.searchInput.text()))
        QtCore.QObject.connect(self.pushButtonLookUp, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.control.lookUpMode(self.searchInput.text()))

        QtCore.QObject.connect(self.ListUENewButton, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.control.test("new ue list button"))
        QtCore.QObject.connect(self.ListWordNewButton, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.control.test("new word list button"))
        
        QtCore.QObject.connect(self.searchButton, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.control.test("search button"))
        QtCore.QObject.connect(self.searchButton, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.control.search(self.searchInput.text()))
        QtCore.QObject.connect(self.searchInput, QtCore.SIGNAL(_fromUtf8("returnPressed()")), lambda: self.control.search(self.searchInput.text()))
        QtCore.QObject.connect(self.exportButton, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.control.export())

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.control.lookUpMode("")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDictionary.setText(QtGui.QApplication.translate("MainWindow", "Dictionary", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonLookUp.setText(QtGui.QApplication.translate("MainWindow", "Look up", None, QtGui.QApplication.UnicodeUTF8))
        self.ListUENewButton.setText(QtGui.QApplication.translate("MainWindow", "New UE List", None, QtGui.QApplication.UnicodeUTF8))
        self.ListWordNewButton.setText(QtGui.QApplication.translate("MainWindow", "New Word List", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.dictionary_2.setProperty("mode_type", QtGui.QApplication.translate("MainWindow", "TEXT", None, QtGui.QApplication.UnicodeUTF8))
        self.exportButton.setText(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTitle.setTitle(QtGui.QApplication.translate("MainWindow", "title", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOptions.setTitle(QtGui.QApplication.translate("MainWindow", "options", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "about", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("MainWindow", "help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "about", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setText(QtGui.QApplication.translate("MainWindow", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))


def new(control):
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    control.addGui(ui)
    ui.setupUi(MainWindow, control)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    control = control.control()
    new(control)
    
