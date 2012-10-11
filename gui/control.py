'''
Created on 08/10/2012

@author: sebastien
'''
import bassic
from noj.db_interface import *
from noj.data_structures import *
from backend_stubs import *

class control(object):
    '''
    classdocs
    '''


    def __init__(self, gui):
        '''
        Constructor
        '''
        self.mode = ""
        self.gui = gui
        self._dbi = None

    @property
    def dbi(self):
        """Get the Database Interface lazily"""
        if self._dbi is None:
            self._dbi = DatabaseInterface('../sentence_library.db')
        return self._dbi
        
    def test(self, str):
        
        print str
        
    def search(self, str):
        print "a search for \"" + str + "\" was conducted"
        
        if (self.mode == "dictionary"):
            if (str):
                print dictionary_mode_search(str)
                
                self.gui.dictionaryWords.addEntry(dictionary_mode_search(str).__str__(), "blah")
                self.gui.dictionary_2.show()
                self.gui.DictionaryWordsScrollArea.hide()
                
            else:
                self.gui.dictionary_2.hide()
        else:    
            pass
        
            
    def lookUpMode(self, str):
        self.mode = "lookUp"
        self.gui.UEarea.show()
        self.gui.dictionary_2.hide()
        self.search(str)
        
    def dictionaryMode(self, str):
        self.mode = "dictionary"
        self.gui.dictionary_2.show()
        self.gui.UEarea.hide()
        self.search(str)
            
    def wordMeanings(self, str):
        print "button has been clicked linked to \"" +str+ "\" meaning"
        
        self.gui.DictionaryWordsScrollArea.show()
    
