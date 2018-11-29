# -*- coding: utf-8 -*-

import codecs

def check_encoding(path_file):
    result = ''

    encodings = ['utf-8', 'us-ascii', 'iso-8859-1', 'windows-1250', 'windows-1252']
    for e in encodings:
        try:
            fh = codecs.open(path_file, 'r', encoding = e)
            fh.readlines()
            fh.seek(0)
        except UnicodeDecodeError:
            None
        else:
            result = e
            break

    return result

print check_encoding('C:/Teste/atlas_to_iramuteq/questionario.txt')