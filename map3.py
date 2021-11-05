#!/usr/bin/env python
import sys
import string

for line in sys.stdin:
    line = line.strip()
    splits = line.split("\t")

    ville = splits[0]
    dept = splits[1]
    count = splits[2]

    if(dept == "78" and int(count) > 2):
        print('%s\t%s' % (ville, dept))
