#!/usr/bin/env python
# parser.py - parse the results of the ASLR test

import sys

if len(sys.argv) < 2:
    print "Usage: ./parser.py <inputfile>"

# WARNING: this doesnt do any error checking

d = {}

f = open(sys.argv[1])
line = f.readline()

while True:
    try:
        i,time = line.split()[1:3]
        line = f.readline()
        lo = 0
        while "ASLR: " not in line:
            addr, hi = line.split()[0].split("-")
            if lo == 0:
                lo = addr
            line = f.readline()
        if lo == 0: continue
        #print i,time,int(lo,16),int(hi,16)
        if lo in d:
            d[lo] = d[lo] + 1
        else:
            d[lo] = 1
    except IndexError:
        if lo in d:
            d[lo] = d[lo] + 1
        else:
            d[lo] = 1
        #print i,time,int(lo,16),int(hi,16)
        break

for k in sorted(d.keys()):
    print int(k,16), d[k]
