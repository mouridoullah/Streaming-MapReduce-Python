#!/usr/bin/env python
import sys
import string

last_dept = None
cur_ville = ""
count = 0

for line in sys.stdin:
    line = line.strip()
    tel, dept, ville = line.split("\t")
    # if this is the first iteration
    if not last_dept:
        last_dept = dept
        cur_ville = ville
        count = 1

    if dept == last_dept:
        if ville == cur_ville:
            count += 1
            cur_ville = ville
    else:
        print('%s\t%s\t%s' % (cur_ville, last_dept, count))
        last_dept = dept
        cur_ville = ville
        count_locations = 1

print('%s\t%s\t%s' % (ville, dept, count))
        