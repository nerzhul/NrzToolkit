#! /usr/local/bin/python2.7

from BeautifulSoup import BeautifulSoup
import NrzHTML, NrzConfig

def parseRER():
	htmlPage = NrzHTML.getPage("http://www.ratp.fr/horaires/fr/ratp/rer/prochains_passages/R%s/%s/A" % (NrzConfig.RERType,NrzConfig.RERStation))
	if htmlPage == -1:
		return htmlPage

	#print htmlPage
	htmlParsed = BeautifulSoup(htmlPage)
	htmlPage = None

	print htmlParsed.body.find('span', attrs={'class':'time'}).text
	return 0
