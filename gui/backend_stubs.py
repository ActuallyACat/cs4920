#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tests.sample_entries_1 import *
from noj.data_structures import *

def dictionary_mode_search(string):
    """docstring for dictionary_mode_search
    Searches string through DB to find all possible matches for entries
	Returns it as a list with respective meanings attached
	"""
    #print SAMPLE_ENTRIES_1
    list_of_entries = list()
    #list_of_entries.append(SAMPLE_ENTRIES_2[0])
    return SAMPLE_ENTRIES_2
    #return list_of_entries

def lookup_mode_search(string):
    """docstring for lookup_mode_search
	Searches string through DB to find all possible matches for entries
	Returns it as a list of usage examples attached to respective entries
	"""
    #print SAMPLE_ENTRIES_1
    list_of_ues = list()
    for entry in SAMPLE_ENTRIES_2:
        for meaning in entry.meanings:
            for ue in meaning.usage_examples:
                list_of_ues.append(ue)
    return list_of_ues

def get_user_ue_lists():
    list_of_ue_lists = list()
    ue_list = UsageExampleList('List1')
    #ue_list.add_usage_example
