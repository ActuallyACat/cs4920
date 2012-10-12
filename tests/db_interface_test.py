#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
from noj.db_interface import *
from noj.japanese_parser import *
from sample_entries_1 import *

class MyTest(unittest.TestCase):

    def setUp(self):
    """For each test case, setup a database."""
        unittest.TestCase.setUp(self)
        try:
            os.remove('test.db')
        except OSError as e:
            pass
        self.dbi = DatabaseInterface('test.db')
        self.dbi.load_schema()

    def testCreateLibrary(self):
    """Test if a new Library can be created"""
        lib_id = self.dbi.get_or_create_library_id('Test', 1)
        self.assertEqual(lib_id, 1)

    def testGetLibrary(self):
    """Test if a library can be retrieved"""
        lib_id = self.dbi.get_or_create_library_id('Test', 1)
        lib_id = self.dbi.get_or_create_library_id('Test2', 1)
        lib_id = self.dbi.get_or_create_library_id('Test', 1)
        self.assertEqual(lib_id, 1)

    def testCreateMorpheme(self):
    """Test if a Morpheme can be created"""
        morph_id = self.dbi.get_or_create_morpheme_id(u'は', 1)
        self.assertEqual(morph_id, 1)

    def testGetMorpheme(self):
    """Test if morpheme can be retrieved"""
        morph_id = self.dbi.get_or_create_morpheme_id(u'は', 1)
        morph_id = self.dbi.get_or_create_morpheme_id(u'を', 1)
        morph_id = self.dbi.get_or_create_morpheme_id(u'は', 2)
        morph_id = self.dbi.get_or_create_morpheme_id(u'は', 1)
        self.assertEqual(morph_id, 1)
        morph_id = self.dbi.get_or_create_morpheme_id(u'は', 2)
        self.assertEqual(morph_id, 3)

    def testCreateEntry(self):
    """Test if a new entry can be created"""
        lib_id = self.dbi.get_or_create_library_id('Test', 1)
        kana_id = self.dbi.get_or_create_morpheme_id(u'は', 15)
        entry_id = self.dbi.create_entry_id(lib_id, 1, kana_id)
        self.assertEqual(entry_id, 1)

    def testCreateEntryHasKanji(self):
    """Test if a new entry with kanji can be created"""
        lib_id = self.dbi.get_or_create_library_id('Test', 1)
        kana_id = self.dbi.get_or_create_morpheme_id(u'は', 15)
        kanji_id = self.dbi.get_or_create_morpheme_id(u'愛', 14)
        entry_id = self.dbi.create_entry_id(lib_id, 1, kana_id)
        entryhaskanji_id = self.dbi.create_entryhaskanji_id(
                           lib_id, kanji_id)
        self.assertEqual(entryhaskanji_id, 1)

    def testCreateMeaning(self):
    """Test if a meaning can be created"""
        lib_id = self.dbi.get_or_create_library_id('Test', 1)
        kana_id = self.dbi.get_or_create_morpheme_id(u'は', 15)
        kanji_id = self.dbi.get_or_create_morpheme_id(u'愛', 14)
        entry_id = self.dbi.create_entry_id(lib_id, 1, kana_id)
        meaning_id = self.dbi.create_meaning_id('meaning', entry_id)
        self.assertEqual(meaning_id, 1)

    def testCreateUsageExample(self):
    """Test if a usage example can be created"""
        ue_id = self.dbi.create_usage_example_id(
                'expression', 'meaning', 'reading', True)
        self.assertEqual(ue_id, 1)

    def testCreateMeaningHasUE(self):
    """Test if a meaning can be created that has an associated usage example"""
        lib_id = self.dbi.get_or_create_library_id('Test', 1)
        kana_id = self.dbi.get_or_create_morpheme_id(u'は', 15)
        kanji_id = self.dbi.get_or_create_morpheme_id(u'愛', 14)
        entry_id = self.dbi.create_entry_id(lib_id, 1, kana_id)
        meaning_id = self.dbi.create_meaning_id('meaning', entry_id)
        ue_id = self.dbi.create_usage_example_id(
                'expression', 'meaning', 'reading', True)
        h_id = self.dbi.create_meaninghasue_id(ue_id, meaning_id)
        self.assertEqual(h_id, 1)

    def testCreateUEPartOfLibrary(self):
    """Test if UE can be created as a part of a library"""
        lib_id = self.dbi.get_or_create_library_id('Test', 1)
        kana_id = self.dbi.get_or_create_morpheme_id(u'は', 15)
        kanji_id = self.dbi.get_or_create_morpheme_id(u'愛', 14)
        entry_id = self.dbi.create_entry_id(lib_id, 1, kana_id)
        meaning_id = self.dbi.create_meaning_id('meaning', entry_id)
        ue_id = self.dbi.create_usage_example_id(
                'expression', 'meaning', 'reading', True)
        self.dbi.create_meaninghasue_id(ue_id, meaning_id)
        l_id = self.dbi.create_uepartoflibrary_id(ue_id, lib_id)
        self.assertEqual(l_id, 1)

    def testCreateUEConsistsOf(self):
    """Test UE can be created with a library id, kana id, kanji id, entry id, meaning id and UE id"""
        lib_id = self.dbi.get_or_create_library_id('Test', 1)
        kana_id = self.dbi.get_or_create_morpheme_id(u'は', 15)
        kanji_id = self.dbi.get_or_create_morpheme_id(u'愛', 14)
        morph_id = self.dbi.get_or_create_morpheme_id(u'は', 1)
        entry_id = self.dbi.create_entry_id(lib_id, 1, kana_id)
        meaning_id = self.dbi.create_meaning_id('meaning', entry_id)
        ue_id = self.dbi.create_usage_example_id(
                'expression', 'meaning', 'reading', True)
        c_id = self.dbi.create_ueconsistsof_id(ue_id, morph_id, 3, 0)
        self.assertEqual(c_id, 1)

    def testImportEntry(self):
    """Test if entries can be imported"""
        lib_id = self.dbi.get_or_create_library_id('Test', 1)
        parser = JapaneseParser()
        for entry in SAMPLE_ENTRIES_1:
            self.dbi.import_entry_recursive(entry, lib_id, parser)
        #TODO: need select functions to retrieve fields

if __name__ == '__main__':
    unittest.main()
