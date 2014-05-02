#! /usr/local/bin/python2.7
# -*- coding: utf-8 -*- #

from BeautifulSoup import BeautifulSoup
import NrzHTML, NrzConfig, NrzDataStorage

def parseRER(_store):
	htmlPage = NrzHTML.getPage("http://www.ratp.fr/horaires/fr/ratp/rer/prochains_passages/R%s/%s/%s" % (NrzConfig.RERType,NrzConfig.RERStation,NrzConfig.RERSens))
	if htmlPage == -1:
		return htmlPage

	#print htmlPage
	htmlParsed = BeautifulSoup(htmlPage)
	htmlPage = None

	_store.RERhour = htmlParsed.body.find('span', attrs={'class':'time'}).text
	_store.RERday = htmlParsed.body.find('span', attrs={'class':'date'}).text
	return 0
