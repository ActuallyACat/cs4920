#!/usr/bin/env python
# -*- coding: utf-8 -*-

from noj.data_structures import *

class UEExporter(object):
    """Export a list of UEs to TSV format"""
    def __init__(self, ue_list=None):
        super(UEExporter, self).__init__()
        self.ue_list = ue_list
        
    def add_ue_list(self, ue_list):
        self.ue_list = ue_list

    def export(self, fname):
        """Export UsageExamples to TSV file."""
        f = open(fname, 'w')
        for ue in self.ue_list:
            line_components = list()
            line_components.append(ue.expression)
            line_components.append(ue.meaning)
            print >>f, '\t'.join(line_components).encode('utf-8')

if __name__ == '__main__':
    exporter = UEExporter()
    ue_list = list()
    ue = UsageExample(u'\u300c\u30d1\u30d1, \u65e9\u304f\u6765\u3066\u300d\u300c\u3042\u3042, \u4eca\u884c\u304f\u3088\u300d', u'"Daddy! Come quickly!"\u2015"OK [All right], I\'m coming."', 0)
    ue_list.append(ue)
    ue = UsageExample(u'\u3042\u3042\u306a\u3063\u305f\u306e\u3082\u81ea\u696d\u81ea\u5f97\u3055.', u"He brought that on himself. \uff5c He has only himself to blame for that. \uff5c It's his own fault that it turned out that way.", 0)
    ue_list.append(ue)
    exporter.add_ue_list(ue_list)
    exporter.export('exportedTSV.txt')
