'''
Created on 2 de out de 2016

@author: vagnerpraia
'''

from re import sub

def find_between(s, first, last):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_between_r(s, first, last):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

def strip_non_ascii(text):
    '''
    stripped = (c for c in text if 0 < ord(c) < 127)
    return ''.join(stripped)
    '''
    return sub(r'[^\x00-\xa3]', r'', text)