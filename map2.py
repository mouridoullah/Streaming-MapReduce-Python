#!/usr/bin/env python
import sys
import string

for line in sys.stdin:
    line = line.strip()
    splits = line.split("\t")

    tel = splits[0]
    nom = splits[1]
    prenom = splits[2]
    dept = splits[3]
    ville = splits[4]

    print('%s\t%s\t%s' % (tel, dept, ville))
