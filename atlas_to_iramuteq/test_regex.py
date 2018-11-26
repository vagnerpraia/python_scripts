# -*- coding: utf-8 -*-
import re

#row = "26:1 Entrevistador: E a desigualdade social, como é que você vê? Entrevist…… (25916:26035) - D 26: 101126e"
#row = "P 2: 101102e.doc - 2:128 [Entrevistador: O que você acha..]  (227:227)   (Super)"
row = "Report: 1369 quotation(s) for 1 code"
key_interview = '101126e'

print '\nMatch 1:'
match1 = re.match(r'([0-9]*):([0-9]*) .*', row, re.M|re.I)
if match1: print "Ok"
else: print "Error"

print "\nMatch 2:"
match2 = re.match(r'Report: [0-9]* quotation\(s\) for [0-9]* code(.*)?', row, re.M|re.I)
if match2: print "Ok"
else: print "Error"

print '\nMatch 3:'
match3 = re.match(r'[0-9]*e', key_interview, re.M|re.I)
if match3: print "Ok: " + key_interview[:-1]
else: print "Error"

'''
print '\nSearch:'
searchObj = re.search(r' - . [0-9]*: ', row, re.M|re.I)
if searchObj:
	print searchObj.group()
	print "Ok"
else:
	print "Error"

print "\nLast:"
print row[len(row) - 1]
'''