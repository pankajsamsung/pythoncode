#! /usr/bin/env python

# ex_argv2.py - Args Demo
import sys
 
# Get the total number of args passed to the ex_argv.py
total = len(sys.argv)
 
# Get the arguments list 
cmdargs = str(sys.argv)
 
# Print it
print ("The total numbers of args passed to the script: %d " % total)
print ("Args list: %s " % cmdargs)
#for i in range(len(cmdargs)):
#    print(i)
 #   print ("%s" % cmdargs[i])