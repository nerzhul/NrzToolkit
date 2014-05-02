#! /usr/local/bin/python2.7
# -*- coding: utf-8 -*- #

import NrzDataStorage, NrzConfig

def generate():
	htmlBuffer = "<div>Prochain RER %s en gare de %s</div><div>Le %s à %s</div>" % (NrzConfig.RERType, NrzConfig.RERStation, NrzDataStorage.RERhour, NrzDataStorage.RERday)
	
	outFile = open("/var/www/htdocs/index.htm","wb")
	outFile.write(htmlBuffer)
	outFile.close()
