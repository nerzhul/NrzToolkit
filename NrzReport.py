#! /usr/local/bin/python2.7
# -*- coding: utf-8 -*- #

import NrzDataStorage, NrzConfig

def generate(_store):
	htmlBuffer = "<div>Prochain RER %s en gare de %s</div><div>Le %s a %s</div>" % (NrzConfig.RERType, NrzConfig.RERStation, _store.RERday, _store.RERhour)
	
	outFile = open(NrzConfig.ReportPath,"wb")
	outFile.write(htmlBuffer)
	outFile.close()
