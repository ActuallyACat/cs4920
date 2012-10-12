#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 08/10/2012

@author: sebastien
'''
import bassic, importGui, exportGui
from noj.db_interface import *
from noj.data_structures import *
from noj.ue_exporter import *
from noj.ue_library_importer import *
from backend_stubs import *
import os.path

class control(object):
    '''
    classdocs
    '''


    def __init__(self, gui=""):
        self.mode = ""
        if gui:
            self.gui = gui
            self.guiStartUp()
        self._dbi = None
        self.importing = False
        
    def addGui(self, gui):
        self.gui = gui
        self.guiStartUp()
    
    def guiStartUp(self):
        pass

    @property
    def dbi(self):
        """Get the Database Interface lazily"""
        if self._dbi is None:
            self._dbi = DatabaseInterface('../sentence_library.db')
        return self._dbi

    def test(self, str):
        pass
        #print str
        
    def search(self, str):
        print "a search for \"" + str + "\" was conducted"
        
        if (self.mode == "dictionary"):
            if (str):
                list_of_entries = dictionary_mode_search(str)
                #self.gui.dictionaryWords.addEntry(dictionary_mode_search(str).__str__(), "blah")
                #print list_of_entries
                self.gui.dictionaryWords.clearMeanings()
                for entry in list_of_entries:
                    print entry
                    if entry.kanji != [u'']:
                        button_text = u"{} [{}]".format(entry.kana, 
                                entry.kanji_string())
                        print "kanji=".format(repr(entry.kanji))
                    else:
                        button_text = u"{}".format(entry.kana)

                    for meaning in entry.meanings:
                        self.gui.dictionaryWords.addMeaning(
                                button_text, meaning.meaning, meaning)
                self.gui.dictionary_2.show()
                self.gui.DictionaryWordsScrollArea.hide()
                
            else:
                self.gui.dictionary_2.hide()
        else:    
            self.gui.UEarea.clearSentences()
            if (str):
                list_of_ues = lookup_mode_search(str)
                for ue in list_of_ues:
                    print ue
                    self.gui.UEarea.addSentence(
                            ue.expression, ue.meaning, 9.99, ue)
                    #if entry.kanji != [u'']:
                        #button_text = u"{} [{}]".format(entry.kana, 
                                #entry.kanji_string())
                        #print "kanji=".format(repr(entry.kanji))
                    #else:
                        #button_text = u"{}".format(entry.kana)

                    #for meaning in entry.meanings:
                        #self.gui.dictionaryWords.addMeaning(
                                #button_text, meaning.meaning, meaning)
                #self.gui.dictionary_2.show()
                #self.gui.DictionaryWordsScrollArea.hide()
                
            #else:
                #self.gui.dictionary_2.hide()
        
            
    def lookUpMode(self, str):
        self.mode = "lookUp"
        self.search(str)
        self.gui.listMode()
        
        #names = ["hello","harry"]
        #self.gui.scrollAreaLists.populateUEs(names)
        
    def dictionaryMode(self, str):
        self.mode = "dictionary"
        self.search(str)
        self.gui.dictionaryMode()
            

    def wordMeanings(self, str, meaning):
        #print "button has been clicked linked to \"" +str+ "\" meaning"
        print meaning
        self.gui.DictionaryWordsScrollArea.clearSentences()
        for ue in meaning.usage_examples:
            self.gui.DictionaryWordsScrollArea.addSentence(ue.expression, ue.meaning, 9.99, ue)
        
        self.gui.DictionaryWordsScrollArea.show()
        self.gui.dictionaryModeList()

    def export(self):
        print "export button was pressed"
        if (self.mode == "dictionary"):
            ue_list = self.gui.DictionaryWordsScrollArea.getSentences()
        else:
            ue_list = self.gui.UEarea.getSentences()
        exporter = UEExporter(ue_list)
        exporter.export(exportGui.Ui_Export().getfile())
    
    def importButton(self):
        if self.importing == True:
            return
        
        self.importing = True
        importWindow = importGui.Ui_Import()
        importWindow.setText("Importing From: " + "...")
        importWindow.show()
        
        fileName = importWindow.getFile()
        importWindow.setText("Importing From: " + str(fileName))
        dictDir = os.path.abspath(os.path.join(str(fileName), 
                                  os.path.pardir))
        print dictDir
        

        importer = LibraryImporter(dictDir, self.dbi)
        importer.set_library('WADAI5')

        for progress in importer.import_progress():
            print progress
            importWindow.setProgress(progress.percent())

        #i = 0
        #while i <= 100000:
            #importWindow.setProgress(i/1000)
            #i = i+1
            #print i/1000
            
        self.importing = False
        
    def newWordList(self, name):
        print name
        #name is what the user has chosen for this list to be called
        self.gui.addListToComboBox(name)
    
    def newUEList(self, name):
        #name is what the user has chosen for this list to be called
        self.gui.addListToComboBox(name)
        
    def addToList(self, listName):
        #if the user selects a list, then presses save too.
        print listName
        
    def viewList(self, listName):
        print listName
        self.mode = "lookUp"
        self.gui.pushButtonLookUp.setEnabled(True)
        self.gui.pushButtonDictionary.setEnabled(True)


if __name__ == "__main__":
    control = control()
    bassic.new(control)
