#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import codecs

re_entry = re.compile(ur'ﾛｰﾏ')
re_entry_split1 = re.compile(ur'^(.*?)([ 【].*$)')
re_entry_split2 = re.compile(ur'^(.*?)([１２３４５６７８９０]*)$')
re_entry_split3 = re.compile(ur'【(.*?)】')
re_entry_word_sep = re.compile(ur'・')
re_ue = re.compile(ur'^[▲・◧◨]?(.*)　(.*)$')
re_numbered_meaning = re.compile(ur'^[0-9]+ (.*)$')
re_example_sentence = re.compile(ur'[.」!?]　')
re_example_sentence_filter1 = re.compile(ur'<LINK>')
re_example_sentence_filter2 = re.compile(ur'^…')
#re_word_form = re.compile(r'^[^　]*$')

has_multiple_meanings = False
entry_number = 0
in_entry = False
in_meaning = False
#in_word_form = False

class Kenkyusha5DumpConverter(object):
    """docstring for Kenkyusha5DumpConverter
    
    The purpose of the converter is to extract words,
    definitions, meanings, usage examples from the Kenkysha 5 library
    into an usable format for the database.
    
    """
    def __init__(self, dumpfile):
        super(Kenkyusha5DumpConverter, self).__init__()
        self.dumpfile = dumpfile

    def convert(self, outfile):
        """docstring for convert'
        
        Convert is a function that runs through a series of regular expressions to extract the necessary items from the dump file.
        
        It delimites the file through tabs and ensures it captures words, the associated meanings and sentences.
        """
        fh_out = open(outfile,"w")
        #fh_out.write(self.replace_gaiji_hex(utf8_content))

        #formation, phrase
        fh_in = codecs.open(self.dumpfile, 'r', encoding='utf-8')
        print >>fh_out, "NAME: Kenkyusha's New Japanese-English Dictionary 5th"
        print >>fh_out, "TYPE: DICTIONARY"
        print >>fh_out, "FORMAT: TABS"
        print >>fh_out, "KANJI-SEP: PIPE"
        print >>fh_out, ''
        for line in fh_in:
            #line = line.decode('utf-8')
            if line == '\n':
                continue
            if re_entry.search(line):
                in_entry = True
                in_meaning = False
                in_word_form = False
                has_multiple_meanings = True
                e = split_entry(line)
                print >>fh_out, entry_string(kana=e['kana'], 
                        number=e['number'], kanji=e['kanji']).encode('utf-8')
                #print "{}".format(line.encode('utf-8')),
            elif in_entry == True:
                nm = re_numbered_meaning.match(line)
                if (nm and has_multiple_meanings == True):
                    in_meaning = True
                    in_word_form = False
                    print >>fh_out, "\t{}".format(nm.group(1).encode('utf-8'))
                elif in_meaning == False:
                    has_multiple_meanings = False
                    in_meaning = True
                    in_word_form = False
                    m = match_sentence(line)
                    if m:
                        print >>fh_out, "\t"
                        print >>fh_out, "\t\t{}\t{}".format(
                                m.group(1).encode('utf-8'), 
                                m.group(2).encode('utf-8'))
                    else:
                        print >>fh_out, "\t{}".format(line.encode('utf-8')),
                elif in_meaning == True:
                    m = match_sentence(line)
                    if m:
                        print >>fh_out, "\t\t{}\t{}".format(
                                m.group(1).encode('utf-8'), 
                                m.group(2).encode('utf-8'))
                    #else:
                        #print "\t\t<P>{}".format(line),




        fh_out.close()

def split_entry(entry_line):
    """docstring for split_entry
    Function helps seperate entries and ensure we dont double up.
    """
    m1 = re_entry_split1.match(entry_line)
    if m1:
        kana_and_number = m1.group(1)
        kanji_and_stuff = m1.group(2)
        m2 = re_entry_split2.match(kana_and_number)
        if m2:
            kana = m2.group(1)
            # number of word seps to skip for kanji
            num_sep = len(re_entry_word_sep.findall(kana))
            number = m2.group(2)
            if number == '':
                number = None
            else:
                number = int(number)
        else:
            raise Exception("didn't match split2")

        kanji = None
        m3 = re_entry_split3.search(kanji_and_stuff)
        if m3:
            kanji = list()
            kanji_unsplit = m3.group(1)
            kanji_over_split = re_entry_word_sep.split(kanji_unsplit)
            build_kanji = list()
            for k in kanji_over_split:
                build_kanji.append(k)
                if len(build_kanji) == num_sep+1:
                    kanji.append(u'・'.join(build_kanji))
                    build_kanji = list()
    else:
        raise Exception("didn't match split1")
    return {'kana':kana, 'number':number, 'kanji':kanji}

def match_sentence(line):
    """docstring for match_sentence
    Checks if passed sentences is matched in database.
    """
    if re_example_sentence.search(line):
        if (re_example_sentence_filter1.search(line) is None
            and
            re_example_sentence_filter2.match(line) is None):
            m = re_ue.match(line)
            return m
    return None

def entry_string(kana, number, kanji):
    """forming a string for an entry
    A entry has 3 elements: kana, kanji and string length"""
    out = list()
    out.append(kana)
    if kanji is None:
        out.append('')
    else:
        out.append('|'.join(kanji))
    if number is None:
        out.append('')
    else:
        out.append(str(number))
    return '\t'.join(out)


if __name__ == '__main__':
    #formation, phrase
    f = codecs.open('wadai5.dump', 'r', encoding='utf-8')
    print "NAME: Kenkyusha's New Japanese-English Dictionary 5th"
    print "TYPE: DICTIONARY"
    print "FORMAT: TABS"
    print "KANJI-SEP: PIPE"
    print
    for line in f:
        #line = line.decode('utf-8')
        if line == '\n':
            continue
        if re_entry.search(line):
            in_entry = True
            in_meaning = False
            in_word_form = False
            has_multiple_meanings = True
            e = split_entry(line)
            print entry_string(kana=e['kana'], 
                    number=e['number'], kanji=e['kanji']).encode('utf-8')
            #print "{}".format(line.encode('utf-8')),
        elif in_entry == True:
            nm = re_numbered_meaning.match(line)
            if (nm and has_multiple_meanings == True):
                in_meaning = True
                in_word_form = False
                print "\t{}".format(nm.group(1).encode('utf-8'))
            elif in_meaning == False:
                has_multiple_meanings = False
                in_meaning = True
                in_word_form = False
                m = match_sentence(line)
                if m:
                    print "\t"
                    print "\t\t{}\t{}".format(
                            m.group(1).encode('utf-8'), 
                            m.group(2).encode('utf-8'))
                else:
                    print "\t{}".format(line.encode('utf-8')),
            elif in_meaning == True:
                m = match_sentence(line)
                if m:
                    print "\t\t{}\t{}".format(
                            m.group(1).encode('utf-8'), 
                            m.group(2).encode('utf-8'))
                #else:
                    #print "\t\t<P>{}".format(line),
