#!/usr/bin/env python
# ASLR-tester.py - test ASLR by looking at location of a library for a program lots and lots of times

import shlex, subprocess, sys, time

if len(sys.argv) < 2:
    print "Usage: ./ASLR-tester.py <lib> <program> [arg [arg [arg...]]]"
    exit(1)

lib = sys.argv[1]
args = sys.argv[2:]

i = 0

while True:
    p = subprocess.Popen(args)
    print 'ASLR:',i, time.time()
    time.sleep(0.05) # wait a millisecond
    f = open('/proc/'+str(p.pid)+'/maps')
    for line in f:
        if lib in line:
            print line.strip()
    f.close()
    i += 1
    p.wait()
