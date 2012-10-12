#!/usr/bin/env python

from sys import argv
import os

"""
    Helper function, replaces a specific line
    in the file
"""
def replace_line(filename, line_num, text):
    lines = open(filename, 'r').readlines()
    lines[line_num] = text + "\n"
    out = open(filename, 'w')
    out.writelines(lines)
    out.close()

    
"""
    Will create a file in whatever directory this class 
    is located in. The supplied path must have no new lines
"""    
class WriteRC (object) :
    
    def __init__(self, filename=None) :
        self._filename = filename
        if os.path.exists(self.filename):
            print "file exists"
        else :
            f = open(self.filename, 'w+')
            #Dont write to file if it already exists
            f.write(".anki_database\n\n\n")
            f.write(".local_database\n\n\n")
            f.write(".i_plus_n\n\n\n")
            f.close()

    @property
    def filename(self):
        if self._filename is None:
            self._filename = 'rc1.txt'
        return self._filename
    
    def append_anki_path (self, anki) :
        replace_line(self.filename, 1, anki)
    
    def append_local_db_path (self, db_path) :
        replace_line(self.filename, 4, db_path)
    
    def append_i_plus_n (self, i_plus_n) :
        replace_line(self.filename, 7, i_plus_n)
        
"""    
    read = WriteRC()
    read.append_anki_path("test anki path")
    read.append_local_db_path("test db path")
    read.append_i_plus_n("test i+n path")
    read.append_local_db_path("test db path again")
"""

if __name__ == '__main__':
    rc_writer = WriteRC('rc2.txt')
    rc_writer.append_anki_path('anki path')
    rc_writer.append_local_db_path('db path')
    rc_writer.append_i_plus_n('i plus n')
