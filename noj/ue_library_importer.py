#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import re
import codecs
from japanese_parser import *
from data_structures import *
from db_interface import *
from kenkyusha5_dumper import *
from kenkyusha5_dump_converter import *
import sqlite3 as lite

re_header_line = re.compile(r'(\w+?): ?(.*)$')
re_entry = re.compile(r'^[^\t]')
re_entry_split = re.compile(r'^([^\t]*)\t([^\t]*)\t([^\t]*)\n')
re_meaning = re.compile(r'^\t[^\t]')
re_meaning_split = re.compile(r'^\t([^\t]*)\n')
re_ue = re.compile(r'^\t\t[^\t]')
re_ue_split = re.compile(r'^\t\t([^\t]*)\t([^\t]*)\n')

class LibraryImporter(object):
    """docstring for LibraryImporter
    Used to import user libraries into the program
    """
    def __init__(self, path, dbi):
        super(LibraryImporter, self).__init__()
        self.path = path # eg. path to epwing dict
        self.converted_path = None 
        #self.db_path = None 
        self.dbi = dbi

    #def set_db_path(self, db_path):
        #self.db_path = db_path

    def set_library(self, library_code):
        """docstring for set_library
        Sets the active library
        """
        self.library_code = library_code
        
    def prepare_library(self):
        """docstring for prepare
        Prepares library by dumping library from epwing format and then
        its put through a converter to ensure it can be stored in the 
        DB schema
        """
        if self.library_code == 'WADAI5':
            dumper = Kenkyusha5Dumper(self.path)
            dumper.dump('kenkyusha_dump')
            dump_converter = Kenkyusha5DumpConverter('kenkyusha_dump')
            self.converted_path = 'kenkyusha_converted'
            dump_converter.convert(self.converted_path)
    
    def import_progress(self):
        """docstring for import_progress
        Prints out the progress of importing a library into the DB
        """
        progress = ProgressPoint(1, 2, 0, 1)
        yield progress
        self.prepare_library()
        #dbi = DatabaseInterface(self.db_path)
        self.dbi.reset_database()
        importer = UELibraryImporter(self.converted_path)
        parser = JapaneseParser()
        lib_type = importer.type_
        if self.library_code == 'WADAI5':
            lib_id = self.dbi.get_or_create_library_id('Kenkyusha 5th', 1)
        total_num_entries = self.num_entries(self.converted_path)
        progress = ProgressPoint(2, 2, 0, total_num_entries)
        for idx, entry in enumerate(importer.entries()):
            progress.point = idx
            self.dbi.import_entry_recursive(entry, lib_id, parser)
            yield progress
        self.dbi.commit()

    def num_entries(self, fname):
        num_entries = 0
        with open(fname) as fh:
            for line in fh:
                if re_entry.match(line):
                    num_entries += 1
        return num_entries

class UELibraryImporter(object):
    """Imports usage example libraries
    Usage Example libraries are basically libraries full of sentences.
    This call helps by formatting the import file into a format that the is in line with the DB schema.
    """
    def __init__(self, file_, encoding='utf-8'):
        super(UELibraryImporter, self).__init__()
        self.fh = codecs.open(file_, 'r', encoding=encoding)
        self.name = ''
        self.type_ = CORPUS
        self.format_type = FORMAT_TABS
        self.process_headers()
        self.prev_line = self.fh.readline()
        self.library_code = None
        print self.name, self.type_, self.format_type


    def process_headers(self):
        """docstring for process_headers
        Determines what the headers are and labels them accordingly"""
        for line in self.fh:
            line = line.rstrip()
            if line == '':
                break
            m = re_header_line.match(line)
            if m:
                key = m.group(1)
                val = m.group(2)
                if key == 'NAME':
                    self.name = val
                elif key == 'TYPE':
                    if val.upper() == 'DICTIONARY':
                        self.type_ = DICTIONARY
                    else:
                        self.type_ == CORPUS
                elif key == 'FORMAT':
                    if val.upper() == 'TABS':
                        self.format_type = FORMAT_TABS

    def read_entry(self):
        """docstring for read_entry
        Reads in the lines from a list and parses them through the DB.
        It also checks if the entry is already in the DB.
        """
        lines = list()
        for line in self.fh:
            #print self.prev_line,
            lines.append(self.prev_line)
            self.prev_line = line
            if re_entry.match(line):
                break
        return self.parse_entry_lines(lines)

    def parse_entry_lines(self, lines):
        """docstring for parse_entry_lines
        Parses entry lines to the DB and check if meanings and usage examples 
        match the entry.
        """
        entry = None
        for line in lines:
            if re_entry.match(line):
                #print "entry", line,
                m = re_entry_split.match(line)
                entry = DictionaryEntry(m.group(1), m.group(2).split('|'), 
                                        m.group(3))
            elif re_meaning.match(line):
                #print "meaning", line,
                m = re_meaning_split.match(line)
                meaning_no = entry.num_meanings()+1
                meaning = DictionaryMeaning(m.group(1), meaning_no)
                entry.add_meaning(meaning)
                #print meaning
            elif re_ue.match(line):
                #print "ue", line,
                m = re_ue_split.match(line)
                ue = UsageExample(m.group(1), m.group(2))
                meaning.add_usage_example(ue)
                #print ue
        return entry

    def entries(self):
        entry = self.read_entry()
        while entry is not None:
            yield entry
            entry = self.read_entry()


#def import_progress():
    #"""docstring for import_progress"""
    #dbi = DatabaseInterface('sentence_library2.db')
    #dbi.reset_database()
    #importer = UELibraryImporter('out2')
    #parser = JapaneseParser()
    #lib_type = importer.type_
    #lib_id = dbi.get_or_create_library_id('Kenkyusha 5th', 1)
    #print lib_id
    #total_num_entries = num_entries('out2')
    #progress = ProgressPoint(1, 2, 0, total_num_entries)
    #for idx, entry in enumerate(importer.entries()):
        ##print entry
        #progress.point = idx
        #dbi.import_entry_recursive(entry, lib_id, parser)
        ##yield idx
        #yield progress
    #dbi.commit()

class ProgressPoint(object):
    """docstring for ProgressPoint
    Displays progress as a percentage"""
    def __init__(self, phase, total_phases, point, total_points):
        super(ProgressPoint, self).__init__()
        self.total_phases = total_phases
        self.phase = phase
        self.point = point
        self.total_points = total_points

    def percent(self):
        return (self.point / self.total_points) * 100

    def __str__(self):
        """docstring for __str__"""
        return "Phase {}/{}  {:3.2f}% {}".format(self.phase, 
                                         self.total_phases, 
                                         self.percent(),
                                         self.point)

def main():
    #import_library()
    #for progress in import_progress():
        #print progress
    dbi = DatabaseInterface('sentence_library3.db')
    importer = LibraryImporter('kenkyusha', dbi)
    #importer.set_db_path('sentence_library3.db')
    importer.set_library('WADAI5')
    #importer.prepare_library()
    for progress in importer.import_progress():
        print progress

if __name__ == '__main__':
    main()
