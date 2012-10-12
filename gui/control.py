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
from settingsGui import *
import os.path

class control(object):
    '''docstring for control
    
	Control is our controller interface between our backend and frontend GUI.
	
	It initiates the GUI and has the key functions of searching, dictionary, lookup modes.
    '''


    def __init__(self, gui=""):
	"""starts initial GUI"""
        self.mode = ""
        if gui:
            self.gui = gui
            self.guiStartUp()
        self._dbi = None
        self.importing = False
        self.user_ue_lists = dict()
        
    def addGui(self, gui):
	"""starts other specificed GUI elements"""
        self.gui = gui
        self.guiStartUp()
    
    def guiStartUp(self):
        #pass
        user_ue_lists = get_user_ue_lists()
        names = list()
        for ue_list in user_ue_lists:
            names.append(ue_list.name)
            self.gui.addListToComboBox(ue_list.name)
            self.user_ue_lists[ue_list.name] = ue_list
        #names = ["hello","harry"]
        self.gui.scrollAreaLists.populateUEs(names)
        #for n in names:
            #self.gui.addListToComboBox(n)

    @property
    def dbi(self):
        """Get the Database Interface lazily"""
        if self._dbi is None:
            self._dbi = DatabaseInterface('../sentence_library.db')
        return self._dbi

    def test(self, str):
        pass
        #print str
        
    def search(self, string):
	"""docstring for search
		
		Search has 2 different functions: lookup and dictionary
		
		For dictionary search = it searches for entries and their assocatied meanings that correspond with the search string
		For lookup search = it searches for usages examples that correspond with the search string
	"""
        string = unicode(string)
        print "a search for \"" + string.encode('utf-8') + "\" was conducted"
        
        if (self.mode == "dictionary"):
            if (string):
                list_of_entries = dictionary_mode_search(string)
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
            print repr(string)
            if (string):
                list_of_ues = self.dbi.lookup_mode_search(string)
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
	"""change to look up mode"""
        self.mode = "lookUp"
        self.search(str)
        self.gui.listMode()
        
        #names = ["hello","harry"]
        #self.gui.scrollAreaLists.populateUEs(names)
        
    def dictionaryMode(self, str):
	"""change to dictionary mode"""
        self.mode = "dictionary"
        self.search(str)
        self.gui.dictionaryMode()
        

    def wordMeanings(self, str, meaning):
	"""show meanings for dictionary search terms"""
        #print "button has been clicked linked to \"" +str+ "\" meaning"
        print meaning
        self.gui.DictionaryWordsScrollArea.clearSentences()
        for ue in meaning.usage_examples:
            self.gui.DictionaryWordsScrollArea.addSentence(ue.expression, ue.meaning, 9.99, ue)
        
        self.gui.DictionaryWordsScrollArea.show()
        self.gui.dictionaryModeList()

    def export(self):
	"""export function exports a generated UE list"""
        print "export button was pressed"
        if (self.mode == "dictionary"):
            ue_list = self.gui.DictionaryWordsScrollArea.getSentences()
        else:
            ue_list = self.gui.UEarea.getSentences()
        exporter = UEExporter(ue_list)
        exporter.export(exportGui.Ui_Export().getfile())
    
    def importButton(self):
	"""import function to import in libraries.
	
		Visually there will be a progress bar displaying completion percentage
	"""
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
        importWindow.setText("Importing From: " + dictDir)
        

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
	"""docstring for newWordList = creates a new word list"""
        print name
        #name is what the user has chosen for this list to be called
        self.gui.addListToComboBox(name)
    
    def newUEList(self, name):
	"""docstring for newUEList = creates a new usage example list"""
        #name is what the user has chosen for this list to be called
        # user manually add
        self.gui.addListToComboBox(name)
        user_ue_list = UsageExampleList(str(name))
        self.user_ue_lists[str(name)] = user_ue_list
        user_ue_list.save()
        
    def addToList(self, listName):
        #if the user selects a list, then presses save too.
        # add ues to list
        # todo
        if (self.mode == "dictionary"):
            ue_list = self.gui.DictionaryWordsScrollArea.getSentences()
        else:
            ue_list = self.gui.UEarea.getSentences()
        user_ue_list = self.user_ue_lists[str(listName)]
        user_ue_list.add_usage_examples(ue_list)
        user_ue_list.save()
        print listName
        
    def viewList(self, listName):
        print listName
        
        #self.mode = "lookUp"
        self.lookUpMode("")
        #self.mode = "viewMode"

        self.gui.pushButtonLookUp.setEnabled(True)
        self.gui.pushButtonDictionary.setEnabled(True)
        self.gui.UEarea.clearSentences()

        user_ue_list = self.user_ue_lists[str(listName)]
        for ue in user_ue_list.ue_list:
            print ue
            self.gui.UEarea.addSentence(
                    ue.expression, ue.meaning, 1.99, ue)
        
    def settingsWindow(self):
        settingsControler = settingsControl()
        settingsGui = Ui_settings(settingsControler)
        settingsGui.show()


if __name__ == "__main__":
    control = control()
    bassic.new(control)
