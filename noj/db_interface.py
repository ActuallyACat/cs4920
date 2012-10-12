#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import os
#from noj.data_structures import *
import noj.data_structures

SCHEMA_PATH = '../schema.sql'

class DatabaseInterface(object):
    """Performs SQL operations to the DB.
    
    Remember to commit() after performing a DB operation.
    """
    def __init__(self, db_path):
        self.db_path = db_path
        self.lib_type_ids = dict()
        self.open_()

    def open_(self):
        """Opens connection to database
        """
        self.con = lite.connect(self.db_path)
        self.cur = self.con.cursor()
        print("Connection Established")    

    def commit(self):
        self.con.commit()

    def close(self):
        """Closes connection to database
        """
        self.con.close()

    def reset_database(self):
        """Delete the DB and reload the schema.
        """
        self.close()
        try:
            os.remove(self.db_path)
        except OSError as e:
            pass
        self.open_()
        self.load_schema()
        self.commit()

    def load_schema(self, schema_path=SCHEMA_PATH):
        """Load schema SQL into DB from SQL file"""
        with open(schema_path, 'rt') as f:
            schema = f.read()
        self.con.executescript(schema)
      
    def get_or_create_library_id(self, name, type_):
        """Returns id of Library with the given name.
        
        Creates a tuple for the library if it doesn't exist,
        otherwise finds the existing tuple. 
        """
        try:
            self.cur.execute("INSERT INTO Libraries VALUES(null,?,?)",
                        (name, type_))
            lib_id = self.cur.lastrowid
        except lite.IntegrityError as e:
            self.cur.execute("select id from Libraries as L where L.name = ?",
                    [name])    
            lib_id = self.cur.fetchone()[0]
        return lib_id

    def get_or_create_morpheme_id(self, morph_str, morph_type, 
                                  count=None):
        """Returns id of Morpheme with the name and type.
        
        Creates a tuple for the Morphemes if it doesn't exist,
        otherwise finds the existing tuple. 
        """
        try:
            self.cur.execute("INSERT INTO Morphemes VALUES(null,?,?,?)",
                        (morph_str, morph_type, count))
            morph_id = self.cur.lastrowid
        except lite.IntegrityError as e:
            self.cur.execute("select id from Morphemes as M where M.morpheme = ? and M.morphemeType = ?",
                    (morph_str, morph_type))
            morph_id = self.cur.fetchone()[0]
        return morph_id
    
    def create_entry_id(self, lib_id, entry_number, kana_id):
        """Create tuple for Entries and return the id."""
        self.cur.execute("INSERT INTO Entries VALUES(null,?,?,?)",
                    (lib_id, entry_number, kana_id))
        return self.cur.lastrowid

    def create_entryhaskanji_id(self, entry_id, kanji_id):
        """Create tuple for EntryHasKanji and return the id."""
        self.cur.execute("INSERT INTO EntryHasKanji VALUES(?,?)",
                    (entry_id, kanji_id))
        return self.cur.lastrowid

    def create_meaning_id(self, meaning_str, entry_id):
        """Create tuple for Meanings and return the id."""
        self.cur.execute("INSERT INTO Meanings VALUES(null,?,?)",
                         (meaning_str, entry_id))
        return self.cur.lastrowid

    def create_usage_example_id(self, expression, meaning, reading, 
                                isSentence):
        """Create tuple for UsageExamples and return the id."""
        self.cur.execute("INSERT INTO UsageExamples VALUES(null,?,?,?,?)",
                         (expression, meaning, reading, isSentence))
        return self.cur.lastrowid

    def create_meaninghasue_id(self, ue_id, meaning_id):
        """Create tuple for MeaningHasUEs and return the id."""
        self.cur.execute("INSERT INTO MeaningHasUEs VALUES(?,?)",
                         (ue_id, meaning_id))
        return self.cur.lastrowid

    def create_uepartoflibrary_id(self, ue_id, lib_id):
        """Create tuple for UEPartOfLibrary and return the id."""
        self.cur.execute("INSERT INTO UEPartOfLibrary VALUES(?,?)",
                    (ue_id, lib_id))
        return self.cur.lastrowid

    def create_ueconsistsof_id(self, ue_id, morph_id, 
                               length, position):
        """Create tuple for UEConsistsOf and return the id."""
        self.cur.execute("INSERT INTO UEConsistsOf VALUES(?,?,?,?)",
                    (ue_id, morph_id, length, position))
        return self.cur.lastrowid

    def import_entry_recursive(self, entry, lib_id, parser):
        """Import entry and all its children into db."""
        #insert entry tuple
        kana_id = self.get_or_create_morpheme_id(entry.kana, 15)
        entry_id = self.create_entry_id(lib_id, entry.entry_number, 
                                       kana_id)
        #insert kanji tuples
        for kanji in entry.kanji:
            if kanji == '':
                continue
            kanji_id = self.get_or_create_morpheme_id(kanji, 14)
            self.create_entryhaskanji_id(entry_id, kanji_id)

        #insert meaning tuples
        for meaning in entry.meanings:
            meaning_id = self.create_meaning_id(meaning.meaning, 
                                               entry_id)
            #insert UE tuples
            for ue in meaning.usage_examples:
                ue_id = self.create_usage_example_id(
                        ue.expression, ue.meaning, None, True)
                self.create_meaninghasue_id(ue_id, meaning_id)
                self.create_uepartoflibrary_id(ue_id, lib_id)
                components = ue.get_components(parser)

                #insert morpheme tuples
                for component in components:
                    if component['base'] == '':
                        continue
                    morph_id = self.get_or_create_morpheme_id(
                               component['base'], component['type'], 
                               None)
                    self.create_ueconsistsof_id(ue_id, morph_id, 
                                               component['length'], 
                                               component['position'])


    def get_lib_type_id(self, type_name):
        """docstring for get_lib_type_id
        
        Returns the type for library"""
        if type_name not in self.lib_type_ids:
            try:
                con = lite.connect(self.db_path)
                with con:
                    cur = con.cursor() 
                    cur.execute("select id from LibraryTypes as L where L.type = ?",[type_name])    
                    self.lib_type_ids[type_name] = cur.fetchone()[0]
            except lite.Error as e:
                if con:
                    con.rollback()
                print "Error %s:" % e.args[0]
                sys.exit(1)
            except TypeError as e:
                raise KeyError("No tuple for '{}' in LibraryTypes".format(type_name))
        return self.lib_type_ids[type_name]

    def import_UE(self,UsageExample,Meaning):
        """docstring for import_UE
        
        imports usages examples into the DB
        """
        try:
            con = lite.connect(self.db_path)
            with con:
                cur = con.cursor()    
                cur.execute("INSERT INTO UsageExamples VALUES(null,?,?,?,?)",(UsageExample.meaning,UsageExample.expression,UsageExample.reading,UsageExample.sentence))
        except lite.Error, e:
            if con:
                con.rollback()
            print "Error %s:" % e.args[0]
            sys.exit(1)
 
    def searchUE_Dictionary(self,entry):
        """docstring for searchUE_Dictionary
        
        searches for the dictionary meaning for associated usage example through DB
        
        returns -> meanings, entries and entry IDs
        """
        try:
            con = lite.connect(self.db_path)
            with con:
                con.row_factory = lite.Row
                cur = con.cursor() 
                cur.execute("select meaning from Meanings as M, EntryHasMeanings as EM, Entries as E where E.id = EM.entry and M.id = EM.meaning and EM.entry =?",(entry.id))    
                rows = cur.fetchall()
                for row in rows:
                    print "%s" % (row["meaning"])
        except lite.Error, e:
            if con:
                con.rollback()
            print "Error %s:" % e.args[0]
            sys.exit(1)
 
                
    def searchUE_lookup(self,morpheme):
        """docstring for searchUE_lookup
        
        searches for usage examples from a word
        
        returns -> meanings, entries, usage examples, morphemes and morpheme IDs
        """
        try:
            con = lite.connect(self.db_path)
            with con:
                con.row_factory = lite.Row
                cur = con.cursor() 
                cur.execute("select UE.id as id, UE.expression as expression, UE.meaning as meaning from UsageExamples as UE, UEConsistsOf as UEC, Morphemes as M where UE.id = UEC.usageExample and UEC.morpheme = M.id and M.morpheme = ?",(morpheme))
                rows = cur.fetchall()
                for row in rows:
                    print "%s %s %s" % (row["id"], row["expression"], row["meaning"])
        except lite.Error, e:
            if con:
                con.rollback()
            print "Error %s:" % e.args[0]
            sys.exit(1)       
    
    def storeUE_list(self,user_list):
        """Create an UE or Word List assumes and object of type user_list is passed as argument"""
        try:
            con = lite.connect(self.db_path)
            with con:
                cur = con.cursor()    
                nameOfList = user_list.name 
                typeOfList = user_list.type
                cur.execute("INSERT INTO Lists VALUES(null,?,?)",(nameOfList,typeOfList))
        except lite.Error, e:
            if con:
                con.rollback()
            print "Error %s:" % e.args[0]
            sys.exit(1)
    
    def insert_elements(self,user_list,UsageExample):
        """Inserts Elements into the UE or Word List assumes an input arg of UsageExample & user_list Object"""
        try:
            con = lite.connect(self.db_path)
            with con:
                cur = con.cursor()    
                list_id = user_list.id
                UE_id = UsageExample.id        
                cur.execute("INSERT INTO UEPartOfList VALUES(?,?,'toLearn')",(list_id,UE_id))
        except lite.Error, e:
            if con:
                con.rollback()
            print "Error %s:" % e.args[0]
            sys.exit(1)
    
    def retrieveUE_list(self,nameOfList):
        "Retreives an UE List, args expected name of List"
        try:
            con = lite.connect(self.db_path)
            with con:
                con.row_factory = lite.Row
                cur = con.cursor() 
                cur.execute("select UE.id as id, UE.expression as expression, UE.meaning as meaning from UsageExamples as UE, UEPartOfList as UEL, List as L where UE.usageExample = UE.id and UEL.list = L.id and L.name = ?",(nameOfList))
                rows = cur.fetchall()
                for row in rows:
                    print "%s %s %s" % (row["id"], row["expression"], row["meaning"])
        except lite.Error, e:
            if con:
                con.rollback()
            print "Error %s:" % e.args[0]
            sys.exit(1)
  
    def get_infoUE(self,UsageExample):
        """Input arg is an UE Object"""
        try:
            con = lite.connect("sentence_library.db")
            with con:
                con.row_factory = lite.Row
                cur = con.cursor() 
                cur.execute("select * from UsageExamples as UE where UE.expression = ?",(UsageExample.expression))
                rows = cur.fetchall()
                for row in rows:
                    print "%s %s %s" % (row["id"], row["expression"], row["meaning"])
        except lite.Error, e:
            if con:
                con.rollback()
            print "Error %s:" % e.args[0]
            sys.exit(1)
    
    def get_UESource(self,UsageExample):
        try:
            con = lite.connect("sentence_library.db")
            with con:
                con.row_factory = lite.Row
                cur = con.cursor() 
                cur.execute("select L.name as source from Library as L, Entries as E, EntryHasMeanings as EM, MeaningHasUEs as MUE, UsageExamples as UE, Meanings as M where L.id = E.library and EM.entry = E.id and EM.meaning = M.id and M.id = MUE.meaning and MUE.usageExample = UE.id and UE.expression = ?",(UsageExample.expression))
                rows = cur.fetchall()
                for row in rows:
                    print "%s " % (row["source"])
        except lite.Error, e:
            if con:
                con.rollback()
            print "Error %s:" % e.args[0]
            sys.exit(1)
            
    def lookup_mode_search(self, string):
        lists = list() #create empty list
        con = lite.connect(self.db_path)
        with con:
            cur = con.cursor()
            #Returns id, expression, meaning, reading, isSentence
            cur.execute("SELECT * FROM usageExamples WHERE id IN " +
                            "(SELECT usageExample FROM UEConsistsOf WHERE morpheme IN "+
                                "(SELECT id FROM morphemes WHERE morpheme=?)"+
                            ")", [string]);
            rows = cur.fetchall()
            i = 0
            for row in rows:
                #Create list of usageExamples
                #create new usage example
                ue = noj.data_structures.UsageExample(row[1], row[2], row[3])
                #print ue
                lists.append(ue)
                i += 1
        return lists

    def dict_mode_search(self, string): 
        """
        #string is the morpheme
        TODO: Returns a list of DictionaryEntry entries (from data_structures.py)
        """
        entries = list()
        con = lite.connect(self.db_path)
        with con:
            cur1 = con.cursor()    
            cur1.execute("""
select ehk.entry from entryhaskanji ehk, morphemes m where m.morphemetype = 14 and ehk.kanji = m.id and m.morpheme=?
UNION
select e.id from entries e join morphemes m on e.kana = m.id where m.morpheme=?;
""", (string, string))
            rows1 = cur1.fetchall()    
            for row in rows1:
                entry_id = row[0]
                print entry_id
                cur1.execute("""
select e.id, e.number, k.morpheme, k2.morpheme from entries e join morphemes k on k.id = e.kana left outer join entryhaskanji ehk on ehk.entry = e.id left outer join morphemes k2 on k2.id = ehk.kanji where e.id = ?;
""", [entry_id])
                entry_rows = cur1.fetchall()
                kanji = list()
                for entry_row in entry_rows:
                    print entry_row
                    single_kanji = entry_row[3]
                    if single_kanji is None:
                        single_kanji = ''
                    kanji.append(single_kanji)
                    kana = entry_row[2]
                    entry_number = entry_row[1]
                entries.append(noj.data_structures.DictionaryEntry(kana, kanji, entry_number, id_=entry_id))
            return entries


    def get_meanings(self, entry_id):
        """Returns list of DictionaryMeaning for given entry id. """
        meanings = list()
        self.cur.execute("select id, meaning from Meanings where entry = ?", [entry_id])
        rows = self.cur.fetchall()    
        for idx, m in enumerate(rows):
            meanings.append(noj.data_structures.DictionaryMeaning(m[1], idx+1, m[0]))
        return meanings

    def get_usage_examples(self, meaning_id):
        """Returns list of UsageExample for given entry id. """
        usage_examples = list()
        self.cur.execute("select ue.id, ue.expression, ue.meaning from usageexamples ue join meaninghasues mhu on mhu.usageexample = ue.id where mhu.meaning = ?", [meaning_id])
        rows = self.cur.fetchall()    
        for idx, ue in enumerate(rows):
            usage_examples.append(noj.data_structures.UsageExample(ue[1], ue[2]))
        return usage_examples

if __name__ == '__main__':
    dbi = DatabaseInterface('sentence_library.db')
    #print dbi.lookup_mode_search(u'才能')
    #print dbi.lookup_mode_search(u'先生')
    #dbi.dict_mode_search(u'先生')
    #dbi.dict_mode_search(u'ああ')
    entries = dbi.dict_mode_search(u'まち')
    for e in entries:
        print e
        e.get_meanings(dbi)
