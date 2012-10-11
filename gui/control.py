#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 08/10/2012

@author: sebastien
'''
import bassic, importGui
from noj.db_interface import *
from noj.data_structures import *
from noj.ue_exporter import *
from backend_stubs import *

class control(object):
    '''
    classdocs
    '''


    def __init__(self, gui=""):
        self.mode = ""
        self.gui = gui
        self._dbi = None
        self.importing = False
        
    def addGui(self, gui):
        self.gui = gui

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
        self.gui.UEarea.show()
        self.gui.dictionary_2.hide()
        self.search(str)
        
    def dictionaryMode(self, str):
        self.mode = "dictionary"
        self.gui.dictionary_2.show()
        self.gui.UEarea.hide()
        self.search(str)
            

    def wordMeanings(self, str, meaning):
        #print "button has been clicked linked to \"" +str+ "\" meaning"
        print meaning
        self.gui.DictionaryWordsScrollArea.clearSentences()
        for ue in meaning.usage_examples:
            self.gui.DictionaryWordsScrollArea.addSentence(ue.expression, ue.meaning, 9.99, ue)
        
        self.gui.DictionaryWordsScrollArea.show()

    def export(self):
        print "export button was pressed"
        if (self.mode == "dictionary"):
            ue_list = self.gui.DictionaryWordsScrollArea.getSentences()
        else:
            ue_list = self.gui.UEarea.getSentences()
        exporter = UEExporter(ue_list)
        exporter.export('exported_sentences.txt')
    
    def importButton(self):
        if self.importing == True:
            return
        
        self.importing = True
        importWindow = importGui.Ui_Import()
        importWindow.setText("Importing From: " + "...")
        importWindow.show()
        fileName = importWindow.getFile()
        importWindow.setText("Importing From: " + fileName)
        
        i = 0
        while i <= 100000:
            importWindow.setProgress(i/1000)
            i = i+1
            print i/1000
            
        self.importing = False


if __name__ == "__main__":
    control = control()
    bassic.new(control)