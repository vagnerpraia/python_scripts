# -*- coding: utf-8 -*-
import re

#row = "26:1 Entrevistador: E a desigualdade social, como é que você vê? Entrevist…… (25916:26035) - D 26: 101126e"
#row = "P 2: 101102e.doc - 2:128 [Entrevistador: O que você acha..]  (227:227)   (Super)"
row = "Report: 1369 quotation(s) for 1 code"

print '\nMatch 1:'
matchObj = re.match(r'([0-9]*):([0-9]*) .*', row, re.M|re.I)
if matchObj:
	print "Ok"
else:
	print "Error"


print "\nMatch 2:"
flagVersion = re.match(r'Report: [0-9]* quotation\(s\) for [0-9]* code(.*)?', row, re.M|re.I)
if flagVersion:
	print "Ok"
else:
	print "Error"
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