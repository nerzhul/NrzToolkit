#! /usr/local/bin/python2.7

import RATP
import NrzReport, NrzDataStorage

_store = NrzDataStorage.NrzStore()

ret = RATP.parseRER(_store)

NrzReport.generate(_store)

if ret == -1:
	print "RATP.parseRER: FATAL ERROR (return code %s)" % ret
else:
	print "Generation: OK"
