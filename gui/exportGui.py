'''
Created on 12/10/2012

@author: sebastien
'''
from PyQt4 import QtCore, QtGui

class Ui_Export(QtGui.QDialog):
    """docstring for Ui_Export
    Exports usage example list
    """
    def __init__(self):
        super(Ui_Export, self).__init__()
        
    def getfile(self):
        fname = QtGui.QFileDialog.getSaveFileName(self, "choose a file to export too")
        return fname
