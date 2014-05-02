#! /usr/local/bin/python2.7

import RATP
import NrzReport

ret = RATP.parseRER()

NrzReport.generate()
if ret == -1:
	print "RATP.parseRER: FATAL ERROR (return code %s)" % ret
else:
	print "Generation: OK"
