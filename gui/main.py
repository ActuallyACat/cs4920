'''
Created on 24/09/2012

@author: sebastien
'''

import sys
from PySide import QtGui, QtCore
import bassic, control




if __name__ == "__main__":
    control = control.control()
    bassic.new(control)