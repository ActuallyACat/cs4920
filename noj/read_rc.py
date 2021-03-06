#!/usr/bin/env python

from sys import argv
from noj.write_rc import *

""" 
    ReadRC opens the rc.txt file, and 
    returns the path of the anki, database, 
    and i+n value
    
    file has the format (for readability): 
    0 .anki_database
    1 C:\anki\path
    2
    3 .local_database
    4 C:\local\database
       5
    6 .i_plus_n 
    7 int_value

    Note: filename must be absolute path, i.e
    C:/Users/blah/desktop/blah/filename.txt
"""
class ReadRC (object) :

    def __init__(self, filename) :
        self.filename = filename
        try:
            f = open(filename)
        except IOError as e:
            writer = WriteRC(filename)
            f = open(filename)
        self.file = f.readlines()

    def get_anki (self) :
        return self.file[1].rstrip('\n')
                    
    def get_local_db(self) :
        return self.file[4].rstrip('\n')

    def get_i_plus_n (self):
        return self.file[7].rstrip('\n')


"""        
script, filename = argv

txt = open(filename)
read = ReadRC(filename)

print "ANKI: %r" % read.get_anki()
print "LOCAL: %r" % read.get_local_db()
print "i+n: %r" % read.get_i_plus_n()
"""

if __name__ == '__main__':
    rc_reader = ReadRC('rc2.txt')
    print rc_reader.get_anki()
    print rc_reader.get_local_db()
    print rc_reader.get_i_plus_n()
    rc_reader = ReadRC('fileThatDoesntExist')

